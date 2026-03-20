# Orquestrador de Automação — Context Guardian

Implementações para transferência automática de contexto sem intervenção do usuário.
Escolha o ambiente que se aplica ao seu caso.

---

## Como a Automação Funciona

O fluxo é o mesmo em todos os ambientes:

```
1. MONITORAR  → checar uso de tokens a cada resposta
2. DETECTAR   → limiar atingido OU sinal semântico de degradação
3. EVACUAR    → chamar Claude com instrução de gerar o relatório completo
4. TRANSFERIR → iniciar nova sessão com o relatório como contexto inicial
5. CONTINUAR  → novo agente responde de onde o anterior parou
```

**Limiares recomendados:**
- `claude-opus-4-6`    → transferir ao atingir ~180.000 tokens (janela: 200k)
- `claude-sonnet-4-6`  → transferir ao atingir ~180.000 tokens (janela: 200k)
- `claude-haiku-4-5`   → transferir ao atingir ~180.000 tokens (janela: 200k)
- Gatilho preventivo recomendado: **85% da janela** para ter margem para a evacuação

---

## Implementação 1 — Python (API Direta)

```python
"""
context_guardian_orchestrator.py

Orquestrador completo para transferência automática de contexto.
Requer: pip install anthropic
"""

import anthropic
import json
from dataclasses import dataclass, field
from typing import Optional

# ─── Configuração ────────────────────────────────────────────────────────────

MODEL = "claude-sonnet-4-6"
MAX_TOKENS_RESPONSE = 8192
CONTEXT_LIMIT = 200_000          # janela máxima do modelo
EVACUATION_THRESHOLD = 0.85      # evacuar ao atingir 85% da janela
EVACUATION_TOKEN_LIMIT = int(CONTEXT_LIMIT * EVACUATION_THRESHOLD)

EVACUATION_INSTRUCTION = """
CONTEXT GUARDIAN — MODO EVACUAÇÃO ATIVADO

Gere imediatamente o Relatório de Transferência completo seguindo esta estrutura:

# RELATÓRIO DE TRANSFERÊNCIA — CONTEXT GUARDIAN

## 🔴 ITENS CRÍTICOS (ler primeiro)
[liste os fatos/decisões/restrições que o novo agente deve saber imediatamente]

## 🎯 IDENTIDADE DO PROJETO
- Projeto: [nome]
- Objetivo: [uma frase precisa]
- Contexto do usuário: [papel/domínio se mencionado]

## ⚙️ STACK TÉCNICA
[linguagens, frameworks, versões, infra]

## 📌 DECISÕES TOMADAS (cronológicas)
[cada decisão com justificativa e alternativas rejeitadas]

## 💻 CÓDIGO E ARTEFATOS
[estrutura de arquivos, snippets críticos, código incompleto]

## 📋 REQUISITOS E RESTRIÇÕES
[funcionais, técnicos, preferências do usuário]

## 🔍 PROBLEMAS E TENTATIVAS
[problemas, o que falhou e por quê, solução adotada]

## 📍 ESTADO NO MOMENTO DA EVACUAÇÃO
- O que estava sendo feito: [descrição exata]
- Ponto de parada: [última ação/linha/decisão]
- Próximos passos: [lista ordenada]

## ❓ PENDÊNCIAS
[questões em aberto, decisões não tomadas]

---
## PROMPT DE RETOMADA PARA NOVO AGENTE

[gere aqui um bloco auto-suficiente que o novo agente pode receber como 
primeira mensagem e saber exatamente onde continurar, incluindo:
- identidade e objetivo
- decisões tomadas (não questionar)
- restrições absolutas
- estado atual e ponto exato de parada
- primeira ação imperativa a executar]

Regras: completude > brevidade. Não omitir nada. Incluir todo código parcial.
"""


# ─── Estruturas de dados ─────────────────────────────────────────────────────

@dataclass
class ConversationState:
    messages: list = field(default_factory=list)
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    transfer_count: int = 0
    evacuation_report: Optional[str] = None


# ─── Cliente ─────────────────────────────────────────────────────────────────

client = anthropic.Anthropic()  # usa ANTHROPIC_API_KEY do ambiente


# ─── Funções principais ───────────────────────────────────────────────────────

def estimate_tokens(messages: list) -> int:
    """Estimativa rápida: ~4 chars por token."""
    total_chars = sum(
        len(m["content"]) if isinstance(m["content"], str)
        else sum(len(b.get("text", "")) for b in m["content"])
        for m in messages
    )
    return total_chars // 4


def needs_evacuation(state: ConversationState) -> bool:
    """Verifica se é necessário evacuar com base nos tokens."""
    estimated = estimate_tokens(state.messages)
    return estimated >= EVACUATION_TOKEN_LIMIT


def generate_evacuation_report(state: ConversationState) -> str:
    """Chama Claude para gerar o relatório completo de transferência."""
    print("\n⚠️  CONTEXT GUARDIAN — Iniciando evacuação...")
    print(f"   Tokens estimados: {estimate_tokens(state.messages):,}")
    print(f"   Limite configurado: {EVACUATION_TOKEN_LIMIT:,}")

    evacuation_messages = state.messages + [
        {"role": "user", "content": EVACUATION_INSTRUCTION}
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS_RESPONSE,
        messages=evacuation_messages,
    )

    report = response.content[0].text
    print("✅  Relatório de transferência gerado.")
    return report


def save_report(report: str, transfer_count: int) -> str:
    """Salva o relatório em arquivo .md."""
    filename = f"context-guardian-transfer-{transfer_count:02d}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"💾  Relatório salvo em: {filename}")
    return filename


def extract_handoff_prompt(report: str) -> str:
    """Extrai o bloco 'PROMPT DE RETOMADA' do relatório para usar como
    primeira mensagem da nova sessão."""
    marker = "## PROMPT DE RETOMADA PARA NOVO AGENTE"
    if marker in report:
        return report.split(marker, 1)[1].strip()
    # fallback: usar o relatório completo
    return report


def transfer_session(state: ConversationState) -> ConversationState:
    """Executa a evacuação e inicia nova sessão com contexto transferido."""
    state.transfer_count += 1

    # 1. Gerar relatório
    report = generate_evacuation_report(state)

    # 2. Salvar arquivo .md
    filename = save_report(report, state.transfer_count)

    # 3. Extrair Prompt de Retomada
    handoff_prompt = extract_handoff_prompt(report)

    # 4. Iniciar nova sessão com o relatório como contexto
    new_state = ConversationState(
        transfer_count=state.transfer_count,
        evacuation_report=report,
    )

    # Primeira mensagem da nova sessão = Prompt de Retomada
    new_state.messages = [
        {
            "role": "user",
            "content": (
                f"[CONTEXT GUARDIAN — Transferência #{state.transfer_count}]\n\n"
                f"{handoff_prompt}"
            )
        }
    ]

    # Confirmar que o novo agente recebeu o contexto
    confirmation = client.messages.create(
        model=MODEL,
        max_tokens=512,
        messages=new_state.messages,
    )

    new_state.messages.append({
        "role": "assistant",
        "content": confirmation.content[0].text
    })

    print(f"\n🔄  Nova sessão iniciada (transferência #{state.transfer_count})")
    print(f"    Arquivo de referência: {filename}")
    print(f"    Confirmação do novo agente:\n    {confirmation.content[0].text[:200]}...\n")

    return new_state


def chat(state: ConversationState, user_message: str) -> tuple[str, ConversationState]:
    """Envia mensagem, verifica necessidade de evacuação e retorna resposta."""

    # Verificar necessidade de evacuação ANTES de enviar
    if needs_evacuation(state):
        state = transfer_session(state)

    # Adicionar mensagem do usuário
    state.messages.append({"role": "user", "content": user_message})

    # Enviar para Claude
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS_RESPONSE,
        messages=state.messages,
    )

    assistant_message = response.content[0].text

    # Registrar resposta
    state.messages.append({"role": "assistant", "content": assistant_message})
    state.total_input_tokens += response.usage.input_tokens
    state.total_output_tokens += response.usage.output_tokens

    return assistant_message, state


# ─── Loop principal ───────────────────────────────────────────────────────────

def main():
    print("🛡️  Context Guardian — Orquestrador Python")
    print(f"   Modelo: {MODEL}")
    print(f"   Limiar de evacuação: {EVACUATION_TOKEN_LIMIT:,} tokens ({int(EVACUATION_THRESHOLD*100)}%)")
    print("   Digite 'sair' para encerrar, 'status' para ver tokens\n")

    state = ConversationState()

    while True:
        user_input = input("Você: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "sair":
            break
        if user_input.lower() == "status":
            estimated = estimate_tokens(state.messages)
            pct = (estimated / CONTEXT_LIMIT) * 100
            print(f"\n📊 Status do contexto:")
            print(f"   Tokens estimados: {estimated:,} / {CONTEXT_LIMIT:,} ({pct:.1f}%)")
            print(f"   Transferências realizadas: {state.transfer_count}")
            print(f"   Limiar de evacuação: {EVACUATION_TOKEN_LIMIT:,} tokens\n")
            continue

        response, state = chat(state, user_input)
        print(f"\nClaude: {response}\n")

    print(f"\nSessão encerrada. Total de transferências: {state.transfer_count}")


if __name__ == "__main__":
    main()
```

