import pyautogui
import time

def scroll_tabla_linea_a_linea(lineas=100):
    """
    Hace scroll línea a línea en una tabla (usando tecla ↓).
    """
    print(f"[INFO] Desplazando {lineas} líneas hacia abajo...")
    for i in range(lineas):
        pyautogui.press("down")
        time.sleep(0.05)  # pequeño retardo entre líneas
    print("[OK] Fin del desplazamiento.")