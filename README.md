# 🛡️ Context Guardian

Skill para Claude.ai que monitora e protege o contexto em conversas longas — detectando degradação, compilando um relatório `.md` completo e gerando um **Prompt de Retomada** para continuidade sem perda de informação.

---

## O problema

Conversas longas no Claude degradam silenciosamente. O modelo começa a esquecer decisões, repetir perguntas já respondidas, contradizer abordagens estabelecidas e dar respostas genéricas que ignoram o contexto acumulado. Quando você percebe, informação crítica já se perdeu.

## A solução

O Context Guardian opera em dois modos complementares:

```
🛡️ MODO SENTINELA              ⚠️ MODO EVACUAÇÃO
──────────────────              ─────────────────────
Ativo desde o início            Disparo automático ou manual
Registra fatos-âncora           Varre toda a conversa
Checkpoint a cada 20 turnos     Gera relatório .md completo
Evacua ao detectar degradação   Gera Prompt de Retomada pronto
```

O **Modo Sentinela** resolve o paradoxo central: uma skill só é consultada se Claude reconhece que precisa dela — mas com contexto degradado, Claude pode não reconhecer os próprios sinais. O Sentinela ativa o monitoramento quando Claude ainda tem contexto pleno, antes de qualquer degradação.

---

## Instalação

1. Acesse a [última release](https://github.com/brunoflma/context-guardian/releases/latest) e baixe o arquivo `context-guardian-vX.X.X.zip`
2. Extraia o zip
3. No Claude.ai: **avatar → Configurações → Skills → Instalar Skill**
4. Selecione a pasta `context-guardian` extraída

---

## Comandos de ativação

### Modo Sentinela (usar no início da conversa)

```
ativar context guardian    context guardian on    /cg
ativar sentinela           iniciar monitoramento   cg on
monitorar contexto         proteção de contexto
```

### Modo Evacuação (manual ou automático)

```
compile tudo       gerar relatório       /evacuar
nova conversa      transferir conversa   checkpoint agora
o que discutimos   contexto perdido      você esqueceu
```

O Modo Evacuação também dispara automaticamente quando Claude detecta que está incerto sobre algo já estabelecido, quando repete conteúdo já coberto ou quando a conversa ultrapassa 50 turnos sem checkpoint.

---

## O que a evacuação gera

**1. Arquivo `.md`** — relatório completo para download com stack técnica, decisões cronológicas, código produzido, tentativas fracassadas e estado exato no momento da evacuação.

**2. Prompt de Retomada** — bloco pronto para colar na nova conversa com o ponto exato de parada e a primeira ação imperativa para o novo agente. Funciona com ou sem o arquivo `.md`.

---

## Automação total (fora do Claude.ai)

No Claude.ai o último passo é sempre manual (3 cliques). Em outros ambientes a transferência é completamente automática:

| Ambiente | Automação |
|---|---|
| Claude.ai | Semi-automático — skill gera tudo, usuário abre nova conversa |
| Python / Node.js | ✅ Total — orquestrador monitora tokens e transfere |
| Claude Code | ✅ Total — subagentes nativos, invisível ao usuário |
| n8n | ✅ Total — fluxo visual sem código |

---

Desenvolvido por **Bruno Ferreira** — 2026
