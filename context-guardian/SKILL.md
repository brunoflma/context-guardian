---
name: context-guardian
description: |
  Protege contexto de conversas longas com Modo Sentinela e Modo Evacuação.

  MODO SENTINELA — ativar com: "ativar context guardian", "context guardian on",
  "ativar sentinela", "iniciar monitoramento", "monitorar contexto",
  "proteção de contexto", "cg on", "/cg"
  Ao ativar: registra fatos-âncora, faz varredura a cada 20 turnos, evacua se detectar
  degradação.

  MODO EVACUAÇÃO — ativar IMEDIATAMENTE quando:
  - Claude está incerto sobre algo já estabelecido nesta conversa
  - Claude repetiu pergunta ou conteúdo já fornecido
  - Claude contradiz decisão anterior
  - Usuário diz: "você esqueceu", "já falei isso", "compile tudo", "gerar relatório",
    "nova conversa", "contexto perdido", "transferir conversa", "/evacuar"
  - Conversa passa de 50 turnos sem checkpoint
  - Qualquer variação de "o que discutimos", "resuma tudo", "checkpoint agora"

  Na evacuação: gerar arquivo .md + Prompt de Retomada via create_file + present_files.
  NUNCA apenas texto no chat.
---

# Context Guardian — Guia Completo

---

## Por Que Dois Modos São Necessários

**O Paradoxo da Detecção Tardia:** Uma skill só é consultada se Claude reconhece que precisa
dela. Mas quando o contexto já está degradado, Claude pode não ter capacidade suficiente
de reconhecer os próprios sinais de degradação. Resultado: a skill nunca é ativada exatamente
quando mais precisaria ser.

**A solução é bifásica:**
- **Modo Sentinela** resolve o paradoxo ativando monitoramento *antes* da degradação,
  quando Claude ainda tem contexto pleno para avaliar a situação com precisão.
- **Modo Evacuação** funciona como fallback — mesmo com contexto parcialmente degradado,
  os gatilhos na description são simples o suficiente para serem reconhecidos.

---

## MODO SENTINELA

### Ativação

O usuário deve ativar explicitamente no **início da conversa** com qualquer frase como:
- "ativar context guardian"
- "iniciar monitoramento de contexto"
- "modo sentinela ativo"
- "quero proteção de contexto nessa conversa"

### Resposta de Ativação (obrigatória)

Ao ativar, Claude deve responder com exatamente este bloco:

```
🛡️ **Context Guardian — Modo Sentinela ATIVO**

**Fatos-âncora registrados no momento da ativação:**
- Turno atual: [N]
- Tópico em andamento: [descrição]
- Objetivo declarado até aqui: [objetivo]
- Decisões já tomadas: [lista ou "nenhuma ainda"]

**Protocolo ativo:**
- ✅ Varredura silenciosa a cada 20 turnos
- ✅ Alerta automático ao detectar degradação
- ✅ Checkpoint obrigatório antes de tópicos complexos
- ✅ Evacuação automática se degradação confirmada

Próximo checkpoint automático: turno ~[N+20]
```

### Comportamento Durante o Modo Sentinela

A cada **20 turnos** a partir da ativação, Claude executa internamente:

**Checklist de varredura silenciosa:**
1. Consigo nomear o objetivo principal desta conversa sem hesitar?
2. Consigo listar as 3 últimas decisões tomadas?
3. Sei o nome/contexto do projeto/tarefa atual?
4. Há alguma contradição entre o que estou dizendo agora e algo dito antes?
5. Estou repetindo alguma pergunta ou sugestão já feita?

Se **qualquer item falhar** → executar Modo Evacuação imediatamente.
Se **todos passarem** → emitir checkpoint verde:

```
🟢 **Checkpoint Context Guardian** (turno ~[N])
Contexto verificado — sem degradação detectada.
Próximo checkpoint: turno ~[N+20]
```

### Checkpoint Manual

O usuário pode solicitar checkpoint a qualquer momento:
- "fazer checkpoint"
- "verificar contexto"
- "como está o contexto?"

---

## MODO EVACUAÇÃO

### Gatilhos de Ativação

**Automáticos (Claude detecta):**
- Incerteza sobre fato já estabelecido nesta conversa
- Repetição de pergunta ou conteúdo já coberto
- Contradição com decisão anterior
- 50+ turnos sem nenhum checkpoint registrado

**Por sinal do usuário:**
- Qualquer variação de: "você esqueceu", "já disse isso", "compile tudo", "nova conversa",
  "contexto perdido", "resuma o que fizemos", "quero transferir a conversa"

### Passo 1 — Anúncio Imediato

```
⚠️ **Context Guardian — Modo Evacuação**
Motivo: [descrição precisa do sinal detectado]

Gerando relatório completo de transferência como arquivo .md.
Não farei mais nada até o relatório estar salvo.
```