---

## Implementação 2 — Node.js / TypeScript (API Direta)

```typescript
/**
 * context-guardian-orchestrator.ts
 * 
 * Orquestrador para transferência automática de contexto.
 * Requer: npm install @anthropic-ai/sdk
 */

import Anthropic from "@anthropic-ai/sdk";
import * as fs from "fs";

// ─── Configuração ─────────────────────────────────────────────────────────

const MODEL = "claude-sonnet-4-6";
const CONTEXT_LIMIT = 200_000;
const EVACUATION_THRESHOLD = 0.85;
const EVACUATION_LIMIT = Math.floor(CONTEXT_LIMIT * EVACUATION_THRESHOLD);
const MAX_TOKENS_RESPONSE = 8192;

const EVACUATION_INSTRUCTION = `
CONTEXT GUARDIAN — MODO EVACUAÇÃO ATIVADO

Gere o Relatório de Transferência completo com:
- Itens críticos (ler primeiro)
- Identidade e objetivo do projeto
- Stack técnica completa
- Todas as decisões tomadas (cronológicas, com justificativas)
- Código e artefatos produzidos
- Requisitos e restrições
- Problemas, tentativas fracassadas e soluções
- Estado exato no momento da evacuação
- Próximos passos ordenados
- PROMPT DE RETOMADA PARA NOVO AGENTE (bloco auto-suficiente)

