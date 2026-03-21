## v1.3.0
- Correção arquitetônica: checkpoints manuais periódicos promovidos a camada primária de proteção — a skill agora comunica isso claramente ao usuário na ativação
- Intervalo de checkpoint definido pelo usuário: Claude pergunta o intervalo na ativação ("a cada quantos turnos?") em vez de usar 20 fixos; recomendado 10 para sessões técnicas densas
- Lembrete de checkpoint ativo: Claude emite alerta no chat a cada N turnos respondidos com opção de confirmar ("ok") ou evacuar; não bloqueia o fluxo se ignorado
- Limitações documentadas honestamente na skill: sem detecção contínua em background, sem acesso a tokens no Claude.ai, detecção automática de fase como complemento e não garantia
- Detecção automática de fase mantida como melhor esforço com eventos explícitos (conclusão declarada, decisão arquitetural grande, 8+ decisões acumuladas)
- Checklist interna expandida com verificação de especificidade e uso de convenções
- Modo silencioso com aviso: usuário informado que responsabilidade de checkpoint manual recai sobre ele nesse modo
- Resposta de ativação atualizada: lista o que é garantido vs. melhor esforço

## v1.1.0
- Checkpoint por fase: Claude detecta viradas de fase (conclusão de módulo, decisão arquitetural grande, mudança de assunto, início de área de risco) e faz checkpoint nesses momentos — não apenas a cada 20 turnos
- Detecção semântica de degradação: 5 novos sinais graduais documentados (genericidade crescente, perda de convenções, qualidade regressiva, disclaimer excessivo, perda de memória de fase) com exemplos concretos e ação para cada um
- Modo silencioso: ativar com "modo silencioso" / "cg silent" — checkpoints acontecem internamente sem mensagem no chat; Claude só fala ao detectar problema ou a pedido explícito
- Prompt de Retomada em dois formatos: Completo (todas as seções, para conversas técnicas e longas) e Compacto (~150 palavras, para retomadas rápidas e conversas estratégicas/criativas)
- Perfis de conversa: Claude detecta automaticamente o perfil na ativação (Técnico, Estratégico, Criativo, Geral) e adapta o relatório priorizando as seções mais relevantes; forçar manualmente com "perfil técnico" etc.
- Integração com memória do Claude: durante a evacuação, preferências recorrentes do usuário (stack, estilo de código, idioma, formato de resposta, contexto profissional) são salvas via memory_user_edits e ficam disponíveis automaticamente em futuras conversas
- 4 templates de relatório .md especializados por perfil (Técnico, Estratégico, Criativo, Geral)
- Resposta de ativação atualizada: inclui perfil detectado e lista os 6 mecanismos ativos

## v1.0.0
- Modo Sentinela: monitoramento proativo ativado no início da conversa com registro de fatos-âncora e varredura automática a cada 20 turnos
- Modo Evacuação: varredura completa da conversa ao detectar degradação, com geração obrigatória de arquivo .md via create_file + present_files
- Prompt de Retomada: bloco auto-suficiente gerado na evacuação com ponto exato de parada e primeira ação imperativa para o novo agente
- 10+ comandos de ativação em PT-BR e inglês, incluindo atalhos /cg e /evacuar
- Detecção automática por sinais internos (incerteza, repetição, contradição) e por gatilhos textuais do usuário
- Evacuação automática após 50 turnos sem checkpoint registrado
- Orquestrador Python completo com loop de chat, estimativa de tokens e reinício transparente de sessão
- Orquestrador Node.js/TypeScript equivalente ao Python
- Sistema de subagentes para Claude Code com transferência invisível ao usuário
- Fluxo n8n com JSON importável para automação visual sem código
- Template de relatório .md com 8 seções estruturadas e Prompt de Retomada integrado
- Taxonomia de sinais de degradação em 3 níveis: crítico, moderado e preventivo
- release.py com validação de zip por allowlist, changelog compilado por faixa de versões e upload automático via API do GitHub
