---
name: context-guardian
description: |
  Protege contexto com 3 modos: Sentinela, Silencioso e Evacuação.

  SENTINELA — ativar com: "ativar context guardian", "context guardian on",
  "ativar sentinela", "iniciar monitoramento", "cg on", "/cg"
  Registra fatos-âncora, detecta viradas de fase, evacua ao detectar degradação.

  SILENCIOSO — ativar com: "modo silencioso", "cg silent"
  Checkpoints internos sem mensagem — Claude só fala ao detectar problema.

  EVACUAÇÃO — ativar IMEDIATAMENTE quando:
  - Claude está incerto sobre algo já estabelecido nesta conversa
  - Claude repetiu pergunta ou conteúdo já fornecido
  - Claude contradiz decisão anterior
  - Usuário diz: "você esqueceu", "já falei", "compile tudo", "gerar relatório",
    "nova conversa", "contexto perdido", "transferir conversa", "/evacuar"
  - Conversa passa de 50 turnos sem checkpoint
  - Qualquer variação de "o que discutimos", "resuma tudo", "checkpoint agora"

  Evacuação: gerar .md + Prompts de Retomada via create_file + present_files.
  NUNCA apenas texto no chat.
---

# Context Guardian v1.1 — Guia Completo

---

## Arquitetura Geral

O Context Guardian opera em três modos e aplica seis mecanismos de proteção:

```
MODOS                    MECANISMOS
─────────────────────    ──────────────────────────────────────
🛡️  Sentinela (ativo)    1. Checkpoint por fase (não só turnos)
🔇  Silencioso (ativo)   2. Detecção semântica de degradação
⚠️  Evacuação (disparo)  3. Prompt de Retomada compacto + completo
                         4. Perfis de conversa especializados
                         5. Modo silencioso sem ruído no chat
                         6. Integração com memória do Claude
```

---

## MODO SENTINELA

### Ativação

Frases aceitas no início da conversa:
- `ativar context guardian` · `context guardian on` · `/cg` · `cg on`
- `ativar sentinela` · `iniciar monitoramento` · `monitorar contexto` · `proteção de contexto`

### Resposta de Ativação (obrigatória)

```
🛡️ **Context Guardian v1.1 — Modo Sentinela ATIVO**

**Fatos-âncora registrados:**
- Turno atual: [N]
- Tópico: [descrição]
- Objetivo: [objetivo declarado]
- Decisões tomadas: [lista ou "nenhuma ainda"]
- Perfil detectado: [Técnico / Estratégico / Criativo / Geral]

**Protocolo:**
- ✅ Checkpoint por virada de fase + a cada 20 turnos
- ✅ Detecção semântica de degradação gradual
- ✅ Evacuação automática com relatório .md + Prompts de Retomada
- ✅ Preferências recorrentes salvas na memória do Claude

Próximo checkpoint: virada de fase ou turno ~[N+20]
```

---

## MODO SILENCIOSO

### Ativação

- `modo silencioso` · `sentinela silencioso` · `cg silent`

Pode ser ativado junto com o Sentinela ou a qualquer momento durante a conversa.

### Comportamento

- Checkpoints acontecem internamente **sem nenhuma mensagem no chat**
- Claude só fala em dois casos:
  1. Detectou degradação → executa evacuação imediatamente
  2. Usuário pede checkpoint manual explicitamente

### Desativar

- `modo normal` · `cg verbose` · `desativar silencioso`

---

## MECANISMO 1 — Checkpoint por Fase

### Eventos que disparam checkpoint de fase

Claude deve reconhecer e fazer checkpoint quando detectar:

| Evento | Exemplo |
|--------|---------|
| Conclusão de módulo/feature | "Perfeito, o módulo de auth está pronto" |
| Decisão arquitetural grande | Escolha de banco, framework, padrão de design |
| Mudança de assunto significativa | Saindo de implementação para deploy |
| Início de área de risco | Refatoração, migração, mudança de stack |
| Usuário expressa satisfação com fase | "Ótimo, agora vamos para a parte X" |
| Acúmulo de 8+ decisões sem checkpoint | Independente de turnos |

### Checkpoint de fase — comportamento

**Modo normal:**
```
🟢 **Checkpoint Context Guardian** — fase concluída: [nome da fase]
Contexto íntegro. Próximo: próxima virada de fase ou turno ~[N+20]
```

**Modo silencioso:** registrar internamente, sem mensagem.

**Checklist interna (executar em todo checkpoint):**
```
□ Sei o objetivo principal sem hesitar?
□ Consigo listar as 3 decisões mais recentes?
□ Sei exatamente o que estava sendo feito antes deste turno?
□ Minhas respostas mantêm o nível de especificidade das anteriores?
□ Estou usando as convenções estabelecidas no início?
□ Há contradição entre o que vou dizer e algo dito antes?
□ Estou prestes a perguntar algo que já foi respondido?
```

