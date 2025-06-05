from panda.ui import PandaPage
from panda.auth import login_required, current_user

class Page(PandaPage):
    @login_required
    
    def setup(self):
        self.label(f"Hola, {current_user().username}")
        self.label("Bienvenido a Página 2", size=24)
        
        self.label("Comience a construir su interfaz aquí.", size=12)

        self.button("Ir a Página 3", link="pagina3")
        self.button("Ir a ops", link="ops")
