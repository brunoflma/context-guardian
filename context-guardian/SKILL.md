---
name: context-guardian
compatibility: claude.ai, claude-code
description: |
  Protege contexto com 3 modos: Sentinela, Silencioso e Evacuação.

  SENTINELA — ativar: "ativar context guardian", "ativar sentinela", "cg on", "/cg"
  Registra fatos-âncora, detecta viradas de fase, evacua ao detectar degradação.

  SILENCIOSO — ativar: "modo silencioso", "cg silent"
  Checkpoints internos sem mensagem — Claude só fala ao detectar problema.

  EVACUAÇÃO — ativar IMEDIATAMENTE quando:
  - Claude incerto sobre algo estabelecido, repetiu conteúdo ou contradiz decisão anterior
  - Usuário diz: "você esqueceu", "já falei", "compile tudo", "gerar relatório",
    "nova conversa", "contexto perdido", "transferir conversa", "/evacuar"
  - Conversa passa de 50 turnos sem checkpoint
  - Variação de "o que discutimos", "resuma tudo", "checkpoint agora"

  Evacuação: gerar .md + Prompts de Retomada via create_file + present_files.
  NUNCA apenas texto no chat.

  PERFIS: Técnico · Jurídico · Estratégico · Criativo · Médico · Educacional · Investigativo · Geral
---

# Context Guardian v1.2.1 — Guia Completo

---

## Arquitetura Geral

O Context Guardian opera em três modos e aplica seis mecanismos de proteção:

```
MODOS                    MECANISMOS
─────────────────────    ──────────────────────────────────────
🛡️  Sentinela (ativo)    1. Checkpoint por fase (não só turnos)
🔇  Silencioso (ativo)   2. Detecção semântica de degradação
⚠️  Evacuação (disparo)  3. Prompt de Retomada compacto + completo
                         4. Perfis de conversa especializados (8 perfis)
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
🛡️ **Context Guardian v1.2.1 — Modo Sentinela ATIVO**

**Fatos-âncora registrados:**
- Turno atual: [N]
- Tópico: [descrição]
- Objetivo: [objetivo declarado]
- Decisões tomadas: [lista ou "nenhuma ainda"]
- Perfil detectado: [Técnico / Jurídico / Estratégico / Criativo / Médico-Científico / Educacional / Investigativo / Geral]

**Protocolo:**
- ✅ Checkpoint por virada de fase + a cada 20 turnos
- ✅ Detecção semântica de degradação gradual
- ✅ Evacuação automática com relatório .md + Prompts de Retomada
- ✅ Preferências recorrentes salvas na memória do Claude

Próximo checkpoint: virada de fase ou turno ~[N+20]
```

### ⚠️ Limitação de plataforma

A Habilidade é injetada apenas em conversas novas. Em conversas em andamento, o Claude não a reconhece automaticamente. Workaround: cole o conteúdo deste SKILL.md no chat e peça ativação manual.

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
| Conclusão de peça jurídica | "A petição está pronta, agora vamos à contestação" |
| Definição de tese ou estratégia | Tese defensiva, fundamento legal escolhido |
| Mudança de assunto significativa | Saindo de implementação para deploy |
| Início de área de risco | Refatoração, prazo processual crítico, procedimento invasivo |
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
□ [Jurídico] Estou ciente de todos os prazos processuais críticos?
□ [Médico] Estou respeitando o protocolo e as contraindicações definidas?
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

**Qualidade regressiva:** conteúdo gerado fica mais simples que o padrão
estabelecido, sem justificativa.
→ Ação: checkpoint imediato.

**Disclaimer excessivo:** Claude adiciona ressalvas sobre coisas já decididas.
→ Ação: registrar; se ocorrer 2x seguidas → evacuação.

**[Jurídico] Perda de referências processuais:** Claude deixa de mencionar número
de processo, partes ou teses já fixadas ao elaborar peças.
→ Ação: evacuação imediata.

**[Jurídico] Confusão entre processos:** Claude mistura fatos, partes ou pedidos
de processos distintos discutidos na mesma conversa.
→ Ação: evacuação imediata.

---

## MECANISMO 3 — Prompt de Retomada em Dois Formatos

### Formato Completo (padrão para evacuações automáticas)

Estrutura detalhada com todas as seções — ver Passo 4 do Modo Evacuação abaixo.

### Formato Compacto (~150 palavras, para retomadas rápidas)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETOMADA RÁPIDA — [NOME DO PROJETO/CASO]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Projeto: [nome] | Objetivo: [1 frase]
Perfil: [tipo] | Contexto: [área/domínio]
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
| Conversa jurídica com peças, prazos e teses | Completo (sempre) |
| Planejamento, brainstorm, estratégia | Compacto |
| Retomada rápida com poucas pendências | Compacto |
| Evacuação automática por degradação | Completo (sempre) |

---

## MECANISMO 4 — Perfis de Conversa

Claude detecta o perfil automaticamente na ativação.
Forçar manualmente: `"perfil jurídico"` · `"perfil técnico"` · `"perfil estratégico"` · `"perfil criativo"` · `"perfil médico"` · `"perfil educacional"` · `"perfil investigativo"`

