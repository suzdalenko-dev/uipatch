import subprocess
import time
import os
import psutil   # opcional, sólo si quieres comprobar el arranque (pip install psutil)

def start_libra(exe_path, args_str, working_dir=None, wait_seconds=0):
    """
    Inicia el ejecutable con sus argumentos (equivalente a Start Process en UiPath).
    - exe_path: ruta completa al .exe (ej. r"C:\Program Files\Libra\Libra.exe")
    - args_str: cadena con los argumentos (ej. "-url https://... -t 60000 ...")
    - working_dir: carpeta de trabajo (opcional)
    - wait_seconds: seconds to wait after starting (opcional)
    Devuelve el objeto subprocess.Popen.
    """
    # Prepara la lista de argumentos. Simple split funciona en este caso.
    # Si tus argumentos llevan comillas complejas, usar shlex.split(..., posix=False)
    import shlex
    try:
        args_list = shlex.split(args_str, posix=False)
    except Exception:
        args_list = args_str.split()

    cmd = [exe_path] + args_list

    print(f"[INFO] Ejecutando: {cmd}")
    print(f"[INFO] Working dir: {working_dir or os.path.dirname(exe_path)}")

    # Lanza el proceso
    proc = subprocess.Popen(cmd, cwd=working_dir or os.path.dirname(exe_path), shell=False)

    if wait_seconds and wait_seconds > 0:
        print(f"[INFO] Esperando {wait_seconds} segundos para que la app arranque...")
        time.sleep(wait_seconds)

    # Opcional: comprobar con psutil que el proceso está vivo
    try:
        p = psutil.Process(proc.pid)
        print(f"[OK] Proceso lanzado PID={proc.pid}, name={p.name()}")
    except Exception:
        print(f"[WARN] Proceso lanzado PID={proc.pid} (psutil no disponible o info no accesible)")

    return proc


# -------------------------
# EJEMPLO de uso integrado
# -------------------------

def libra_start():
    EXE = r"C:\Program Files\Libra\Libra.exe"
    ARGS = r'-url https://libra.froxadom.local:443/forms/frmservlet?config=libra_saa -t 60000 -wlv 12.2.1.19.0 -idcrm BYPFC0CH7I -fs S -ww 0 -wh 0 -dpi 0'
    WORKDIR = r"C:\Program Files\Libra"   # normalmente "Iniciar en" del acceso directo

    # ejemplo: matar procesos anteriores (usa la función kill_process si la tienes)
    # from previous snippet: kill_process("Libra")

    # espera (delay) 2 segundos si lo necesitas
    time.sleep(2)

    # iniciar Libra
    proc = start_libra(EXE, ARGS, working_dir=WORKDIR, wait_seconds=5)

    # proc es el Popen; si quieres más adelante comprobar si sigue vivo:
    alive = proc.poll() is None
    print(f"[INFO] Libra sigue vivo? {alive}")
