import pyautogui
import time
import os

def click_por_imagen(nombre_imagen, carpeta="img", intentos=10, confianza=0.8, pausa=0.5):
    """
    Busca una imagen en pantalla y hace clic en su posición central.

    Parámetros:
      nombre_imagen : str → nombre del archivo (por ejemplo 'clasificacion_articulos.png')
      carpeta       : str → carpeta donde se guarda la imagen
      intentos      : int → número de reintentos antes de fallar
      confianza     : float → valor entre 0 y 1 para comparar similitud
      pausa         : float → segundos entre intentos
    """
    ruta_imagen = os.path.join(carpeta, nombre_imagen)

    print(f"[INFO] Buscando imagen '{nombre_imagen}' en pantalla...")
    posicion = None

    for intento in range(intentos):
        posicion = pyautogui.locateCenterOnScreen(ruta_imagen, confidence=confianza)
        if posicion:
            break
        time.sleep(pausa)

    if posicion:
        pyautogui.click(posicion)
        print(f"[OK] Click realizado sobre '{nombre_imagen}' en posición {posicion}")
        return True
    else:
        print(f"[ERROR] No se encontró la imagen '{nombre_imagen}' tras {intentos} intentos.")
        return False