### Passo 2 — Varredura Exaustiva

Percorrer **toda a conversa, do turno 1 até o atual**, extraindo:

```
SEÇÃO A — Identidade
  - Nome do projeto / produto / sistema
  - Objetivo principal (exato, sem parafrasear)
  - Contexto do usuário (papel, empresa, domínio, se mencionado)
  - Data/contexto temporal se relevante

SEÇÃO B — Fatos Técnicos
  - Linguagens, versões exatas
  - Frameworks, bibliotecas, dependências
  - Infraestrutura, ambiente, plataforma
  - Endpoints, variáveis de ambiente (sem valores sensíveis)
  - Configurações estabelecidas

SEÇÃO C — Decisões (cronológicas)
  - [turno aproximado] O que foi decidido
  - Justificativa ou contexto da decisão
  - Alternativas rejeitadas e por quê

SEÇÃO D — Código e Artefatos
  - Arquivos criados, modificados, planejados
  - Snippets críticos (código que não pode ser perdido)
  - Estrutura de pastas estabelecida

SEÇÃO E — Problemas e Tentativas
  - Problema identificado
  - O que foi tentado e NÃO funcionou (com motivo)
  - Solução adotada ou estado atual

SEÇÃO F — Requisitos e Restrições
  - Requisitos funcionais (o que deve fazer)
  - Restrições técnicas (o que não pode usar/fazer)
  - Preferências do usuário (estilo, idioma, formato)
  - Prazo, orçamento ou outros constraints

SEÇÃO G — Estado Atual
  - O que estava sendo feito no momento da evacuação
  - Próximos passos definidos
  - Perguntas em aberto

SEÇÃO H — Referências
  - URLs, documentos, fontes citadas
  - Recursos externos mencionados
```

### Passo 3 — Gerar o Arquivo .md

**OBRIGATÓRIO:** Usar `create_file` para salvar em `/mnt/user-data/outputs/`.
**NUNCA** gerar apenas texto no chat — a capacidade de informação do chat é insuficiente.

Nome do arquivo: `context-guardian-[slug-do-projeto]-[timestamp-simplificado].md`
Exemplo: `context-guardian-sistema-atlas-turno-87.md`

Ver template completo em `references/transfer-report-template.md`.

Após criar o arquivo, usar `present_files` para entregá-lo ao usuário.

### Passo 4 — Gerar o Prompt de Retomada

Esta é a peça mais crítica da evacuação. O **Prompt de Retomada** é um bloco de texto
auto-suficiente que um novo agente Claude (sem nenhum histórico) consegue ler e entender
**exatamente onde a conversa foi suspensa** e o que fazer imediatamente.

Ele é diferente do relatório .md:
- O relatório .md é o **arquivo de referência completo** — toda a história, código, decisões
- O Prompt de Retomada é a **instrução de execução** — o que o novo agente faz agora

**Gerar o Prompt de Retomada com esta estrutura exata:**

```
════════════════════════════════════════════════════════════════
PROMPT DE RETOMADA — CONTEXT GUARDIAN
Copie todo este bloco e cole como PRIMEIRA mensagem na nova conversa.
════════════════════════════════════════════════════════════════

Você está assumindo uma conversa que foi transferida por limite de contexto.
Leia tudo abaixo antes de responder qualquer coisa.

## IDENTIDADE
Projeto: [nome exato]
Objetivo: [uma frase precisa — o que estamos construindo/resolvendo]
Eu sou: [papel/contexto do usuário se mencionado, ex: "desenvolvedor solo, back-end Python"]

## ESTADO NO MOMENTO DA SUSPENSÃO
Estávamos em: [descrição exata da atividade — ex: "implementando o endpoint POST /auth/login"]
Ponto exato de parada: [o que foi dito/escrito na última mensagem antes da evacuação]
Status: [ex: "código parcialmente escrito", "decisão tomada, implementação não iniciada"]

## DECISÕES JÁ TOMADAS — NÃO QUESTIONAR
[lista numerada de cada decisão com justificativa de 1 linha]
1. [decisão] — [por quê]
2. [decisão] — [por quê]
...

## RESTRIÇÕES ABSOLUTAS
[lista de tudo que foi proibido, descartado ou limitado]
- ❌ [o que não usar/fazer] — [motivo]
- ❌ [o que não usar/fazer] — [motivo]

## STACK E AMBIENTE
[lista compacta: linguagem+versão, framework, banco, infra]

## O QUE FOI FEITO ATÉ AQUI
[parágrafo denso descrevendo o arco completo da conversa anterior —
o que foi construído, os problemas resolvidos, as tentativas fracassadas]

## CÓDIGO EXISTENTE RELEVANTE
[incluir snippets críticos que o novo agente precisará ver imediatamente —
especialmente qualquer código incompleto que estava sendo escrito no momento da suspensão]

## PROBLEMAS EM ABERTO
[lista de qualquer coisa não resolvida, bug identificado, questão pendente]
- ❓ [problema/questão]

## PRIMEIRA AÇÃO DO NOVO AGENTE
[instrução imperativa, sem ambiguidade — ex:
"Continue escrevendo a função validate_token() a partir da linha 47.
A função deve verificar JWT com secret da env JWT_SECRET e retornar o user_id ou lançar
AuthError. O corpo da função estava sendo escrito quando a conversa foi suspensa."]

## ARQUIVO DE REFERÊNCIA COMPLETO
O relatório detalhado completo está no arquivo: [nome-do-arquivo.md]
Faça upload deste arquivo junto com este prompt para referência completa.
════════════════════════════════════════════════════════════════
```

