import os
import sys
import time
import subprocess

def main():
    print("\n🚀 Compilando proyecto Panda v1.0...")
    print("\n🔑 Panda Auth - Generando credenciales...")
    print("\n🌐 Base de datos creada - SQLite")
    start_time = time.time()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    main_path = os.path.join(project_root, "src", "main.py")

    process = subprocess.Popen(["python", main_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if stdout:
        print(stdout.decode(errors='replace'))

    if stderr:
        print(stderr.decode(errors='replace'))

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\n✅ Tiempo de ejecución total: {execution_time:.2f} segundos")

if __name__ == "__main__":
    main()
