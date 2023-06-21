import time

def cronometro():
    segundos = 0
    while True:
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        print(f"{minutos:02d}:{segundos_restantes:02d}")
        time.sleep(1)
        segundos += 1  # Incremento corrigido dos segundos

cronometro()