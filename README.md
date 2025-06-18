## Objetivo:
Desenvolver um sistema automatizado de gerenciamento de energia solar residencial, com foco na priorização de cargas essenciais durante o horário de pico da concessionária (17h30 às 20h30), otimizando o consumo energético e promovendo economia.

## Funcionalidades:
- Detecção automática de horário de pico
- Priorização manual e/ou automática de cargas
- Ciclo de atualização autônoma a cada 3 segundos
- Emissão de alertas via console e dashboard
- Visualização em tempo real do status dos dispositivos e economia gerada

## Arquitetura do sistema:
# - Codigo em python:
1. Entrada de Dados:
  • Fonte: Relógio do sistema operacional (RTC interno,via biblioteca datetime com fuso horário pytz)
  • Dados obtidos: Horário atual (formato HH:MM)

2. Processamento
  • Verificação de faixa horária crítica: 17:30 ≤ horaAtual ≤ 20:30
  • Classificação de cargas:
    Essenciais: Geladeira, Wi-Fi
    Não essenciais: Televisão, Máquina de Lavar

Lógica de decisão:
  • Durante o horário de pico: desligamento automático de cargas não essenciais
  • Fora do pico: ativação de todas as cargas

3. Saída e Monitoramento:
  • Interface de visualização (console ou dashboard):
  • Status de cada carga (ON/OFF)
  • Horário atual (Fuso BR)
  • Economia estimada de energia (Wh)

# - Simulação TinkerCad:
 1. Entrada de Dados
  • Variável simulada: horaAtual no formato inteiro (e.g. 1830 para 18h30)

 2. Lógica de Processamento (Simulação de Automação)
  • Função estaNoHorarioDePico() para validar faixa de horário
  • Classificação de cargas:
      Essenciais: Geladeira, Wi-Fi
      Não essenciais: TV, Máquina de lavar
  • Ações de controle:
      Se horaAtual ∈ [1730, 2030]: manter apenas cargas essenciais ativadas
      Caso contrário: todas as cargas são ativadas	

3. Saída / Monitoramento
   • Monitor Serial (via Arduino IDE):
   • Indicação se o sistema está operando em modo de economia	
   • Listagem das cargas ativas no momento	
   • Atualização a cada 3 segundos	

 # - Codigo Arduino:
 1. Entrada de Dados
   • Variável fixa: horaAtual = 1830 (pode ser substituída por módulo RTC no futuro)
    
2. Lógica de Processamento (Código C/C++)
   • Função estaNoHorarioDePico(int hora)
        Retorna true se hora ∈ [1730, 2030]
   • Controle de saídas digitais:
	ligarCargasEssenciais(): ativa pinos 2 (geladeira) e 3 (Wi-Fi)
        ligarTodasAsCargas(): ativa todos os pinos (2 a 5)

3. Saída / Monitoramento
    • Saída via Serial.println:
        Exibição de mensagens como:
        "Horário de pico: desligando cargas não essenciais"
        "Fora do pico: todas as cargas ligadas"

    • Estado dos dispositivos (simulados com LEDs):
       HIGH: dispositivo ativo
       LOW: dispositivo desativado
