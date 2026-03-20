# Templates de Relatório de Transferência — por Perfil

Escolha o template correspondente ao perfil detectado na evacuação.
Perfis: Técnico · Estratégico · Criativo · Geral

---

## TEMPLATE TÉCNICO / CÓDIGO

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DO PROJETO]
**Context Guardian v1.1.1** | Turno: [N] | Perfil: Técnico
Motivo: [degradação / conversa longa / pedido do usuário]

---

## 🔴 LEIA PRIMEIRO

- 🔴 [fato/decisão crítica 1]
- 🔴 [fato/decisão crítica 2]

---

## 🎯 IDENTIDADE

| Campo | Valor |
|-------|-------|
| **Projeto** | [nome exato] |
| **Objetivo** | [1-2 frases precisas] |
| **Fase atual** | [ex: implementação do módulo de auth] |
| **Usuário** | [papel/contexto, ex: dev solo, fintech B2B] |

---

## ⚙️ STACK TÉCNICA

| Item | Versão / Detalhe |
|------|-----------------|
| Linguagem | [ex: Python 3.11] |
| Framework | [ex: FastAPI 0.110] |
| Banco | [ex: PostgreSQL 15, local] |
| Infra | [ex: Docker, sem CI ainda] |
| OS/Plataforma | [ex: Linux Ubuntu 22.04] |

### Variáveis de Ambiente (estrutura, sem valores)
```env
[NOME_VAR]=[tipo/formato esperado]
```

### Configurações Estabelecidas
[configs relevantes — formatters, linters, padrões de projeto]

---

## 📌 DECISÕES TOMADAS (cronológicas)

### Decisão 1 — [nome curto]
- **O que:** [descrição completa]
- **Por quê:** [justificativa]
- **Descartado:** [alternativas rejeitadas e motivo]
- **Turno aprox.:** [N]

### Decisão 2 — [nome curto]
[repetir estrutura]

---

## 💻 CÓDIGO E ARTEFATOS

### Estrutura de Arquivos
```
[projeto]/
├── [pasta]/
│   ├── [arquivo] — [o que faz]
│   └── [arquivo] — [o que faz]
└── [arquivo] — [o que faz]
```

### Status dos Arquivos
| Arquivo | Status | Descrição |
|---------|--------|-----------|
| `[path]` | ✅ Completo / 🔄 Parcial / 📋 Planejado | [o que contém] |

### Código Crítico (incluir COMPLETO — nunca truncar)

#### [nome do trecho]
```[linguagem]
[código completo]
```

---

## 🔍 PROBLEMAS E TENTATIVAS

### Problema 1 — [nome]
- **Descrição:** [detalhes]
- **Tentativas que falharam:** [abordagem] → [por que falhou]
- **Solução adotada:** [o que funcionou]
- **Status:** ✅ Resolvido / 🔄 Em progresso / ❌ Bloqueado

---

## 📋 REQUISITOS E RESTRIÇÕES

### Funcionais
- [ ] [RF01] [o que deve fazer]

### Restrições Técnicas
- ❌ **Proibido:** [o que não pode ser usado]
- ⚠️ **Limitação:** [restrição de ambiente]

### Preferências do Usuário
| Preferência | Valor |
|-------------|-------|
| Idioma do código | [PT-BR / EN] |
| Estilo | [ex: comentado, funcional] |
| Formato de resposta | [ex: conciso] |

---

## 📍 ESTADO ATUAL

**O que estava sendo feito:**
[descrição precisa e completa]

**Ponto exato de parada:**
[última linha/ação/decisão — cirúrgico]

### Próximos Passos
1. **[Passo imediato]** — [detalhes]
2. **[Passo seguinte]** — [detalhes]

### Pendências
- ❓ [questão em aberto]

---

## 🔗 REFERÊNCIAS
| Recurso | URL / Local | Finalidade |
|---------|-------------|------------|
| [nome] | [url] | [para que serve] |

---

## 📋 PROMPTS DE RETOMADA

### Prompt Completo
[inserir bloco completo — ver estrutura no SKILL.md Passo 4]

