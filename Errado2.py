import time

def cronometro():
    segundos = 0
    while True:
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        print(f"{minutos:02d}:{segundos_restantes:02d}")
        time.sleep(1)
        # O erro está aqui: não há incremento de segundos
        
cronometro()