# Templates de Relatório de Transferência — por Perfil

Escolha o template correspondente ao perfil detectado na evacuação.
Perfis: Técnico · Estratégico · Criativo · Geral

---

## TEMPLATE TÉCNICO / CÓDIGO

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DO PROJETO]
**Context Guardian v1.1** | Turno: [N] | Perfil: Técnico
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
**Context Guardian v1.1** | Turno: [N] | Perfil: Estratégico

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
**Context Guardian v1.1** | Turno: [N] | Perfil: Criativo

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
**Context Guardian v1.1** | Turno: [N] | Perfil: Geral

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