---

### Perfil Técnico / Código
**Quando:** há linguagem, framework, banco, API, código, arquitetura de software.
**Prioriza:** Stack, Código e Artefatos, Decisões arquiteturais, Snippets completos, Estrutura de pastas.
**Alerta especial:** código parcial ou incompleto no momento da evacuação — nunca truncar.

---

### Perfil Jurídico
**Quando:** menção a processo, petição, vara, tribunal, réu, autor, prazo processual, legislação, jurisprudência, inventário, contrato, defesa, recurso, habilitação de crédito, execução, liminar, tutela.
**Prioriza:**
- Identificação completa do processo (número, vara, tribunal, instância, fase)
- Partes envolvidas (autor, réu, terceiros, intervenientes, espólio, herdeiros)
- Teses jurídicas fixadas e fundamentos legais (artigos, leis, súmulas, jurisprudência citada)
- Peças já elaboradas e seu status (rascunho, finalizada, protocolada)
- Prazos processuais — **SEMPRE marcados em 🔴 vermelho, independente do modo**
- Provas e documentos mapeados (o que existe, o que falta, o que foi juntado)
- Estratégia processual definida (defensiva, ofensiva, negocial)
- Decisões do juízo e recursos cabíveis
- Pedidos formulados e seu status

**Alerta especial — prazos:**
Qualquer prazo processual identificado deve ser extraído e destacado em 🔴 no relatório, mesmo em modo silencioso. Perda de prazo é irreparável.

**Alerta especial — confusão de processos:**
Se a conversa envolver múltiplos processos, Claude deve manter um mapa de processos ativo e verificar, a cada resposta, se está referenciando o processo correto.

**Gatilhos de evacuação adicionais:**
- Claude menciona número de processo errado
- Claude confunde partes entre processos distintos
- Claude sugere fundamento legal já descartado
- Claude elabora peça sem mencionar o processo ao qual ela pertence

**Reduz:** jargão técnico de TI, stack tecnológica (omitir se irrelevante).

---

### Perfil Estratégico / Planejamento
**Quando:** foco em negócio, roadmap, priorização, OKRs, tomada de decisão executiva.
**Prioriza:** Decisões cronológicas, Alternativas rejeitadas com justificativa, Próximos passos, Stakeholders, Prazos e marcos.
**Reduz:** Stack técnica (omitir se irrelevante).

---

### Perfil Criativo
**Quando:** escrita, design, conteúdo, narrativa, roteiro, campanha, branding.
**Prioriza:** Diretrizes criativas, Tom e voz, Restrições de estilo, Estado da obra, Fio narrativo em construção.
**Reduz:** Stack técnica, Requisitos funcionais.

---

### Perfil Médico / Científico
**Quando:** discussão clínica, diagnóstico, protocolo terapêutico, pesquisa científica, metodologia, análise de dados, revisão de literatura.
**Prioriza:**
- Hipótese diagnóstica ou científica central
- Protocolo e metodologia definidos
- Medicamentos, doses e contraindicações mencionados
- Resultados e achados até o momento
- Limitações metodológicas identificadas
- Referências bibliográficas citadas
- Próximos passos do protocolo ou investigação

**Alerta especial:** contraindicações e doses — marcadas em 🔴, nunca omitidas.
**Reduz:** jargão jurídico, stack técnica de TI.

---

### Perfil Educacional / Didático
**Quando:** ensino, tutoria, elaboração de material didático, plano de aula, trilha de aprendizado, explicação progressiva de conceitos.
**Prioriza:**
- Nível e perfil do aprendiz (iniciante, intermediário, avançado; área de formação)
- Conteúdo já ensinado e assimilado
- Dificuldades e dúvidas identificadas
- Analogias e exemplos já utilizados (não repetir)
- Próxima etapa didática e pré-requisitos
- Material já produzido (exercícios, resumos, questões)
- Objetivos de aprendizagem declarados

**Reduz:** terminologia excessivamente técnica não introduzida ainda, código não relacionado ao ensino.

---

### Perfil Investigativo / Pesquisa
**Quando:** pesquisa documental, jornalismo investigativo, due diligence, inteligência competitiva, análise de fontes, mapeamento de evidências.
**Prioriza:**
- Hipótese ou pergunta investigativa central
- Fontes consultadas e seu status (confirmada, pendente, descartada, contraditória)
- Achados confirmados vs. suspeitos
- Contradições e inconsistências identificadas
- Lacunas de informação ainda abertas
- Linha do tempo de eventos mapeada
- Conexões entre pessoas, entidades ou fatos

**Alerta especial:** fontes contraditórias — sempre destacadas; nunca omitir divergência.
**Reduz:** stack técnica, terminologia clínica.

---

### Perfil Geral
Fallback automático quando nenhum perfil específico é detectado.
Usa o template completo sem otimizações de perfil.

Ver templates por perfil em `references/transfer-report-template.md`.

---

## MECANISMO 5 — Modo Silencioso

Documentado acima na seção MODO SILENCIOSO.
Ativar quando o usuário não quer interrupções no fluxo de trabalho.