### Prompt Compacto
[inserir bloco compacto — ver estrutura no SKILL.md Mecanismo 3]
```

---

## TEMPLATE ESTRATÉGICO / PLANEJAMENTO

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DO PROJETO]
**Context Guardian v1.1.1** | Turno: [N] | Perfil: Estratégico

---

## 🔴 LEIA PRIMEIRO
- 🔴 [decisão estratégica crítica 1]
- 🔴 [restrição crítica de negócio]

---

## 🎯 CONTEXTO

| Campo | Valor |
|-------|-------|
| **Projeto / Iniciativa** | [nome] |
| **Objetivo estratégico** | [em 1-2 frases] |
| **Fase** | [ex: definição de roadmap Q3] |
| **Stakeholders** | [quem está envolvido] |
| **Prazo / Marco** | [se mencionado] |

---

## 📌 DECISÕES TOMADAS (cronológicas)

### Decisão 1 — [nome]
- **O que:** [descrição]
- **Justificativa:** [raciocínio estratégico]
- **Alternativas descartadas:** [e por quê]
- **Impacto:** [o que muda com essa decisão]

---

## ❌ FORA DO ESCOPO (definido explicitamente)

- [o que foi explicitamente descartado ou adiado]
- [restrições de negócio ou orçamento]

---

## 📊 ESTADO DO PLANEJAMENTO

### O que foi definido
- [lista do que está fechado]

### O que está em aberto
- ❓ [decisão pendente]
- ❓ [questão não resolvida]

### Próximos Passos
1. [ação] — [responsável / prazo se mencionado]

---

## 📋 PROMPTS DE RETOMADA

### Prompt Compacto (recomendado para este perfil)
[inserir bloco compacto]

### Prompt Completo
[inserir bloco completo]
```

---

## TEMPLATE CRIATIVO

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DA OBRA/PROJETO]
**Context Guardian v1.1.1** | Turno: [N] | Perfil: Criativo

---

## 🔴 LEIA PRIMEIRO
- 🔴 [diretriz criativa inegociável]
- 🔴 [restrição de tom ou estilo]

---

## 🎯 IDENTIDADE CRIATIVA

| Campo | Valor |
|-------|-------|
| **Obra / Projeto** | [nome] |
| **Formato** | [ex: artigo, roteiro, conto, campanha] |
| **Objetivo** | [o que a obra deve causar/comunicar] |
| **Público** | [para quem] |
| **Fase** | [ex: rascunho do segundo ato] |

---

## 🎨 DIRETRIZES CRIATIVAS

### Tom e Voz
[descrição detalhada do tom — formal/informal, irônico/direto, etc.]

### Restrições de Estilo
- ❌ [o que NÃO usar — palavras, estruturas, referências proibidas]
- ✅ [o que DEVE estar presente]

### Referências e Inspirações
[obras, autores, exemplos que guiam o estilo]

---

## 📄 ESTADO DA OBRA

### O que foi produzido
[resumo do conteúdo criado até agora — preservar nuances]

### Ponto de parada
[exatamente onde estava ao ser suspenso — parágrafo, cena, seção]

### Fio narrativo / Argumento em construção
[o raciocínio ou narrativa que estava sendo desenvolvida]

---

## 📋 PROMPTS DE RETOMADA

### Prompt Compacto (recomendado para este perfil)
[inserir bloco compacto]

### Prompt Completo
[inserir bloco completo]
```

---

## TEMPLATE GERAL (Fallback)

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA
**Context Guardian v1.1.1** | Turno: [N] | Perfil: Geral

---

## 🔴 LEIA PRIMEIRO
- 🔴 [item crítico]

---

## 🎯 CONTEXTO
- **Tópico:** [assunto da conversa]
- **Objetivo:** [o que o usuário quer alcançar]
- **Estado:** [onde chegamos]

---

## 📌 DECISÕES E DEFINIÇÕES
[lista cronológica de tudo que foi decidido ou definido]

## 🔍 PROBLEMAS RESOLVIDOS
[o que foi resolvido e como]

## 📍 ESTADO ATUAL E PRÓXIMOS PASSOS
[o que estava sendo feito e o que vem a seguir]

---

## 📋 PROMPTS DE RETOMADA

### Prompt Compacto
[inserir bloco compacto]

### Prompt Completo
[inserir bloco completo]
```

---

## TEMPLATE JURÍDICO

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DO CASO / PROCESSO]
**Context Guardian v1.2.0** | Turno: [N] | Perfil: Jurídico
Motivo: [degradação / conversa longa / pedido do usuário]

---

## 🔴 LEIA PRIMEIRO

- 🔴 [prazo processual crítico — data e ato]
- 🔴 [tese central fixada — não questionar]
- 🔴 [restrição processual crítica]

---

## ⚖️ IDENTIFICAÇÃO DO(S) PROCESSO(S)

| Campo | Processo 1 | Processo 2 (se houver) |
|-------|-----------|------------------------|
| **Número** | [nº completo] | [nº completo] |
| **Vara / Juízo** | [vara] | [vara] |
| **Tribunal** | [tribunal] | [tribunal] |
| **Instância** | [1ª / 2ª / STJ / STF] | |
| **Fase atual** | [conhecimento / execução / recurso] | |
| **Tipo de ação** | [petição inicial / inventário / execução...] | |

