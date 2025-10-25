from java_access_bridge_wrapper import AccessBridgeWrapper
import time

# Inicializar el bridge
bridge = AccessBridgeWrapper()

print("[INFO] Buscando ventanas Java activas...")
windows = bridge.get_windows()
for i, w in enumerate(windows):
    print(f"{i}: {w.title}")

# Buscar ventana Libra
libra_window = None
for w in windows:
    if "LIBRA" in w.title.upper():
        libra_window = w
        break

if not libra_window:
    print("[ERROR] No se encontró ventana Java de LIBRA.")
    exit(1)

print(f"[OK] Ventana detectada: {libra_window.title}")

# Listar elementos accesibles
print("\n[INFO] Explorando elementos de la ventana...")
root = libra_window.get_accessible_context()
print(f"Root: {root.get_accessible_name()} ({root.get_accessible_role()})")

def explore(node, level=0):
    try:
        name = node.get_accessible_name()
        role = node.get_accessible_role()
        print("  " * level + f"- {role}: {name}")
        for child in node.get_accessible_children():
            explore(child, level + 1)
    except Exception as e:
        pass

explore(root)

print("\n[INFO] Fin de exploración.")
