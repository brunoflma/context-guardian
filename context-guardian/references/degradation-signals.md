# Taxonomia de Sinais de Degradação

---

## Nível 1 — CRÍTICO (Evacuação Imediata)

Informação já foi perdida. Não há verificação — evacuar agora.

| Sinal | Exemplo Concreto |
|-------|-----------------|
| Pergunta algo já respondido | "Qual linguagem você está usando?" — dito no turno 3 |
| Contradiz decisão anterior | Após decidir REST, sugere implementar GraphQL |
| Ignora restrição estabelecida | Usa TypeScript após "sem TypeScript" |
| Re-propõe alternativa rejeitada | Sugere Redis após usuário ter descartado Redis |
| Descreve código já produzido como "vamos criar" | Arquivo já foi gerado na conversa |

---

## Nível 2 — ALTO (Evacuação Recomendada)

Degradação ocorrendo ativamente.

| Sinal | Como Reconhecer |
|-------|----------------|
| Incerteza interna sobre fato estabelecido | Não tem certeza se usam PostgreSQL ou MySQL — mas isso foi definido |
| Usuário corrigiu 2x sobre o mesmo ponto | Repetição do mesmo erro após correção |
| Claude adiciona disclaimers sobre coisas decididas | "Você poderia usar X ou Y" — quando X já foi escolhido |

---

## Nível 3 — SEMÂNTICO (Sinais Graduais — NOVO em v1.1)

Sinais sutis que precedem a degradação total. Detectar cedo evita evacuação.

### 3a — Genericidade Crescente

**O que é:** respostas que eram específicas ao projeto ficam progressivamente genéricas.

**Exemplos concretos:**
- Início da conversa: "Use o método `validate_cpf()` que já criamos no módulo `utils/validators.py`"
- Após degradação parcial: "Você pode criar uma função de validação para CPF"

**Como detectar:** comparar o nível de especificidade da resposta atual com respostas anteriores sobre o mesmo tópico. Se há queda sem motivo (o usuário não pediu simplificação), é sinal.

**Ação:** checkpoint imediato.

---

### 3b — Perda de Convenções

**O que é:** Claude para de usar nomes, padrões ou estilos estabelecidos no início da conversa.

**Exemplos concretos:**
- Usuário estabeleceu: classes em PascalCase, variáveis em snake_case, comentários em PT-BR
- Após degradação: Claude gera código com camelCase e comentários em inglês sem justificativa

- Usuário chamou o projeto de "Sistema Atlas" durante toda a conversa
- Após degradação: Claude começa a chamar de "seu sistema" ou "a aplicação"

**Como detectar:** monitorar uso de nomes próprios, padrões de nomenclatura e estilo declarados no início.

**Ação:** checkpoint imediato.

---

### 3c — Qualidade Regressiva

**O que é:** código ou conteúdo gerado fica mais simples, menos robusto ou menos alinhado ao padrão estabelecido.

**Exemplos concretos:**
- Padrão estabelecido: funções com type hints, docstrings e tratamento de exceção
- Após degradação: Claude gera função sem type hints, sem docstring, sem try/except

- Padrão estabelecido: respostas estruturadas com seções claras
- Após degradação: respostas em parágrafo único sem estrutura

**Como detectar:** comparar qualidade estrutural da saída atual com as primeiras saídas da conversa.

**Ação:** checkpoint imediato.

---

### 3d — Disclaimer Excessivo

**O que é:** Claude começa a adicionar ressalvas e alternativas sobre coisas que já foram decididas e fixadas.

**Exemplos concretos:**
- Decidido: usar FastAPI. Claude depois: "Você poderia usar FastAPI, Flask ou Django, dependendo do que preferir"
- Decidido: banco PostgreSQL. Claude depois: "Considerando que você talvez queira usar PostgreSQL ou MySQL..."

**Atenção:** distinguir de casos legítimos onde Claude genuinamente tem nova informação relevante.

**Como detectar:** o disclaimer refere-se a algo já decidido E não há nova informação que justifique reabrir.

**Ação:** registrar internamente. Se ocorrer 2x seguidas → evacuação.

---

### 3e — Perda de Memória de Fase

**O que é:** Claude não reconhece que uma fase foi concluída e tenta refazer trabalho já feito.

**Exemplos:**
- "Vamos começar definindo a estrutura do banco" — banco já foi definido e implementado
- "Podemos criar o endpoint de login" — endpoint já foi criado e testado

**Como detectar:** proposta de ação contradiz o estado de progresso estabelecido.

**Ação:** evacuação imediata (equivale a Nível 1).

---

## Nível 4 — PREVENTIVO (Checkpoint Proativo)

Risco aumentado, degradação não confirmada.

| Sinal | Threshold |
|-------|-----------|
| Volume de turnos | 30+: oferecer / 50+: obrigatório |
| Conclusão de fase importante | Bom momento para checkpoint |
| Mudança para área nova e densa | Antes de iniciar |
| 8+ decisões sem checkpoint | Independente de turnos |

---

## Sinais do Usuário (Qualquer Nível → Evacuação Imediata)

**Memória:**
`"você esqueceu que..."` · `"já te falei isso"` · `"como disse antes..."` · `"lembra que..."`

**Pedido explícito:**
`"compile tudo"` · `"resuma o que fizemos"` · `"quero um relatório"` · `"gera o contexto"`
`"vou abrir nova conversa"` · `"nova sessão"` · `"preciso transferir isso"`

**Frustração:**
`"está perdendo o fio"` · `"contexto corrompido"` · `"não está lembrando"` · `"começou a errar"`

---

## Falsos Positivos — Quando NÃO Evacuar

| Situação | Por Que Não É Degradação |
|----------|--------------------------|
| Claude pede esclarecimento sobre ambiguidade | Cautela, não amnésia |
| Usuário muda de assunto voluntariamente | Escolha, não perda |
| Claude sugere alternativa com justificativa nova | Sugestão válida, não confusão |
| Conversa longa mas coesa e sem erros | Longa ≠ degradada |
| Claude simplifica a pedido do usuário | Resposta ao pedido, não regressão |

---

## Checklist de Autoavaliação (executar em todo checkpoint)

```
□ Sei o objetivo principal sem hesitar?
□ Consigo listar as 3 decisões mais recentes?
□ Sei exatamente o que estava sendo feito antes deste turno?
□ Minhas respostas mantêm o nível de especificidade das anteriores?
□ Estou usando as convenções estabelecidas no início (nomes, estilo, padrões)?
□ Há contradição entre o que vou dizer e algo dito antes?
□ Estou prestes a perguntar algo que já foi respondido?
```

**0 falhas** → checkpoint verde, continuar.
**1+ falha** → evacuação imediata.
