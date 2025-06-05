import os
import importlib
import customtkinter as ctk
import sys
from panda.auth.auth import AuthPage

class App(ctk.CTk):
    def __init__(self, pages_dir=None, role_to_page=None):
        super().__init__()

        self.title("Panda App")
        self.geometry("900x600")

        window_width = 900
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2 - 50

        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Ajustar el path para la estructura real
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.root_dir = os.path.dirname(self.base_dir)
        if self.root_dir not in sys.path:
            sys.path.append(self.root_dir)

        # Directorio real de las páginas
        if pages_dir is None:
            self.pages_dir = os.path.join(self.root_dir, "src", "pages")
        else:
            self.pages_dir = pages_dir

        self.pages = {} 
        self.current_page = None
        self.role_to_page = role_to_page or {}

        self.load_pages()
        self.show_login()

    def show_login(self):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = AuthPage(self, role_to_page=self.role_to_page)
        self.current_page.pack(fill="both", expand=True)

    def load_pages(self):
        """Carga y registra las páginas dinámicamente"""
        if not os.path.exists(self.pages_dir):
            print(f"El directorio de páginas no existe: {self.pages_dir}")
            return

        for file in os.listdir(self.pages_dir):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = f"src.pages.{file[:-3]}"  # src.pages.pagina1, etc.
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, "Page"): 
                        self.pages[file[:-3]] = module.Page
                        print(f"Página cargada: {module_name}")
                except Exception as e:
                    print(f"Error al cargar la página {module_name}: {str(e)}")

    def link(self, page_name):
        """Renderiza dinámicamente la página seleccionada"""
        if page_name in self.pages:
            if self.current_page:
                self.current_page.destroy()

            self.current_page = self.pages[page_name](self)
            self.current_page.pack(fill="both", expand=True)
        else:
            print(f"Página '{page_name}' no encontrada.")