---
name: context-guardian
description: |
  Protege contexto com 3 modos: Sentinela, Silencioso e Evacuação.

  SENTINELA — ativar com: "ativar context guardian", "cg on", "/cg",
  "ativar sentinela", "iniciar monitoramento", "proteção de contexto"
  Na ativação: perguntar intervalo de checkpoint, registrar fatos-âncora,
  emitir lembrete a cada N turnos. Checkpoint manual é a camada primária.

  SILENCIOSO — ativar com: "modo silencioso", "cg silent"
  Suprime lembretes — Claude fala só ao detectar degradação ou a pedido.

  EVACUAÇÃO — ativar IMEDIATAMENTE quando:
  - Claude incerto sobre algo já estabelecido nesta conversa
  - Claude repetiu pergunta ou conteúdo já fornecido
  - Claude contradiz decisão anterior
  - Usuário diz: "você esqueceu", "já falei", "compile tudo", "gerar relatório",
    "nova conversa", "contexto perdido", "transferir conversa", "/evacuar"
  - 50 turnos sem checkpoint confirmado
  - "o que discutimos", "resuma tudo", "checkpoint agora"

  Evacuação: gerar .md + Prompts de Retomada via create_file + present_files.
  NUNCA apenas texto no chat.
---

# Context Guardian v1.3 — Guia Completo

---

## Limitações Honestas (ler antes de tudo)

Esta seção existe para que o usuário saiba exatamente o que a skill consegue
e o que não consegue — sem promessas que a arquitetura não cumpre.

### O que NÃO é possível no Claude.ai

**Monitoramento contínuo em background:** Claude não executa processos paralelos.
Ele processa uma mensagem e responde. Não há "loop" rodando entre as respostas.
A skill é lida na ativação — não é re-executada automaticamente a cada turno.

**Detecção de viradas de fase:** depende de Claude reconhecer ativamente o evento
enquanto está respondendo. Em conversas densas e técnicas, isso falha com frequência
porque o foco cognitivo está na tarefa, não no monitoramento.

**Evacuação pré-compactação:** Claude não tem acesso ao contador de tokens no Claude.ai.
Não é possível saber proativamente que a compactação está se aproximando.

### O que É garantido

**Evacuação por gatilho textual:** quando o usuário escreve um dos comandos de
evacuação, ou quando Claude percebe claramente que repetiu/contradiz algo, a evacuação
acontece de forma confiável — esses são gatilhos binários e simples.

**Checkpoint por lembrete:** Claude emite lembretes de checkpoint em intervalos
definidos na ativação. Isso funciona porque não requer detecção — é uma contagem
explícita de turnos respondidos.

**Relatório completo na evacuação:** uma vez disparada, a evacuação gera o arquivo
.md e os Prompts de Retomada de forma confiável.

### Consequência para o design

**Checkpoints manuais periódicos são a camada primária de proteção.**
A detecção automática de fase é secundária e não deve ser confiada isoladamente.
O usuário que define um intervalo de checkpoint na ativação tem proteção real.
O usuário que confia só na detecção automática pode ter falhas como as documentadas.

---

## MODO SENTINELA

### Ativação

Frases aceitas:
`ativar context guardian` · `context guardian on` · `/cg` · `cg on`
`ativar sentinela` · `iniciar monitoramento` · `monitorar contexto` · `proteção de contexto`

### Pergunta obrigatória na ativação

Ao ativar, Claude deve SEMPRE perguntar antes de confirmar:

```
🛡️ **Context Guardian v1.3 — Ativando Sentinela**

A cada quantos turnos você quer receber o lembrete de checkpoint?
Recomendado: 10 turnos para conversas técnicas densas, 15 para conversas mais leves.
(Responda com um número, ex: "10")
```

### Resposta de confirmação (após o usuário definir o intervalo)

```
🛡️ **Context Guardian v1.3 — Modo Sentinela ATIVO**

**Fatos-âncora registrados:**
- Turno atual: [N]
- Tópico: [descrição]
- Objetivo: [objetivo declarado]
- Decisões tomadas: [lista ou "nenhuma ainda"]
- Perfil detectado: [Técnico / Estratégico / Criativo / Geral]

**Protocolo ativo:**
- ✅ Lembrete de checkpoint a cada [N] turnos (camada primária)
- ✅ Evacuação por gatilho textual (confiável)
- ✅ Evacuação ao detectar repetição ou contradição clara
- ⚠️  Detecção automática de fase: melhor esforço, não garantida
- ⚠️  Pré-compactação: não detectável — use o intervalo de checkpoint como proteção

Próximo checkpoint: turno ~[N + intervalo definido]

Dica: se a conversa for crítica, use "checkpoint agora" a qualquer momento.
```

### Lembrete de Checkpoint (emitir a cada N turnos respondidos)

Claude deve contar os turnos respondidos desde a ativação (ou desde o último
checkpoint confirmado) e emitir ao atingir o intervalo:

```
⏰ **Checkpoint Context Guardian** — turno ~[N]

É um bom momento para verificar o contexto.
Digite "ok" para confirmar que está tudo bem, ou "evacuar" para gerar o relatório.
```

Aguardar resposta do usuário:
- `"ok"` / `"tudo bem"` / qualquer confirmação → registrar checkpoint, reiniciar contagem
- `"evacuar"` / qualquer gatilho de evacuação → executar Modo Evacuação
- Usuário ignora e continua → registrar como não confirmado, emitir próximo lembrete
  normalmente (não bloquear o fluxo)

### Checkpoint Manual

O usuário pode solicitar a qualquer momento:
`"fazer checkpoint"` · `"verificar contexto"` · `"checkpoint agora"` · `"status"`

Resposta do checkpoint manual:

```
🟢 **Checkpoint Context Guardian** (turno ~[N])

**Estado atual:**
- Objetivo: [confirmar se ainda é o mesmo]
- Fase: [em que fase estamos]
- Últimas decisões: [listar as 3 mais recentes]
- Pendências: [o que está em aberto]

Contexto íntegro? Se sim, diga "ok". Se algo estiver errado, descreva.
```

### Detecção Automática de Fase (melhor esforço)

Claude deve tentar reconhecer os eventos abaixo e fazer checkpoint quando detectar.
**Esta detecção não é garantida em conversas densas — é complementar, não primária.**

| Evento | Como reconhecer |
|--------|----------------|
| Conclusão explícita de módulo | Usuário diz "perfeito", "feito", "próxima parte" |
| Decisão arquitetural grande | Escolha definitiva de tecnologia, padrão ou abordagem |
| Mudança clara de assunto | Tópico muda sem relação com o anterior |
| Acúmulo de 8+ decisões | Contar decisões desde último checkpoint |

Quando detectar: executar checklist interna e emitir checkpoint ou evacuação.

### Checklist Interna (executar em todo checkpoint)

```
□ Sei o objetivo principal sem hesitar?
□ Consigo listar as 3 decisões mais recentes com suas justificativas?
□ Sei exatamente o que estava sendo feito antes deste turno?
□ Minhas respostas mantêm o nível de especificidade das anteriores?
□ Estou usando as convenções estabelecidas (nomes, estilo, padrões)?
□ Vou contradizer algo dito antes?
□ Vou perguntar algo que já foi respondido?
```

0 falhas → checkpoint verde, continuar.
1+ falha → evacuação imediata.

---

## MODO SILENCIOSO

### Ativação

`modo silencioso` · `cg silent` · `sentinela silencioso`

Pode ser ativado junto com o Sentinela ou durante a conversa.

### Comportamento

- Lembretes de checkpoint são **suprimidos**
- Claude só fala em dois casos:
  1. Detectou degradação clara → evacuação imediata
  2. Usuário solicita checkpoint manualmente

**Atenção ao usuário:** no modo silencioso, a responsabilidade de solicitar
checkpoints periódicos recai sobre você. Recomendado apenas para conversas
onde interrupções seriam muito prejudiciais.

### Desativar

`modo normal` · `cg verbose` · `desativar silencioso`

---

## MODO EVACUAÇÃO

### Gatilhos confiáveis (funcionam mesmo com contexto degradado)

**Por sinal do usuário (binários — alta confiabilidade):**
`você esqueceu` · `já falei isso` · `compile tudo` · `gerar relatório`
`nova conversa` · `contexto perdido` · `transferir conversa` · `/evacuar`
`o que discutimos` · `resuma tudo` · `checkpoint agora`

**Por detecção interna (quando Claude percebe claramente):**
- Está incerto sobre fato já estabelecido nesta conversa
- Repetiu pergunta ou conteúdo já fornecido
- Contradiz decisão anterior documentada

**Por contagem:**
- 50+ turnos sem checkpoint confirmado pelo usuário

### Passo 1 — Anúncio Imediato

```
⚠️ **Context Guardian — Modo Evacuação**
Motivo: [descrição precisa do gatilho]
Perfil: [Técnico / Estratégico / Criativo / Geral]

Gerando relatório .md + Prompts de Retomada.
Não farei mais nada até concluir.
```

### Passo 2 — Varredura Exaustiva (turno 1 → atual)

Percorrer toda a conversa extraindo por perfil:

- **A — Identidade:** nome do projeto, objetivo exato, contexto do usuário, perfil
- **B — Fatos Técnicos** *(Técnico/Geral):* linguagens+versões, frameworks, infra, configs,
  variáveis de ambiente (estrutura, sem valores sensíveis)
- **C — Decisões Cronológicas:** [turno aprox.] decisão — justificativa — alternativas rejeitadas
- **D — Código e Artefatos** *(Técnico):* estrutura de pastas, snippets completos,
  código incompleto (NUNCA truncar — incluir exatamente onde parou)
- **E — Diretrizes Criativas** *(Criativo):* tom, voz, restrições de estilo, estado da obra
- **F — Problemas e Tentativas:** problema → o que falhou e por quê → solução adotada
- **G — Requisitos e Restrições:** funcionais, técnicos, preferências do usuário, constraints
- **H — Estado Atual:** o que estava sendo feito, ponto exato de parada, próximos passos
- **I — Referências:** URLs, documentos, fontes citadas

