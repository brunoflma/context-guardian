# Template: Relatório de Transferência de Contexto (.md)

> Este arquivo é o template que Claude deve usar ao gerar o relatório de evacuação.
> Preencher TODAS as seções aplicáveis. Remover apenas seções genuinamente vazias.
> O arquivo gerado deve ser rico, denso e completamente auto-suficiente.

---

```markdown
# 📋 RELATÓRIO DE TRANSFERÊNCIA — [NOME DO PROJETO]

> **Gerado pelo Context Guardian**  
> Turno da conversa: [N]  
> Motivo: [degradação detectada / conversa longa / pedido do usuário]  
> Instrução de uso: Cole este arquivo como anexo na primeira mensagem de uma nova conversa,
> ou copie o conteúdo e cole diretamente. O novo agente terá contexto completo.

---

## 🔴 LEIA PRIMEIRO — Itens Críticos

> Um novo Claude DEVE saber isso antes de qualquer coisa.

- 🔴 [fato/decisão/restrição crítica 1]
- 🔴 [fato/decisão/restrição crítica 2]
- 🔴 [fato/decisão/restrição crítica 3]
*(adicione quantos forem necessários — não limite)*

---

## 🎯 Identidade do Projeto

| Campo                  | Valor                                      |
|------------------------|--------------------------------------------|
| **Nome do projeto**    | [nome exato como o usuário usa]            |
| **Objetivo principal** | [em uma ou duas frases exatas]             |
| **Fase atual**         | [ex: implementação do módulo de auth]      |
| **Usuário / papel**    | [ex: desenvolvedor solo, CTO de startup]   |
| **Domínio**            | [ex: fintech B2B, app mobile, API interna] |
| **Contexto temporal**  | [prazo, sprint, marco se mencionado]       |

---

## ⚙️ Stack Técnica

### Linguagens e Runtimes
| Item          | Versão / Detalhes                |
|---------------|----------------------------------|
| [linguagem]   | [versão exata se mencionada]     |
| [runtime]     | [versão exata se mencionada]     |

### Frameworks e Bibliotecas
| Biblioteca / Framework | Versão  | Finalidade               |
|------------------------|---------|--------------------------|
| [nome]                 | [v]     | [para que serve no projeto] |

### Infraestrutura
| Componente     | Detalhe                          |
|----------------|----------------------------------|
| **Banco**      | [ex: PostgreSQL 15, local]       |
| **Deploy**     | [ex: Railway, sem CI ainda]      |
| **Ambiente**   | [ex: dev local, Docker]          |
| **OS / Plat.** | [ex: macOS, Linux]               |

### Variáveis de Ambiente e Configurações
```env
# Estrutura (sem valores sensíveis)
[NOME_DA_VAR]=[tipo/formato esperado]
[OUTRA_VAR]=[tipo/formato esperado]
```

---

## 📌 Decisões Tomadas

> Cronológicas. Incluir justificativa sempre que disponível.
> Não resumir — preservar nuances.

### Decisão 1 — [nome curto da decisão]
- **O que foi decidido:** [descrição completa]
- **Justificativa:** [por quê esta e não outra]
- **Alternativas descartadas:** [o que foi rejeitado e por quê]
- **Posição na conversa:** [ex: após discutir autenticação, turno ~15]

### Decisão 2 — [nome curto]
- **O que foi decidido:** [...]
- **Justificativa:** [...]
- **Alternativas descartadas:** [...]
- **Posição na conversa:** [...]

*(continuar para todas as decisões da conversa)*

---

## 💻 Código e Artefatos

### Estrutura de Arquivos Estabelecida
```
[projeto]/
├── [pasta]/
│   ├── [arquivo] — [o que faz]
│   └── [arquivo] — [o que faz]
└── [arquivo] — [o que faz]
```

### Arquivos por Status
| Arquivo                | Status              | Descrição                    |
|------------------------|---------------------|------------------------------|
| `[path/arquivo.ext]`   | ✅ Criado           | [o que contém]               |
| `[path/arquivo.ext]`   | 🔄 Em progresso     | [o que falta]                |
| `[path/arquivo.ext]`   | 📋 Planejado        | [o que deve conter]          |

### Código Crítico — Não Pode Ser Perdido

#### [nome do trecho — ex: Schema do banco]
```[linguagem]
[código completo — não resumir]
```

#### [nome do trecho — ex: Lógica de autenticação]
```[linguagem]
[código completo]
```

*(incluir todos os snippets críticos gerados na conversa)*

---

## 📋 Requisitos

### Funcionais
- [ ] [RF01] [o que o sistema deve fazer]
- [ ] [RF02] [outro requisito]

### Não-Funcionais / Restrições Técnicas
- ❌ **Proibido:** [o que não pode ser usado/feito, ex: sem dependências de terceiros]
- ⚠️ **Limitação:** [restrição de ambiente, ex: deve rodar em Node 18 LTS]
- 🔒 **Segurança:** [requisitos de segurança mencionados]

### Preferências do Usuário
| Preferência          | Valor                                    |
|----------------------|------------------------------------------|
| Idioma do código     | [PT-BR / EN / misto]                     |
| Estilo de código     | [ex: comentado, funcional, sem classes]  |
| Formato de resposta  | [ex: conciso, sem markdown excessivo]    |
| Outras               | [outras preferências mencionadas]        |

---

## 🔍 Problemas, Tentativas e Soluções

### Problema 1 — [nome descritivo]
**Descrição:** [o problema em detalhes]

**Tentativas que falharam:**
1. [abordagem tentada] → [por que falhou]
2. [abordagem tentada] → [por que falhou]

**Solução adotada:** [o que funcionou]  
**Status:** [✅ Resolvido / 🔄 Em progresso / ❌ Bloqueado]

### Problema 2 — [nome]
*(repetir estrutura)*

---

## ❓ Estado Atual e Próximos Passos

### O que estava sendo feito no momento desta transferência:
> [Descrição precisa e completa do ponto exato — o que estava em discussão,
> qual parte do código estava sendo escrita, qual decisão estava sendo tomada]

### Próximos Passos (ordem definida)
1. **[Passo imediato]**
   - Detalhes: [o que exatamente fazer]
   - Contexto: [por que este passo agora]

2. **[Passo seguinte]**
   - Detalhes: [...]

3. **[Passo posterior]**
   - Detalhes: [...]

### Perguntas em Aberto / Decisões Pendentes
- ❓ [pergunta que ainda precisa de resposta do usuário]
- ❓ [decisão técnica ainda não tomada]
- ❓ [ponto de investigação pendente]

---

## 🔗 Referências e Recursos

| Recurso                    | URL / Local                  | Para que serve          |
|----------------------------|------------------------------|-------------------------|
| [nome]                     | [url ou caminho]             | [finalidade]            |

---

## 📋 Prompt de Retomada para Novo Agente

> **Este é o bloco mais importante do relatório.**
> Cole como PRIMEIRA mensagem na nova conversa — com ou sem o arquivo .md.
> Deve ser completamente auto-suficiente: o novo agente não precisa de mais nada para continuar.

---

```
════════════════════════════════════════════════════════════════
PROMPT DE RETOMADA — CONTEXT GUARDIAN
Copie todo este bloco e cole como PRIMEIRA mensagem na nova conversa.
════════════════════════════════════════════════════════════════