**Exceção obrigatória no Perfil Jurídico:** prazos processuais são sempre reportados, mesmo em modo silencioso.

---

## MECANISMO 6 — Integração com Memória do Claude

Durante a evacuação, Claude identifica e salva nas **memórias persistentes**
preferências recorrentes do usuário úteis em futuras conversas.

### O que salvar na memória

**Sempre que detectado:**
- Área de atuação profissional (ex: advogado, médico, dev, professor)
- Stack tecnológica preferida
- Linguagem de programação principal
- Estilo de código (comentado, funcional, sem classes, etc.)
- Idioma preferido para código e comentários
- Formato de resposta preferido (conciso, detalhado, com exemplos)
- Restrições recorrentes ("nunca usa X", "sempre prefere Y")
- Perfil de conversa predominante (Jurídico, Técnico, etc.)

**Nunca salvar:**
- Decisões específicas de um projeto ou processo (ficam só no relatório)
- Dados sensíveis (credenciais, dados de partes, informações pessoais de clientes)
- Números de processos, nomes de partes ou valores em litígio

### Como salvar

Usar `memory_user_edits` com `command: "add"` para cada preferência,
formulada de forma compacta:

```
"Usuário é advogado, atua em direito cível, criminal e sucessões"
"Usuário prefere perfil Jurídico no Context Guardian"
"Usuário prefere Python com type hints e sem frameworks pesados"
"Usuário escreve código em inglês mas conversa em PT-BR"
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

**Jurídico — gatilhos adicionais:**
`prazo` · `vencimento` · `protocolar` · `confundiu os processos` · `processo errado`

### Passo 1 — Anúncio

```
⚠️ **Context Guardian — Modo Evacuação**
Motivo: [sinal detectado]  |  Perfil: [perfil ativo]

Gerando relatório + Prompts de Retomada. Não farei mais nada até concluir.
```

### Passo 2 — Varredura Exaustiva (turno 1 → atual)

Extrair por perfil:
- **A** Identidade: nome/caso, objetivo exato, contexto do usuário, perfil
- **B** Fatos Técnicos *(Técnico/Geral)*: linguagens, frameworks, infra, configs
- **C** Fatos Jurídicos *(Jurídico)*: processo(s), partes, vara, teses, prazos, peças, provas
- **D** Decisões Cronológicas: [turno] decisão — justificativa — alternativas rejeitadas
- **E** Código e Artefatos *(Técnico)*: estrutura de pastas, snippets completos, código incompleto
- **F** Diretrizes Criativas *(Criativo)*: tom, voz, restrições, estado da obra
- **G** Protocolo/Metodologia *(Médico/Científico)*: hipótese, protocolo, achados, contraindicações
- **H** Estado Didático *(Educacional)*: nível do aprendiz, conteúdo ensinado, próxima etapa
- **I** Mapa de Fontes *(Investigativo)*: fontes, achados, contradições, lacunas
- **J** Problemas e Tentativas: problema → falhas (com motivo) → solução adotada
- **K** Requisitos e Restrições: funcionais, técnicos, preferências, constraints
- **L** Estado Atual: o que estava sendo feito, ponto exato de parada, próximos passos
- **M** Referências: URLs, documentos, fontes, jurisprudência citada

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
Projeto/Caso: [nome] | Objetivo: [1 frase] | Perfil: [tipo]
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

## CONTEXTO ESPECÍFICO DO PERFIL
[Técnico: stack | Jurídico: processo+partes+teses+prazos | Médico: protocolo+contraindicações | etc.]

## HISTÓRICO
[parágrafo denso: o que foi construído/elaborado, problemas resolvidos, tentativas fracassadas]

## ARTEFATOS RELEVANTES
[código incompleto / peças em rascunho / material didático em construção]

## PENDÊNCIAS
- ❓ [problema/questão em aberto]
- 🔴 [prazo crítico, se perfil Jurídico]

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
  📋 Prompt Completo — para conversas técnicas, jurídicas e longas
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
- ❌ NUNCA truncar código parcial ou peça jurídica em rascunho
- ❌ NUNCA gerar apenas no chat — sempre arquivo .md
- ❌ NUNCA omitir prazo processual, mesmo em modo silencioso
- ❌ NUNCA salvar dados pessoais de clientes, partes ou pacientes na memória
- ✅ Completude > brevidade no relatório .md
- ✅ Marcar 🔴 itens que o novo Claude deve saber imediatamente
- ✅ Perfil prioriza seções — nunca omite completamente
- ✅ Salvar na memória apenas preferências recorrentes do usuário
- ✅ Em conversas com múltiplos processos: manter mapa de processos separado

---

## Automação Total — Ambientes Externos

| Ambiente | Automação |
|---|---|
| **Claude.ai** | Semi-automático — 3 passos manuais |
| **Claude Code** | ✅ Total — subagentes nativos |
| **API Python/Node** | ✅ Total — orquestrador monitora tokens |
| **n8n** | ✅ Total — fluxo visual sem código |

Implementações completas em `references/automation-orchestrator.md`.