### Passo 3 — Gerar Arquivo .md

**OBRIGATÓRIO:** `create_file` → `/mnt/user-data/outputs/context-guardian-[slug]-turno-[N].md`

Template por perfil em `references/transfer-report-template.md`.

Após criar: `present_files`.

### Passo 4 — Gerar Prompts de Retomada no Chat

Gerar os dois formatos em sequência.

**Prompt Completo:**

```
════════════════════════════════════════════════════════════════
PROMPT DE RETOMADA COMPLETO — CONTEXT GUARDIAN v1.3
════════════════════════════════════════════════════════════════
Você está assumindo uma conversa transferida. Leia tudo antes de responder.

## IDENTIDADE
Projeto: [nome] | Objetivo: [1 frase] | Perfil: [tipo]
Usuário: [papel/contexto]

## ESTADO NO MOMENTO DA SUSPENSÃO
Estávamos em: [atividade exata]
Ponto de parada: [última coisa dita/escrita — cirúrgico]
Status: [ex: código 60% escrito / decisão tomada sem implementação]

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
[instrução imperativa sem ambiguidade — o que fazer agora]

## REFERÊNCIA COMPLETA
Arquivo: [nome-do-arquivo.md]
Faça upload junto com este prompt para contexto completo.
════════════════════════════════════════════════════════════════
```

**Prompt Compacto (~150 palavras):**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETOMADA RÁPIDA — [NOME DO PROJETO]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Projeto: [nome] | Objetivo: [1 frase]
Stack: [lista compacta]
Fase: [onde estamos]

Decisões fixas:
1. [decisão] — [motivo]
2. [decisão] — [motivo]

Restrições: [lista compacta]

Parado em: [ponto exato — 1 frase]

Próxima ação: [instrução imperativa — 1 frase]

Ref: [nome-do-arquivo.md]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Passo 5 — Salvar Preferências na Memória

Identificar e salvar via `memory_user_edits` preferências **recorrentes** do usuário:
stack preferida, linguagem principal, estilo de código, idioma, formato de resposta,
contexto profissional. Nunca salvar dados de projeto específico ou dados sensíveis.

Informar o que foi salvo:
```
🧠 **Preferências salvas na memória do Claude:**
- [preferência 1]
- [preferência 2]
Disponíveis automaticamente em futuras conversas.
```

### Passo 6 — Instruções ao Usuário

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ EVACUAÇÃO CONCLUÍDA

  📄 Arquivo .md — relatório completo (baixe acima)
  📋 Prompt Completo — conversas técnicas e longas
  📋 Prompt Compacto — retomadas rápidas
  🧠 Preferências salvas na memória

COMO CONTINUAR:

Opção A — Upload + Prompt Completo:
  1. Baixe o .md
  2. Nova conversa no Claude
  3. Upload do .md + cole o Prompt Completo

Opção B — Retomada rápida:
  1. Nova conversa no Claude
  2. Cole o Prompt Compacto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Perfis de Conversa

Claude detecta automaticamente na ativação.
Forçar: `"perfil técnico"` · `"perfil estratégico"` · `"perfil criativo"`

| Perfil | Quando | Prioriza | Reduz |
|--------|--------|----------|-------|
| **Técnico** | Linguagem, framework, código | Stack, artefatos, snippets | — |
| **Estratégico** | Negócio, roadmap, OKRs | Decisões, alternativas rejeitadas | Stack técnica |
| **Criativo** | Escrita, design, narrativa | Tom, voz, restrições de estilo | Stack, requisitos |
| **Geral** | Fallback | Template completo | — |

Templates completos por perfil em `references/transfer-report-template.md`.

---

## Regras Absolutas

- ❌ NUNCA omitir informação por parecer pequena ou óbvia
- ❌ NUNCA truncar código parcial — incluir exatamente onde parou
- ❌ NUNCA gerar apenas no chat — sempre arquivo .md
- ❌ NUNCA prometer detecção automática de fase como garantia
- ✅ Completude > brevidade no relatório .md
- ✅ Marcar 🔴 itens críticos para o novo Claude
- ✅ Checkpoints manuais periódicos são a camada primária — comunicar isso ao usuário
- ✅ Salvar na memória apenas preferências recorrentes

---

## Automação Total — Ambientes Externos

No Claude.ai, o último passo é sempre manual. Em outros ambientes:

| Ambiente | Automação | Nota |
|---|---|---|
| **Claude.ai** | Semi-automático | Limitação de plataforma — sem acesso a tokens |
| **Claude Code** | ✅ Total | Subagentes nativos |
| **API Python/Node** | ✅ Total | Acesso a `usage.input_tokens` — evacuação real pré-compactação |
| **n8n** | ✅ Total | Fluxo visual sem código |

Implementações em `references/automation-orchestrator.md`.
