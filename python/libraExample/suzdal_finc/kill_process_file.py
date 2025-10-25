import psutil

def kill_process(process_name: str):
    """Mata todos los procesos que coincidan con el nombre indicado (como UiPath Kill Process)."""
    killed = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower().startswith(process_name.lower()):
                proc.kill()
                killed.append(proc.info['pid'])
                print(f"[INFO] Proceso '{proc.info['name']}' (PID {proc.info['pid']}) terminado.")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if killed:
        print(f"[OK] Se han cerrado {len(killed)} proceso(s) de '{process_name}'.")
    else:
        print(f"[INFO] No se encontraron procesos con el nombre '{process_name}'.")

