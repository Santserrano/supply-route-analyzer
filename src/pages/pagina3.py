from panda.ui import PandaPage
from panda.auth import role_required, current_user

class Page(PandaPage):
    @role_required("admin")
    
    def setup(self):
        self.label(f"Bienvenido, {current_user().username}")
        self.label("Página 3", size=24)

        self.label("Comience a construir su interfaz aquí.", size=12)
            
        self.button("Ir a Página 1", link="pagina1")