**Regras para o Prompt de Retomada:**
- Deve funcionar **mesmo sem o arquivo .md** — ser completamente auto-suficiente
- O campo "Ponto exato de parada" deve ser tão preciso que o novo agente saiba
  exatamente qual era a última palavra/linha sendo trabalhada
- A "Primeira Ação" deve ser imperativa e sem margem para interpretação
- Incluir todo código incompleto ou parcial que estava sendo escrito — nunca truncar

### Passo 5 — Instruções ao Usuário

Após `present_files` e o Prompt de Retomada no chat, exibir:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ EVACUAÇÃO CONCLUÍDA

Foram gerados:
  📄 Arquivo .md — relatório completo (baixe pelo botão acima)
  📋 Prompt de Retomada — bloco acima, pronto para copiar

COMO CONTINUAR:

Opção A — Com upload (recomendado, mais completo):
  1. Baixe o arquivo .md
  2. Abra nova conversa no Claude
  3. Faça upload do .md + cole o Prompt de Retomada como primeira mensagem

Opção B — Só texto (funciona sem o arquivo):
  1. Abra nova conversa no Claude
  2. Cole apenas o Prompt de Retomada como primeira mensagem
  3. O novo agente terá contexto suficiente para continuar
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Garantias Arquitetônicas

### Por que o Modo Sentinela resolve o paradoxo

Quando ativado no início da conversa:
1. Claude registra fatos-âncora **enquanto ainda tem contexto pleno**
2. Os checkpoints acontecem a cada 20 turnos — bem antes da degradação crítica
3. A detecção é **proativa**, não depende de Claude reconhecer degradação no pico dela

### Por que o Modo Evacuação funciona mesmo com contexto degradado

A description da skill (sempre visível no system prompt) contém gatilhos **simples e binários**:
- "estou incerto sobre algo já estabelecido" — Claude sabe quando está inseguro
- "usuário disse X" — reconhecimento de padrão textual, não depende de memória

Claude não precisa de contexto rico para reconhecer que o usuário escreveu "você esqueceu".

### Limitação honesta

Se o contexto estiver **completamente destruído** (Claude não reconhece nem os gatilhos
da description), nenhuma skill pode resolver isso. A solução é o Modo Sentinela, que
previne chegar a esse ponto. Por isso a instrução ao usuário é clara:
**ative o Context Guardian na PRIMEIRA mensagem de conversas importantes.**

---

## Regras Absolutas do Relatório

- ❌ NUNCA omitir informação por parecer "pequena" ou "óbvia"
- ❌ NUNCA resumir decisões perdendo nuances
- ❌ NUNCA omitir tentativas fracassadas
- ❌ NUNCA gerar apenas no chat — sempre arquivo .md
- ✅ Completude tem prioridade máxima sobre brevidade
- ✅ Em dúvida se deve incluir: inclua
- ✅ Marcar 🔴 itens que um novo Claude deve saber IMEDIATAMENTE
- ✅ Incluir posição relativa na conversa ("após decisão de usar REST", "início da sessão")

Ver referências adicionais:
- `references/transfer-report-template.md` — template completo do arquivo .md
- `references/degradation-signals.md` — taxonomia detalhada de sinais

---

## Automação Total — Ambientes Suportados

No **Claude.ai** (interface web/mobile), o último passo da evacuação é sempre manual:
o usuário baixa o arquivo, abre nova conversa e cola o Prompt de Retomada.

Em outros ambientes, a transferência pode ser **completamente automática**:

| Ambiente | Nível de Automação | Como |
|---|---|---|
| **Claude.ai** | Semi-automático | Skill gera tudo pronto; usuário executa 3 passos |
| **Claude Code** | ✅ Total | Subagentes nativos; transferência sem intervenção |
| **API direta** | ✅ Total | Orquestrador monitora tokens e transfere automaticamente |
| **n8n / Make** | ✅ Total | Nó de decisão baseado em `usage.input_tokens` |

Para implementação completa (Python, Node.js, Claude Code e n8n),
consultar `references/automation-orchestrator.md`.