0 falhas → checkpoint verde / silencioso.
1+ falha → evacuação imediata.

---

## MECANISMO 2 — Detecção Semântica de Degradação

Além dos sinais binários, Claude deve detectar sinais **graduais**
que precedem a degradação total. Ver taxonomia em `references/degradation-signals.md`.

### Sinais de alerta precoce

**Genericidade crescente:** respostas específicas ao projeto ficam genéricas.
Ex: sugere "você pode usar X ou Y" quando X foi escolhido há 10 turnos.
→ Ação: checkpoint imediato.

**Perda de convenções:** Claude para de usar nomes, padrões ou estilos
estabelecidos sem motivo aparente.
→ Ação: checkpoint imediato.

**Qualidade regressiva:** código gerado fica mais simples que o padrão
estabelecido, sem justificativa.
→ Ação: checkpoint imediato.

**Disclaimer excessivo:** Claude adiciona ressalvas sobre coisas já decididas.
→ Ação: registrar; se ocorrer 2x seguidas → evacuação.

---

## MECANISMO 3 — Prompt de Retomada em Dois Formatos

### Formato Completo (padrão para evacuações automáticas)

Estrutura detalhada com todas as seções — ver Passo 4 do Modo Evacuação abaixo.

### Formato Compacto (~150 palavras, para retomadas rápidas)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETOMADA RÁPIDA — [NOME DO PROJETO]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Projeto: [nome] | Objetivo: [1 frase]
Stack: [lista compacta]
Fase atual: [onde estamos]

Decisões fixas:
1. [decisão] — [motivo]
2. [decisão] — [motivo]

Restrições: [lista compacta]

Parado em: [ponto exato — 1 frase cirúrgica]

Próxima ação: [instrução imperativa — 1 frase]

Ref. completa: [nome-do-arquivo.md]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Quando usar cada formato:**

| Situação | Formato |
|---|---|
| Conversa técnica com código e muitas decisões | Completo |
| Planejamento, brainstorm, estratégia | Compacto |
| Retomada rápida com poucas pendências | Compacto |
| Evacuação automática por degradação | Completo (sempre) |

---

## MECANISMO 4 — Perfis de Conversa

Claude detecta o perfil automaticamente na ativação.
Forçar manualmente: `"perfil técnico"` · `"perfil estratégico"` · `"perfil criativo"`

### Perfil Técnico / Código
Quando: há linguagem, framework, banco, API, código.
Prioriza: Stack, Código e Artefatos, Decisões arquiteturais, Snippets completos.

### Perfil Estratégico / Planejamento
Quando: foco em negócio, roadmap, priorização, OKRs.
Prioriza: Decisões cronológicas, Alternativas rejeitadas, Próximos passos.
Reduz: Stack técnica (omitir se irrelevante).

### Perfil Criativo
Quando: escrita, design, conteúdo, narrativa, roteiro.
Prioriza: Diretrizes criativas, Tom e voz, Restrições de estilo, Estado da obra.
Reduz: Stack técnica, Requisitos funcionais.

### Perfil Geral
Fallback. Usa o template completo sem otimizações.

Ver templates por perfil em `references/transfer-report-template.md`.

---

## MECANISMO 5 — Modo Silencioso

Documentado acima na seção MODO SILENCIOSO.
Ativar quando o usuário não quer interrupções no fluxo de trabalho.

---

## MECANISMO 6 — Integração com Memória do Claude

Durante a evacuação, Claude identifica e salva nas **memórias persistentes**
preferências recorrentes do usuário úteis em futuras conversas.

### O que salvar na memória

**Sempre que detectado:**
- Stack tecnológica preferida
- Linguagem de programação principal
- Estilo de código (comentado, funcional, sem classes, etc.)
- Idioma preferido para código e comentários
- Formato de resposta preferido (conciso, detalhado, com exemplos)
- Restrições recorrentes ("nunca usa X", "sempre prefere Y")
- Papel/contexto profissional ("dev solo", "CTO de startup")

**Nunca salvar:**
- Decisões específicas de um projeto (ficam só no relatório)
- Dados sensíveis (credenciais, informações pessoais)

### Como salvar

Usar `memory_user_edits` com `command: "add"` para cada preferência,
formulada de forma compacta:

```
"Usuário prefere Python com type hints e sem frameworks pesados"
"Usuário escreve código em inglês mas conversa em PT-BR"
"Usuário é dev solo, contexto fintech B2B"
"Usuário prefere respostas concisas sem markdown excessivo"
```

### Informar o usuário após salvar

```
🧠 **Preferências salvas na memória do Claude:**
- [preferência 1]
- [preferência 2]
Estarão disponíveis automaticamente em futuras conversas.
```

---

## MODO EVACUAÇÃO

### Gatilhos

**Automáticos:** falha na checklist · sinal semântico recorrente · 50+ turnos sem checkpoint

