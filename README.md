# 🛡️ Context Guardian

Habilidade para Claude.ai que monitora e protege o contexto em conversas longas — detectando degradação, compilando um relatório `.md` completo e gerando Prompts de Retomada para continuidade sem perda de informação.

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
4. Perfis de conversa especializados (Técnico, Jurídico, Estratégico, Criativo, Médico/Científico, Educacional, Investigativo, Geral)
5. Modo silencioso sem ruído no fluxo de trabalho
6. Integração com a memória do Claude para preferências recorrentes

---

## Instalação

### Pré-requisito obrigatório

Antes de instalar, certifique-se de que **Code Execution** está ativado:

> **Configurações → Capacidades → ativar "Execução de código e criação de arquivos"**

Sem essa opção ativada, a Habilidade não carrega, mesmo que o upload seja feito corretamente.

### Passos

1. Acesse a [última release](https://github.com/brunoflma/context-guardian/releases/latest) e baixe o arquivo `context-guardian-vX.X.X.zip`
2. No Claude.ai: **avatar → Personalizar → Habilidades → Fazer upload de uma habilidade (Botão +)**
3. Faça upload do arquivo `.zip` baixado (não é necessário extrair)
4. Ative o toggle ao lado da Habilidade na lista

> **Atenção:** o `.zip` de instalação é o arquivo `context-guardian-vX.X.X.zip` disponível nos assets da release — não o arquivo do repositório baixado via "Download ZIP" do GitHub.

### ⚠️ Limitação importante: conversas em andamento

A Habilidade é injetada no contexto **apenas na inicialização de uma conversa nova**. Em conversas já em andamento, o Claude não reconhece a Habilidade mesmo que ela esteja instalada.

**Workaround para conversas em andamento:** cole o conteúdo do `SKILL.md` diretamente no chat como mensagem e peça ao Claude para ativar o modo desejado.

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

**Arquivo `.md`** com relatório adaptado ao perfil da conversa, cobrindo decisões cronológicas, artefatos produzidos, tentativas fracassadas e estado exato no momento da evacuação.

**Perfis suportados:** Técnico · Jurídico · Estratégico · Criativo · Médico/Científico · Educacional · Investigativo · Geral

**Prompt Completo** — todas as seções, para conversas técnicas, jurídicas e longas.

**Prompt Compacto** — ~150 palavras, para retomadas rápidas.

**Memória do Claude** — preferências recorrentes (área de atuação, estilo de resposta, idioma, formato) salvas automaticamente para futuras conversas.

---

## Automação total (fora do Claude.ai)

| Ambiente | Automação |
|---|---|
| Claude.ai | Semi-automático — Habilidade gera tudo, usuário abre nova conversa |
| Python / Node.js | ✅ Total — orquestrador monitora tokens e transfere |
| Claude Code | ✅ Total — subagentes nativos, invisível ao usuário |
| n8n | ✅ Total — fluxo visual sem código |

---

Desenvolvido por **Bruno Ferreira** — 2026
