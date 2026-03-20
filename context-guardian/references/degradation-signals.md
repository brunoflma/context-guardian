# Taxonomia de Sinais de Degradação

---

## Nível 1 — CRÍTICO (Evacuação Imediata)

Estes sinais indicam que informação já foi perdida. Não há "verificação" — evacuar agora.

| Sinal | Exemplo Concreto |
|-------|-----------------|
| Claude pergunta algo já respondido | "Qual linguagem você está usando?" — já foi dito no turno 3 |
| Claude contradiz decisão anterior | Após decidir usar REST, sugere implementar GraphQL |
| Claude ignora restrição estabelecida | Usa TypeScript após usuário dizer "sem TypeScript" |
| Claude re-propõe alternativa rejeitada | Sugere Redis após usuário ter descartado Redis |
| Claude descreve código já produzido como "vamos criar" | Arquivo já foi gerado na conversa |

**Ação:** Anunciar evacuação imediatamente. Não fazer mais nada antes do relatório.

---

## Nível 2 — ALTO (Evacuação Recomendada)

Sinais de que degradação está ocorrendo ativamente.

| Sinal | Como Reconhecer |
|-------|----------------|
| Incerteza interna sobre fato estabelecido | Claude internamente não tem certeza se o projeto usa PostgreSQL ou MySQL — mas isso foi definido |
| Respostas ficam progressivamente genéricas | Código gerado não usa as convenções estabelecidas sem motivo |
| Usuário corrigiu Claude 2x sobre o mesmo ponto | Repetição do mesmo erro após correção |
| Claude adiciona disclaimers sobre coisas já decididas | "Você poderia usar X ou Y" — quando X já foi escolhido |

**Ação:** Executar checklist do Modo Sentinela. Se qualquer item falhar → Evacuação.

---

## Nível 3 — MODERADO (Checkpoint Preventivo)

Sinais de risco aumentado, não de degradação confirmada.

| Sinal | Threshold |
|-------|-----------|
| Volume de turnos | 30+ turnos: oferecer checkpoint / 50+ turnos: checkpoint obrigatório |
| Fase concluída | Ao terminar um módulo/feature — bom momento para checkpoint |
| Mudança de tópico complexo | Antes de entrar em área nova e densa |
| Acúmulo de decisões | 10+ decisões sem checkpoint registrado |

**Ação:** Oferecer checkpoint proativamente. "Ótimo momento para um checkpoint — quer que eu gere agora?"

---

## Sinais do Usuário (Qualquer Nível)

Qualquer frase do usuário nestas categorias → Evacuação imediata, sem análise adicional.

**Memória:**
- "você esqueceu que..."
- "já te falei isso"
- "como disse antes..."
- "lembra que..."

**Pedido explícito:**
- "compile tudo", "resuma o que fizemos"
- "quero um relatório", "gera o contexto"
- "vou abrir nova conversa", "nova sessão"
- "preciso transferir isso"

**Frustração com contexto:**
- "está perdendo o fio"
- "contexto corrompido", "contexto perdido"
- "não está lembrando"
- "começou a errar"

---

## Falsos Positivos — Quando NÃO evacuar

| Situação | Por Que Não É Degradação |
|----------|--------------------------|
| Claude pede esclarecimento sobre ambiguidade | Cautela, não amnésia |
| Usuário muda de assunto voluntariamente | Escolha, não perda |
| Claude sugere alternativa a abordagem escolhida | Sugestão, não contradição — mas verificar tom |
| Conversa longa mas coesa, sem erros | Longa ≠ degradada |
| Claude faz pergunta de confirmação antes de agir | Boa prática, não falha |

---

## Autoavaliação do Modo Sentinela (checklist a cada 20 turnos)

```
□ Sei o nome/objetivo do projeto sem hesitar?
□ Consigo listar as 3 decisões mais recentes?
□ Sei exatamente o que estava sendo feito antes deste turno?
□ Conheço as restrições técnicas principais?
□ Há contradição entre o que vou dizer e algo dito antes?
□ Estou prestes a perguntar algo que já foi respondido?
```

**0 falhas** → Checkpoint verde, continuar.  
**1+ falha** → Evacuação imediata.
