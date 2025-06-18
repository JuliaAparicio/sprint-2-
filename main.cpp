// Pinos das cargas
const int PIN_GELADEIRA = 2;
const int PIN_WIFI = 3;
const int PIN_TV = 4;
const int PIN_MAQUINA = 5;

// Simulação de horário atual (HHMM)
int horaAtual = 1830;

void setup() {
  pinMode(PIN_GELADEIRA, OUTPUT);
  pinMode(PIN_WIFI, OUTPUT);
  pinMode(PIN_TV, OUTPUT);
  pinMode(PIN_MAQUINA, OUTPUT);

  Serial.begin(9600);
  Serial.println("Sistema iniciado em modo automático.");
}

void loop() {
  if (estaNoHorarioDePico(horaAtual)) {
    Serial.println("Horário de pico: desligando cargas não essenciais");
    ligarCargasEssenciais();
  } else {
    Serial.println("Fora do pico: todas as cargas ligadas");
    ligarTodasAsCargas();
  }

  delay(3000); // Aguarda 3 segundos antes de repetir
}

// Verifica se estamos no horário de pico
bool estaNoHorarioDePico(int hora) {
  return (hora >= 1730 && hora <= 2030);
}

// Liga apenas cargas essenciais
void ligarCargasEssenciais() {
  digitalWrite(PIN_GELADEIRA, HIGH);
  digitalWrite(PIN_WIFI, HIGH);
  digitalWrite(PIN_TV, LOW);
  digitalWrite(PIN_MAQUINA, LOW);
}

// Liga todas as cargas
void ligarTodasAsCargas() {
  digitalWrite(PIN_GELADEIRA, HIGH);
  digitalWrite(PIN_WIFI, HIGH);
  digitalWrite(PIN_TV, HIGH);
  digitalWrite(PIN_MAQUINA, HIGH);
}