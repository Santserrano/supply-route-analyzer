import sys
import os

def add_project_root_to_path():
    """Enrutado path carpeta raiz"""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    print(f"DEBUG: Agregando {project_root} a sys.path") # DEBUG ruta
    print(os.path.abspath(os.path.dirname(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