Regra absoluta: completude > brevidade. Incluir todo código parcial.
`;

// ─── Tipos ────────────────────────────────────────────────────────────────

interface Message {
  role: "user" | "assistant";
  content: string;
}

interface SessionState {
  messages: Message[];
  transferCount: number;
  totalInputTokens: number;
  totalOutputTokens: number;
}

// ─── Cliente ──────────────────────────────────────────────────────────────

const client = new Anthropic(); // usa ANTHROPIC_API_KEY do ambiente

// ─── Funções ──────────────────────────────────────────────────────────────

function estimateTokens(messages: Message[]): number {
  const totalChars = messages.reduce((sum, m) => sum + m.content.length, 0);
  return Math.floor(totalChars / 4);
}

function needsEvacuation(state: SessionState): boolean {
  return estimateTokens(state.messages) >= EVACUATION_LIMIT;
}

function extractHandoffPrompt(report: string): string {
  const marker = "## PROMPT DE RETOMADA PARA NOVO AGENTE";
  if (report.includes(marker)) {
    return report.split(marker)[1].trim();
  }
  return report;
}

async function generateEvacuationReport(state: SessionState): Promise<string> {
  console.log("\n⚠️  CONTEXT GUARDIAN — Iniciando evacuação...");

  const evacuationMessages = [
    ...state.messages,
    { role: "user" as const, content: EVACUATION_INSTRUCTION },
  ];

  const response = await client.messages.create({
    model: MODEL,
    max_tokens: MAX_TOKENS_RESPONSE,
    messages: evacuationMessages,
  });

  const report = (response.content[0] as { text: string }).text;
  console.log("✅  Relatório gerado.");
  return report;
}

async function transferSession(state: SessionState): Promise<SessionState> {
  const newTransferCount = state.transferCount + 1;

  // 1. Gerar relatório
  const report = await generateEvacuationReport(state);

  // 2. Salvar arquivo .md
  const filename = `context-guardian-transfer-${String(newTransferCount).padStart(2, "0")}.md`;
  fs.writeFileSync(filename, report, "utf-8");
  console.log(`💾  Relatório salvo: ${filename}`);

  // 3. Extrair Prompt de Retomada
  const handoffPrompt = extractHandoffPrompt(report);

  // 4. Iniciar nova sessão
  const newState: SessionState = {
    messages: [],
    transferCount: newTransferCount,
    totalInputTokens: 0,
    totalOutputTokens: 0,
  };

  const firstMessage: Message = {
    role: "user",
    content: `[CONTEXT GUARDIAN — Transferência #${newTransferCount}]\n\n${handoffPrompt}`,
  };

  newState.messages.push(firstMessage);

  // Confirmação do novo agente
  const confirmation = await client.messages.create({
    model: MODEL,
    max_tokens: 512,
    messages: newState.messages,
  });

  const confirmText = (confirmation.content[0] as { text: string }).text;
  newState.messages.push({ role: "assistant", content: confirmText });

  console.log(`\n🔄  Nova sessão iniciada (transferência #${newTransferCount})`);
  console.log(`    Confirmação: ${confirmText.substring(0, 150)}...\n`);

  return newState;
}

