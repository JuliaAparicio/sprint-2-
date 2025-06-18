from datetime import datetime
import pytz
import time

# Dicionário de cargas
cargas = {
    "Geladeira": {"essencial": True, "estado": "OFF"},
    "Wi-Fi": {"essencial": True, "estado": "OFF"},
    "Televisão": {"essencial": False, "estado": "OFF"},
    "Máquina de Lavar": {"essencial": False, "estado": "OFF"}
}

# Economia estimada por carga não essencial desligada
economia_Watts = {
    "Televisão": 120,
    "Máquina de Lavar": 500
}

def obter_hora_atual():
    """Retorna a hora atual com fuso horário do Brasil (São Paulo)."""
    fuso_br = pytz.timezone('America/Sao_Paulo')
    return datetime.now(fuso_br)

def hora_pico(hora):
    """Verifica se o horário está entre 17:30 e 20:30."""
    hora_formatada = int(hora.strftime("%H%M"))
    return 1730 <= hora_formatada <= 2030

def processar_logica(hora_atual):
    """Aplica lógica de desligamento com base no horário de pico."""
    pico = hora_pico(hora_atual)
    economia_total = 0

    for nome, dados in cargas.items():
        if pico and not dados["essencial"]:
            dados["estado"] = "OFF"
            economia_total += economia_Watts.get(nome, 0)
        else:
            dados["estado"] = "ON"

    return economia_total

def exibir_dashboard(hora_atual, economia_total):
    """Exibe status no console."""
    print("\n" + "=" * 60)
    print(f"⏰ Hora atual (Brasil): {hora_atual.strftime('%H:%M:%S')}")
    print("🔌 Estado das Cargas:")
    for nome, dados in cargas.items():
        tipo = "Essencial" if dados["essencial"] else "Não Essencial"
        print(f"  - {nome:<20} | Tipo: {tipo:<15} | Estado: {dados['estado']}")
    print(f"💡 Economia estimada: {economia_total} Wh")
    print("=" * 60)

def executar_monitoramento():
    try:
        while True:
            hora_atual = obter_hora_atual()
            economia = processar_logica(hora_atual)
            exibir_dashboard(hora_atual, economia)
            time.sleep(3) # atualiza a cada 3 seg.
    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")

# Inicia o monitoramento
executar_monitoramento()

