from pywinauto import Application
import pyautogui
import time


def input_login():
    # 1️⃣ Conecta a la ventana de Libra
    app = Application(backend="uia").connect(title_re=".*LIBRA EDISA.*")
    dlg = app.window(title_re=".*LIBRA EDISA.*")
    dlg.set_focus()
    dlg.restore()
    print("[INFO] Ventana LIBRA activada.")

    # 2️⃣ Buscar campo 'Usuario'
    print("[INFO] Buscando campo 'Usuario'...")
    usuario_field = None
    for _ in range(10):
        usuario_field = pyautogui.locateCenterOnScreen("img/login_usuario.png", confidence=0.8)
        if usuario_field:
            break
        time.sleep(0.5)

    if not usuario_field:
        print("[ERROR] No se encontró el campo 'Usuario'.")
        return

    pyautogui.click(usuario_field)
    pyautogui.typewrite("alexey", interval=0.1)
    print("[OK] Usuario escrito correctamente.")

    # 3️⃣ Buscar campo 'Clave'
    print("[INFO] Buscando campo 'Clave'...")
    clave_field = None
    for _ in range(10):
        clave_field = pyautogui.locateCenterOnScreen("img/login_clave.png", confidence=0.8)
        if clave_field:
            break
        time.sleep(0.5)

    if not clave_field:
        print("[WARN] No se encontró imagen del campo 'Clave'. Usando Tab para moverse.")
        pyautogui.press("tab")
    else:
        pyautogui.click(clave_field)

    pyautogui.typewrite("", interval=0.1)  # 🔒 tu contraseña real
    print("[OK] Clave escrita correctamente.")

    # 4️⃣ Buscar botón “Acceder”
    print("[INFO] Buscando botón 'Acceder'...")
    acceder_btn = None
    for _ in range(10):
        acceder_btn = pyautogui.locateCenterOnScreen("img/login_acceder.png", confidence=0.8)
        if acceder_btn:
            break
        time.sleep(0.5)

    if acceder_btn:
        pyautogui.click(acceder_btn)
        print("[OK] Click en botón 'Acceder' realizado.")
    else:
        print("[WARN] No se encontró el botón 'Acceder'. Presionando Enter como alternativa.")
        pyautogui.press("enter")

    print("[✅] Login completado correctamente.")





def cerrar_notificaciones():
    """Cierra la ventana de notificaciones si aparece."""
    print("[INFO] Buscando ventana de Notificaciones...")
    puerta_icon = None
    for _ in range(10):
        # Busca la imagen del icono de salida (la puerta)
        puerta_icon = pyautogui.locateCenterOnScreen(r"img\notif_salir.png", confidence=0.8)
        if puerta_icon:
            break
        time.sleep(0.5)

    if puerta_icon:
        pyautogui.click(puerta_icon)
        print("[OK] Ventana de notificaciones cerrada.")
        time.sleep(1)
    else:
        print("[INFO] No se detectó ventana de notificaciones.")



