from panda.ui import PandaPage

"""
¡¡¡ATENCIÓN!!!

Esta ventana es una guía para visualizar la síntaxis (estructura) de las
etiquetas en Panda y los recursos que este framework le proporciona.

La ventana "ejemplos.py" no es enrutada en la compilación.
Para ejecutarla manualmente corra el siguiente comando en terminal "python src/pages/ejemplo.py"

"""

class Page(PandaPage): # Directiva imprescindible para ventanas
    def setup(self): # Inicializador - Configuración de ventana

        """Crea una barra de navegación en la parte superior con botones distribuidos en columnas."""
        # Nombre de la etiqueta -->> Redirección al presionar
        self.navbar([
            ("Inicio", "pagina1"),
            ("Sobre Nosotros", "pagina2"),
            ("Contacto", "pagina3")
        ])

        # Contenido de la página
        self.label("Bienvenido a la página principal", size=24) #Etiqueta
        self.button("Ir a Página 2", link="pagina2")            #Botón
        self.button("Ir a Página 3", link="pagina3")
        self.input("Introduce tu nombre")                       #Campo texto
        self.checkbox("Aceptar términos y condiciones")         #Check list
        self.option_menu(["Opción 1", "Opción 2", "Opción 3"])  #Menú de opciones

        # Grid Layout con 3 elementos
        # Defino cantidad de elementos y paso los elementos correspondientes dentro de las llaves.
        self.grid_layout(3, [
            self.label("Logo", size=16),
            self.label("Texto descriptivo", size=16),
            self.button("Click aquí", link="pagina3")
        ])
