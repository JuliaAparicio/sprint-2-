## Objetivo:
Automatizar o uso de energia solar em uma residencia, priorizando cargas essenciais durante o horário de pico de energia (17h30 às 20h30). Ligado a assistente virtual

## Funcionalidades:
- Detectação do horário de pico
- Priorização manual e/ou automática da priorização de equipamentos
- Simulação da energia solar e tensão da bateria
- Visualização de alertas no console/dashoboard

## Arquitetura do sistema:
- Codigo em python:
  1. Entrada de Dados
	•	Sensor de tempo / Relógio do sistema: Verifica o horário atual do sistema.

2. Lógica de Processamento (Script Python)
	•	Verifica se o horário atual está entre 17:30 e 20:30 (período de pico).
	•	Identifica os dispositivos conectados e classificados em:
	•	Prioritários
	•	Não prioritários
	•	Aplica a lógica:
	•	Se horário estiver dentro do pico, então:
	•	Desligar todos os dispositivos classificados como não prioritários (sejam eles de base ou cadastrados pelo usuário).
	•	Manter ligados somente os dispositivos prioritários.
	•	Se fora do horário de pico, todos os dispositivos funcionam normalmente.

3. Saída / Monitoramento
	•	Painel de visualização:
	•	Exibe status de dispositivos (ligado/desligado).
	•	Indica horário atual.
	•	Mostra economia estimada durante o período de restrição.

- Simulação TinkerCad:
  1.

## Video:


## Tecnologias utilizadas:


