# 🛡️ Context Guardian

Skill para Claude.ai que monitora e protege o contexto em conversas longas — detectando degradação, compilando um relatório `.md` completo e gerando Prompts de Retomada para continuidade sem perda de informação.

---

## O problema

Conversas longas no Claude degradam silenciosamente. O modelo começa a esquecer decisões, repetir perguntas já respondidas, contradizer abordagens estabelecidas e dar respostas genéricas que ignoram o contexto acumulado. Quando você percebe, informação crítica já se perdeu.

## A solução

O Context Guardian opera em três modos e seis mecanismos de proteção:

```
🛡️ MODO SENTINELA    — monitoramento ativo desde o início
🔇 MODO SILENCIOSO   — checkpoints sem interrupção no chat
⚠️ MODO EVACUAÇÃO    — relatório .md + Prompts de Retomada ao detectar degradação
```

**Seis mecanismos integrados:**
1. Checkpoint por virada de fase (não só por turnos)
2. Detecção semântica de degradação gradual
3. Prompt de Retomada em dois formatos (completo e compacto)
4. Perfis de conversa especializados (Técnico, Estratégico, Criativo, Geral)
5. Modo silencioso sem ruído no fluxo de trabalho
6. Integração com a memória do Claude para preferências recorrentes

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
ativar context guardian    context guardian on    /cg    cg on
ativar sentinela           iniciar monitoramento
monitorar contexto         proteção de contexto
```

### Modo Silencioso

```
modo silencioso    sentinela silencioso    cg silent
```

### Modo Evacuação (manual ou automático)

```
compile tudo       gerar relatório       /evacuar
nova conversa      transferir conversa   checkpoint agora
o que discutimos   contexto perdido      você esqueceu
```

O Modo Evacuação dispara automaticamente quando Claude detecta degradação — incerteza sobre fatos estabelecidos, repetição de conteúdo, contradição de decisões, sinais semânticos graduais — ou quando a conversa ultrapassa 50 turnos sem checkpoint.

---

## O que a evacuação gera

**Arquivo `.md`** com relatório adaptado ao perfil da conversa (Técnico, Estratégico, Criativo ou Geral), cobrindo decisões cronológicas, código produzido, tentativas fracassadas e estado exato no momento da evacuação.

**Prompt Completo** — todas as seções, para conversas técnicas e longas.

**Prompt Compacto** — ~150 palavras, para retomadas rápidas.

**Memória do Claude** — preferências recorrentes (stack, estilo de código, idioma, formato de resposta) salvas automaticamente para futuras conversas.

---

## Automação total (fora do Claude.ai)

| Ambiente | Automação |
|---|---|
| Claude.ai | Semi-automático — skill gera tudo, usuário abre nova conversa |
| Python / Node.js | ✅ Total — orquestrador monitora tokens e transfere |
| Claude Code | ✅ Total — subagentes nativos, invisível ao usuário |
| n8n | ✅ Total — fluxo visual sem código |

---

Desenvolvido por **Bruno Ferreira** — 2026