**Por sinal do usuário:**
`você esqueceu` · `já falei isso` · `compile tudo` · `gerar relatório` · `nova conversa`
`contexto perdido` · `transferir conversa` · `/evacuar` · `o que discutimos` · `resuma tudo`

### Passo 1 — Anúncio

```
⚠️ **Context Guardian — Modo Evacuação**
Motivo: [sinal detectado]  |  Perfil: [Técnico / Estratégico / Criativo / Geral]

Gerando relatório + Prompts de Retomada. Não farei mais nada até concluir.
```

### Passo 2 — Varredura Exaustiva (turno 1 → atual)

Extrair por perfil:
- **A** Identidade: nome, objetivo exato, contexto do usuário, perfil
- **B** Fatos Técnicos *(Técnico/Geral)*: linguagens, frameworks, infra, configs
- **C** Decisões Cronológicas: [turno] decisão — justificativa — alternativas rejeitadas
- **D** Código e Artefatos *(Técnico)*: estrutura de pastas, snippets completos, código incompleto
- **E** Diretrizes Criativas *(Criativo)*: tom, voz, restrições, estado da obra
- **F** Problemas e Tentativas: problema → falhas (com motivo) → solução adotada
- **G** Requisitos e Restrições: funcionais, técnicos, preferências, constraints
- **H** Estado Atual: o que estava sendo feito, ponto exato de parada, próximos passos
- **I** Referências: URLs, documentos, fontes

### Passo 3 — Gerar Arquivo .md

`create_file` → `/mnt/user-data/outputs/context-guardian-[slug]-turno-[N].md`
Template por perfil em `references/transfer-report-template.md`.
Após criar: `present_files`.

### Passo 4 — Gerar Prompts de Retomada no Chat

**Prompt Completo** — estrutura:

```
════════════════════════════════════════════════════════════════
PROMPT DE RETOMADA COMPLETO — CONTEXT GUARDIAN
════════════════════════════════════════════════════════════════
Você está assumindo uma conversa transferida por limite de contexto.
Leia tudo antes de responder.

## IDENTIDADE
Projeto: [nome] | Objetivo: [1 frase] | Perfil: [tipo]
Eu sou: [papel/contexto do usuário]

## ESTADO NO MOMENTO DA SUSPENSÃO
Estávamos em: [atividade exata]
Ponto de parada: [última coisa dita/escrita]
Status: [parcialmente escrito / decisão tomada sem implementação / etc.]

## DECISÕES TOMADAS — NÃO QUESTIONAR
1. [decisão] — [por quê]
2. [decisão] — [por quê]

## RESTRIÇÕES ABSOLUTAS
- ❌ [o que não usar/fazer] — [motivo]

## STACK E AMBIENTE
[linguagem+versão · framework · banco · infra]

## HISTÓRICO
[parágrafo denso: o que foi construído, problemas resolvidos, tentativas fracassadas]

## CÓDIGO RELEVANTE
[snippets críticos — especialmente código incompleto no momento da suspensão]

## PENDÊNCIAS
- ❓ [problema/questão em aberto]

## PRIMEIRA AÇÃO
[instrução imperativa sem ambiguidade]

## REFERÊNCIA COMPLETA
Arquivo: [nome-do-arquivo.md] — faça upload junto com este prompt.
════════════════════════════════════════════════════════════════
```

**Prompt Compacto** — formato descrito no Mecanismo 3.

### Passo 5 — Salvar Preferências na Memória

Executar Mecanismo 6.

### Passo 6 — Instruções ao Usuário

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ EVACUAÇÃO CONCLUÍDA

  📄 Arquivo .md — relatório completo (baixe acima)
  📋 Prompt Completo — para conversas técnicas e longas
  📋 Prompt Compacto — para retomadas rápidas
  🧠 Preferências salvas na memória do Claude

COMO CONTINUAR:

Opção A — Upload + Prompt Completo:
  1. Baixe o .md  2. Nova conversa  3. Upload + cole o Prompt Completo

Opção B — Retomada rápida:
  1. Nova conversa  2. Cole o Prompt Compacto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Regras Absolutas

- ❌ NUNCA omitir informação por parecer pequena ou óbvia
- ❌ NUNCA truncar código parcial
- ❌ NUNCA gerar apenas no chat — sempre arquivo .md
- ✅ Completude > brevidade no relatório .md
- ✅ Marcar 🔴 itens que o novo Claude deve saber imediatamente
- ✅ Perfil prioriza seções — nunca omite completamente
- ✅ Salvar na memória apenas preferências recorrentes

---

## Automação Total — Ambientes Externos

| Ambiente | Automação |
|---|---|
| **Claude.ai** | Semi-automático — 3 passos manuais |
| **Claude Code** | ✅ Total — subagentes nativos |
| **API Python/Node** | ✅ Total — orquestrador monitora tokens |
| **n8n** | ✅ Total — fluxo visual sem código |

Implementações completas em `references/automation-orchestrator.md`.
