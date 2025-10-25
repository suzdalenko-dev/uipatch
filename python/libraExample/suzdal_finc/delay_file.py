import time

def delay(seconds: float):
    """Simula la actividad Delay de UiPath en segundos."""
    print(f"[INFO] Esperando {seconds} segundos...")
    time.sleep(seconds)
    print("[OK] Continuando ejecución...")