from panda.ui import PandaPage

class Page(PandaPage):
    def setup(self):
        # Crear una barra de navegación
        # Nombre de la etiqueta -> Redirección al presionar
        self.navbar([
            ("Inicio", "pagina1"),
            ("Sobre Nosotros", "pagina2"),
            ("Contacto", "pagina3")
        ])

        # Contenido de la página
        self.label("Bienvenido a la página principal", size=24)
        self.button("Ir a Página 2", link="pagina2")
        self.button("Ir a Página 3", link="pagina3")
        self.input("Introduce tu nombre")
        self.checkbox("Aceptar términos y condiciones")
        self.option_menu(["Opción 1", "Opción 2", "Opción 3"])

        # Grid Layout con 3 elementos
        self.grid_layout(3, [
            self.label("Logo", size=16),
            self.label("Texto descriptivo", size=16),
            self.button("Click aquí", link="pagina3")
        ])
        