---

## 👥 PARTES

| Polo | Nome | Qualificação |
|------|------|-------------|
| Autor / Requerente | [nome] | [qualificação] |
| Réu / Requerido | [nome] | [qualificação] |
| Terceiros / Intervenientes | [nome] | [papel] |
| Representação do usuário | [autor / réu / terceiro] | [advogado / parte] |

---

## 📅 PRAZOS PROCESSUAIS

| Ato | Prazo | Data-Limite | Status |
|-----|-------|-------------|--------|
| 🔴 [ato] | [X dias] | [DD/MM/AAAA] | [pendente / cumprido] |
| [ato] | [X dias] | [DD/MM/AAAA] | [pendente / cumprido] |

---

## ⚖️ TESES JURÍDICAS E FUNDAMENTOS

### Teses fixadas (não questionar)
1. [tese] — Fundamento: [art. X, Lei Y / Súmula Z / REsp XXXX]
2. [tese] — Fundamento: [referência]

### Jurisprudência mapeada
- [tribunal] — [referência] — [síntese da decisão]

### Teses descartadas (e motivo)
- [tese descartada] — Motivo: [por que não usar]

---

## 📄 PEÇAS ELABORADAS E STATUS

| Peça | Status | Observação |
|------|--------|------------|
| [nome da peça] | ✅ Protocolada / 🔄 Em rascunho / 📋 Planejada | [obs] |
| [nome da peça] | | |

### Rascunho em construção no momento da evacuação
[incluir o rascunho COMPLETO — nunca truncar]

---

## 🗂️ PROVAS E DOCUMENTOS

| Documento | Status | Relevância |
|-----------|--------|-----------|
| [documento] | ✅ Juntado / ⏳ Pendente / ❌ Indisponível | [para qual tese] |

---

## 🧭 ESTRATÉGIA PROCESSUAL

**Postura definida:** [defensiva / ofensiva / negocial / mista]

**Estratégia principal:** [descrição]

**Alternativas descartadas:** [e por quê]

**Decisões do juízo relevantes:** [o que já foi decidido, despachos, liminares]

---

## 📍 ESTADO ATUAL

**O que estava sendo feito:** [descrição precisa]

**Ponto exato de parada:** [última linha/seção/argumento]

### Próximos Passos
1. **[Próximo ato imediato]** — [prazo / urgência]
2. **[Passo seguinte]** — [detalhes]

### Pendências
- ❓ [questão jurídica em aberto]
- 📋 [documento que falta]

---

## 🔗 REFERÊNCIAS

| Recurso | Local / URL | Finalidade |
|---------|------------|-----------|
| [peça / decisão / doutrina] | [local] | [para que serve] |

---

## 📋 PROMPTS DE RETOMADA

### Prompt Completo
[inserir bloco completo]

### Prompt Compacto
[inserir bloco compacto]
```

---

## TEMPLATE MÉDICO / CIENTÍFICO

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DO CASO / PESQUISA]
**Context Guardian v1.2.0** | Turno: [N] | Perfil: Médico/Científico
Motivo: [degradação / conversa longa / pedido do usuário]

---

## 🔴 LEIA PRIMEIRO

- 🔴 [contraindicação crítica]
- 🔴 [restrição metodológica inegociável]
- 🔴 [achado que muda o protocolo]

---

## 🎯 IDENTIDADE

| Campo | Valor |
|-------|-------|
| **Caso / Pesquisa** | [nome] |
| **Hipótese central** | [hipótese diagnóstica ou científica] |
| **Objetivo** | [diagnóstico / tratamento / pesquisa / revisão] |
| **Fase** | [anamnese / diagnóstico / tratamento / análise de dados] |
| **Contexto** | [clínico / laboratorial / epidemiológico / revisão] |

---

## 🧪 PROTOCOLO E METODOLOGIA

**Protocolo definido:** [descrição]
**Metodologia:** [tipo de estudo / abordagem terapêutica]
**Critérios de inclusão/exclusão:** [se pesquisa]

### Medicamentos / Intervenções

| Item | Dose / Parâmetro | Contraindicações | Status |
|------|-----------------|-----------------|--------|
| 🔴 [medicamento] | [dose] | [contraindicações] | [ativo / suspenso] |

---

## 📊 ACHADOS E RESULTADOS

**Achados confirmados:** [lista]
**Achados suspeitos / pendentes:** [lista]
**Resultados de exames:** [relevantes para o caso]

---

## 📚 REFERÊNCIAS BIBLIOGRÁFICAS

| Referência | Síntese relevante |
|-----------|-----------------|
| [autor, ano, periódico] | [o que sustenta] |

---

## 📍 ESTADO ATUAL E PRÓXIMOS PASSOS

**Fase:** [onde estamos no protocolo / investigação]
**Próxima etapa:** [descrição]
**Limitações identificadas:** [lista]

---

## 📋 PROMPTS DE RETOMADA

### Prompt Completo
[inserir bloco completo]

### Prompt Compacto
[inserir bloco compacto]
```