Você está assumindo uma conversa que foi transferida por limite de contexto.
Leia tudo abaixo antes de responder qualquer coisa.

## IDENTIDADE
Projeto: [nome exato do projeto]
Objetivo: [uma frase precisa — o que estamos construindo/resolvendo]
Eu sou: [papel/contexto do usuário, ex: "desenvolvedor solo, foco back-end Python"]

## ESTADO NO MOMENTO DA SUSPENSÃO
Estávamos em: [descrição exata da atividade em andamento]
Ponto exato de parada: [última coisa dita/escrita antes da evacuação — ser cirúrgico]
Status do trabalho: [ex: "código 60% escrito", "decisão tomada, sem implementação ainda"]

## DECISÕES TOMADAS — NÃO QUESTIONAR
1. [decisão] — [justificativa em uma linha]
2. [decisão] — [justificativa em uma linha]
3. [decisão] — [justificativa em uma linha]
[continuar para todas as decisões]

## RESTRIÇÕES ABSOLUTAS
- ❌ [o que não pode ser usado/feito] — [motivo]
- ❌ [o que não pode ser usado/feito] — [motivo]
[sem restrições = omitir esta seção]

## STACK E AMBIENTE
- Linguagem: [nome + versão exata]
- Framework: [nome + versão]
- Banco: [nome + versão + local ex: local/cloud]
- Infra/Deploy: [detalhes]
- Ambiente: [ex: macOS local, Docker, WSL2]

## HISTÓRICO DA CONVERSA ANTERIOR
[Parágrafo(s) denso(s) cobrindo: o que foi construído, em que ordem, quais problemas
foram encontrados, quais abordagens foram tentadas e descartadas, o que funcionou.
Não resumir demais — este é o único histórico que o novo agente terá.]

## CÓDIGO EXISTENTE E ARTEFATOS
[Incluir snippets de código críticos, especialmente qualquer código incompleto
que estava sendo escrito no momento da suspensão. Incluir estrutura de pastas
se estabelecida. Nunca truncar código parcial — é fundamental para continuidade.]

```[linguagem]
// [nome do arquivo / contexto]
[código]
```

## ARQUIVOS POR STATUS
| Arquivo | Status | O que contém |
|---------|--------|--------------|
| `[path]` | ✅ Completo / 🔄 Parcial / 📋 Planejado | [descrição] |

## PROBLEMAS EM ABERTO
- ❓ [problema não resolvido ou questão pendente]
- ❓ [decisão técnica ainda não tomada]

## PRIMEIRA AÇÃO DO NOVO AGENTE
[Instrução imperativa, sem ambiguidade, sem margem para interpretação.
Exemplo: "Continue escrevendo a função validate_token() — o corpo estava sendo
escrito e parou após a verificação de expiração. A próxima linha deve verificar
a assinatura com JWT_SECRET e retornar o payload decodificado ou lançar AuthError."]

## REFERÊNCIA COMPLETA
O relatório detalhado está no arquivo: [nome-do-arquivo.md]
Faça upload deste arquivo junto com este prompt para referência completa.
════════════════════════════════════════════════════════════════
```