async function chat(
  state: SessionState,
  userMessage: string
): Promise<[string, SessionState]> {
  let currentState = state;

  // Verificar evacuação antes de enviar
  if (needsEvacuation(currentState)) {
    currentState = await transferSession(currentState);
  }

  currentState.messages.push({ role: "user", content: userMessage });

  const response = await client.messages.create({
    model: MODEL,
    max_tokens: MAX_TOKENS_RESPONSE,
    messages: currentState.messages,
  });

  const assistantMessage = (response.content[0] as { text: string }).text;

  currentState.messages.push({ role: "assistant", content: assistantMessage });
  currentState.totalInputTokens += response.usage.input_tokens;
  currentState.totalOutputTokens += response.usage.output_tokens;

  return [assistantMessage, currentState];
}

// ─── Main ─────────────────────────────────────────────────────────────────

async function main() {
  const readline = await import("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  console.log("🛡️  Context Guardian — Orquestrador Node.js/TypeScript");
  console.log(`   Limiar de evacuação: ${EVACUATION_LIMIT.toLocaleString()} tokens\n`);

  let state: SessionState = {
    messages: [],
    transferCount: 0,
    totalInputTokens: 0,
    totalOutputTokens: 0,
  };

  const ask = (prompt: string): Promise<string> =>
    new Promise((resolve) => rl.question(prompt, resolve));

  while (true) {
    const input = (await ask("Você: ")).trim();

    if (!input) continue;
    if (input.toLowerCase() === "sair") break;
    if (input.toLowerCase() === "status") {
      const est = estimateTokens(state.messages);
      console.log(`\n📊 Tokens: ~${est.toLocaleString()} / ${CONTEXT_LIMIT.toLocaleString()} (${((est/CONTEXT_LIMIT)*100).toFixed(1)}%)`);
      console.log(`   Transferências: ${state.transferCount}\n`);
      continue;
    }

    const [response, newState] = await chat(state, input);
    state = newState;
    console.log(`\nClaude: ${response}\n`);
  }

  rl.close();
}

main().catch(console.error);
```

---

## Implementação 3 — Claude Code (Automação Total com Subagentes)

No Claude Code, a transferência é nativa — não precisa de orquestrador externo.

```bash
# Ativar o Context Guardian no início de qualquer sessão Claude Code:
claude --system "$(cat context-guardian-system-prompt.txt)" -p "ativar context guardian"
```

**context-guardian-system-prompt.txt:**
```
Você tem acesso ao Context Guardian. Monitore seu uso de contexto continuamente.

Quando atingir 85% da janela de contexto OU detectar qualquer sinal de degradação:
1. Gere o Relatório de Transferência completo (conforme skill context-guardian)
2. Salve em arquivo .md com timestamp
3. Spawne novo subagente com: claude -p "[conteúdo do Prompt de Retomada]"
4. Encaminhe a resposta do subagente de volta ao usuário
5. Continue a conversa através do subagente sem interromper o fluxo

O usuário não deve perceber a transição — mantenha continuidade total.
```

**Script de automação Claude Code (bash):**
```bash
#!/bin/bash
# guardian-session.sh — Sessão com transferência automática

REPORT_DIR="./cg-reports"
mkdir -p "$REPORT_DIR"

SESSION_ID=$(date +%Y%m%d-%H%M%S)
TRANSFER=0

echo "🛡️  Context Guardian — Sessão $SESSION_ID"

# Loop de sessão com transferência automática
while true; do
  TRANSFER=$((TRANSFER + 1))
  REPORT_FILE="$REPORT_DIR/transfer-$SESSION_ID-$TRANSFER.md"
  
  if [ $TRANSFER -eq 1 ]; then
    # Primeira sessão — sem contexto anterior
    claude --dangerously-skip-permissions \
           -p "ativar context guardian. sessão $SESSION_ID"
  else
    # Sessões subsequentes — injetar relatório anterior
    HANDOFF=$(cat "$REPORT_DIR/transfer-$SESSION_ID-$((TRANSFER-1)).md")
    claude --dangerously-skip-permissions \
           -p "[CONTEXT GUARDIAN — Transferência #$TRANSFER]

$HANDOFF

Continue exatamente de onde parou. Primeira ação: retomar o último ponto pendente."
  fi
  
  # Verificar se encerrou normalmente ou pediu transferência
  EXIT_CODE=$?
  if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Sessão encerrada normalmente."
    break
  fi
done
```

---

## Implementação 4 — n8n (Automação Visual, Sem Código)

Fluxo para o n8n que monitora tokens e transfere automaticamente.

```json
{
  "name": "Context Guardian — Auto Transfer",
  "nodes": [
    {
      "name": "Receber Mensagem do Usuário",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "chat",
        "method": "POST"
      }
    },
    {
      "name": "Buscar Estado da Sessão",
      "type": "n8n-nodes-base.redis",
      "parameters": {
        "operation": "get",
        "key": "={{ $json.session_id }}"
      }
    },
    {
      "name": "Verificar Limite de Tokens",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "number": [{
            "value1": "={{ $json.token_count }}",
            "operation": "largerEqual",
            "value2": 170000
          }]
        }
      }
    },
    {
      "name": "Chamar Claude — Evacuação",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.anthropic.com/v1/messages",
        "method": "POST",
        "headers": {
          "x-api-key": "={{ $env.ANTHROPIC_API_KEY }}",
          "anthropic-version": "2023-06-01"
        },
        "body": {
          "model": "claude-sonnet-4-6",
          "max_tokens": 8192,
          "messages": "={{ $json.messages.concat([{role:'user',content:'CONTEXT GUARDIAN — EVACUAÇÃO: gere o Relatório de Transferência completo com Prompt de Retomada'}]) }}"
        }
      }
    },
    {
      "name": "Salvar Relatório",
      "type": "n8n-nodes-base.writeBinaryFile",
      "parameters": {
        "fileName": "=cg-transfer-{{ $now.format('YYYYMMDD-HHmmss') }}.md",
        "dataPropertyName": "report"
      }
    },
    {
      "name": "Iniciar Nova Sessão",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.anthropic.com/v1/messages",
        "method": "POST",
        "body": {
          "model": "claude-sonnet-4-6",
          "max_tokens": 8192,
          "messages": [{
            "role": "user",
            "content": "={{ '[CONTEXT GUARDIAN — Nova Sessão]\\n\\n' + $json.handoff_prompt }}"
          }]
        }
      }
    },
    {
      "name": "Atualizar Estado no Redis",
      "type": "n8n-nodes-base.redis",
      "parameters": {
        "operation": "set",
        "key": "={{ $json.session_id }}",
        "value": "={{ JSON.stringify({messages: $json.new_messages, token_count: 0, transfer_count: $json.transfer_count + 1}) }}"
      }
    },
    {
      "name": "Chamar Claude — Normal",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.anthropic.com/v1/messages",
        "method": "POST",
        "body": {
          "model": "claude-sonnet-4-6",
          "max_tokens": 8192,
          "messages": "={{ $json.messages }}"
        }
      }
    },
    {
      "name": "Retornar Resposta",
      "type": "n8n-nodes-base.respondToWebhook",
      "parameters": {
        "responseBody": "={{ {response: $json.content[0].text, transferred: false} }}"
      }
    }
  ]
}
```

**Variáveis de ambiente necessárias no n8n:**
```
ANTHROPIC_API_KEY=sk-ant-...
REDIS_HOST=localhost
REDIS_PORT=6379
```

---

## Comparativo de Implementações

| Critério | Python | Node.js | Claude Code | n8n |
|---|---|---|---|---|
| **Automação** | Total | Total | Total | Total |
| **Visibilidade da transferência** | Terminal | Terminal | Invisível | Dashboard |
| **Persistência entre sessões** | Arquivo .md | Arquivo .md | Arquivo .md | Redis + arquivo |
| **Curva de aprendizado** | Baixa | Baixa | Mínima | Nenhuma |
| **Ideal para** | Scripts/bots | Apps web | Devs no terminal | Automações visuais |
| **Requer servidor** | Não | Não | Não | Sim (n8n) |

---

## Variáveis de Ambiente Necessárias (Python e Node.js)

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-api03-...

# Opcional — sobrescrever defaults
CG_MODEL=claude-sonnet-4-6
CG_EVACUATION_THRESHOLD=0.85
CG_MAX_TOKENS_RESPONSE=8192
```

```bash
# Instalar dependências
# Python:
pip install anthropic python-dotenv

# Node.js:
npm install @anthropic-ai/sdk dotenv
npx ts-node context-guardian-orchestrator.ts
```