---

## TEMPLATE EDUCACIONAL / DIDÁTICO

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DA TRILHA / AULA / MATERIAL]
**Context Guardian v1.2.0** | Turno: [N] | Perfil: Educacional
Motivo: [degradação / conversa longa / pedido do usuário]

---

## 🎯 IDENTIDADE DIDÁTICA

| Campo | Valor |
|-------|-------|
| **Tema / Disciplina** | [nome] |
| **Objetivo de aprendizagem** | [o que o aprendiz deve saber ao final] |
| **Nível do aprendiz** | [iniciante / intermediário / avançado] |
| **Perfil** | [área de formação, experiência prévia] |
| **Formato** | [aula / trilha / tutoria / material] |

---

## ✅ CONTEÚDO JÁ ENSINADO

| Tópico | Status | Observação |
|--------|--------|-----------|
| [tópico] | ✅ Assimilado / 🔄 Com dificuldade / ⏭️ Introduzido | [obs] |

---

## ⚠️ DIFICULDADES IDENTIFICADAS

- [dificuldade / dúvida] — Como foi abordada: [abordagem]
- [conceito com resistência] — Analogia usada: [analogia — não repetir]

---

## 📚 MATERIAL PRODUZIDO

| Item | Status |
|------|--------|
| [exercício / resumo / questão] | ✅ Concluído / 🔄 Em construção |

### Material em construção no momento da evacuação
[incluir COMPLETO — nunca truncar]

---

## 📍 PRÓXIMA ETAPA DIDÁTICA

**Próximo tópico:** [nome]
**Pré-requisitos:** [o que o aprendiz já precisa saber — já ensinado? ✅/❌]
**Abordagem planejada:** [como ensinar]

---

## 📋 PROMPTS DE RETOMADA

### Prompt Compacto (recomendado para este perfil)
[inserir bloco compacto]

### Prompt Completo
[inserir bloco completo]
```

---

## TEMPLATE INVESTIGATIVO / PESQUISA

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DA INVESTIGAÇÃO / PESQUISA]
**Context Guardian v1.2.0** | Turno: [N] | Perfil: Investigativo
Motivo: [degradação / conversa longa / pedido do usuário]

---

## 🔴 LEIA PRIMEIRO

- 🔴 [contradição crítica entre fontes]
- 🔴 [lacuna que bloqueia a investigação]
- 🔴 [hipótese já descartada — não revisitar]

---

## 🎯 IDENTIDADE DA INVESTIGAÇÃO

| Campo | Valor |
|-------|-------|
| **Tema** | [nome] |
| **Hipótese central** | [o que se investiga] |
| **Objetivo** | [o que se quer provar / entender / mapear] |
| **Fase** | [levantamento / análise / síntese / conclusão] |

---

## 🗂️ MAPA DE FONTES

| Fonte | Tipo | Status | Achado Principal | Confiabilidade |
|-------|------|--------|-----------------|---------------|
| [fonte] | [doc / entrevista / dado] | ✅ Confirmada / ⏳ Pendente / ❌ Descartada | [síntese] | [alta / média / baixa] |

---

## 🔍 ACHADOS E CONTRADIÇÕES

**Achados confirmados:**
1. [achado] — Fonte(s): [referência]

**Contradições identificadas:**
- 🔴 [fonte A] afirma [X] × [fonte B] afirma [Y] — Status: [não resolvida / investigando]

**Hipóteses descartadas:**
- [hipótese] — Motivo: [por que descartada]

---

## 🗓️ LINHA DO TEMPO (se relevante)

| Data | Evento | Fonte | Confiabilidade |
|------|--------|-------|---------------|
| [data] | [evento] | [fonte] | [alta/média/baixa] |

---

## 🔗 CONEXÕES MAPEADAS

[mapa de conexões entre pessoas, entidades ou fatos — em texto ou lista]

---

## ❓ LACUNAS ABERTAS

- [informação que falta e onde buscar]
- [pergunta ainda sem resposta]

---

## 📍 ESTADO ATUAL E PRÓXIMOS PASSOS

**Onde estamos:** [fase e atividade atual]
**Próxima fonte / ação:** [o que consultar / fazer]

---

## 📋 PROMPTS DE RETOMADA

### Prompt Completo
[inserir bloco completo]

### Prompt Compacto
[inserir bloco compacto]
```
