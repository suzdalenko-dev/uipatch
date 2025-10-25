import pyautogui, time

def click_buscar():
    print("[INFO] Buscando campo 'Buscar...' en pantalla...")
    buscar_icon = None

    # 🔍 Intentar localizar el campo Buscar
    for _ in range(10):  # intenta 10 veces
        buscar_icon = pyautogui.locateCenterOnScreen("img/buscar.png", confidence=0.8)
        if buscar_icon:
            break
        time.sleep(0.5)

    # ✅ Si lo encuentra, hace clic e inserta texto
    if buscar_icon:
        pyautogui.click(buscar_icon)
        print(f"[OK] Campo 'Buscar' clicado en posición {buscar_icon}")

        # Espera breve antes de escribir
        time.sleep(0.5)

        # ✍️ Escribir el texto "Clasificación Art"
        pyautogui.typewrite("Clasificacion Art", interval=0.1)
        print("[OK] Texto 'Clasificacion Art' escrito correctamente.")

        # (Opcional) Presionar Enter para confirmar la búsqueda
        pyautogui.press("enter")
        print("[INFO] Enter presionado para confirmar búsqueda.")

    else:
        print("[ERROR] No se encontró el campo 'Buscar' en pantalla.")