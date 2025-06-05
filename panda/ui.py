import customtkinter as ctk

class PandaPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_row = 0  # Contador de filas para ubicar elementos dinámicamente
        self.app = parent.winfo_toplevel()  # Almacenar referencia a la aplicación principal
        self.setup()

    def setup(self):
        pass 

    def label(self, text, size=14, row=None, col=0, padx=5, pady=10, parent=None, 
              fg_color="transparent", text_color=None, font_family="Arial", anchor="w"):
        if row is None:
            row = self.current_row
            self.current_row += 1
        target = parent or self
        etiqueta = ctk.CTkLabel(
            target, 
            text=text, 
            font=(font_family, size),
            fg_color=fg_color,
            text_color=text_color,
            anchor=anchor
        )
        if parent:
            etiqueta.pack(padx=padx, pady=pady, anchor='w')
        else:
            etiqueta.grid(row=row, column=col, padx=padx, pady=pady, sticky='w')
        return etiqueta

    def button(self, text, link=None, command=None, row=None, col=0, padx=5, pady=10, parent=None,
               fg_color=None, hover_color=None, text_color=None, width=200, height=35):
        if row is None:
            row = self.current_row
            self.current_row += 1
        target = parent or self
        if command is not None:
            boton = ctk.CTkButton(
                target, 
                text=text, 
                command=command,
                fg_color=fg_color,
                hover_color=hover_color,
                text_color=text_color,
                width=width,
                height=height
            )
        else:
            boton = ctk.CTkButton(
                target, 
                text=text, 
                command=lambda: self.app.link(link),
                fg_color=fg_color,
                hover_color=hover_color,
                text_color=text_color,
                width=width,
                height=height
            )
        if parent:
            boton.pack(padx=padx, pady=pady, anchor='w')
        else:
            boton.grid(row=row, column=col, padx=padx, pady=pady, sticky='w')
        return boton

    def entry(self, label, placeholder="", width=200, row=None, col=0, padx=5, pady=10, parent=None,
              fg_color=None, border_color=None, text_color=None, placeholder_text_color=None):
        if row is None:
            row = self.current_row
            self.current_row += 1
        target = parent or self
        frame = ctk.CTkFrame(target, fg_color="transparent")
        
        if parent:
            frame.pack(fill='x', padx=padx, pady=pady)
        else:
            frame.grid(row=row, column=col, padx=padx, pady=pady, sticky='w')
        
        label_widget = ctk.CTkLabel(
            frame, 
            text=label,
            text_color="#1f538d"  # Color azul oscuro para las etiquetas
        )
        label_widget.pack(side='left', padx=(0, 5))
        
        entrada = ctk.CTkEntry(
            frame, 
            placeholder_text=placeholder, 
            width=width,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color,
            placeholder_text_color=placeholder_text_color
        )
        entrada.pack(side='left', fill='x', expand=True)
        return entrada

    def frame(self, title=None, row=None, col=0, rowspan=1, colspan=1, padx=5, pady=10,
              fg_color=None, border_color=None, corner_radius=None):
        if row is None:
            row = self.current_row
            self.current_row += 1
        marco = ctk.CTkFrame(
            self,
            fg_color=fg_color,
            border_color=border_color,
            corner_radius=corner_radius
        )
        marco.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=padx, pady=pady, sticky='nsew')
        
        if title:
            titulo = ctk.CTkLabel(
                marco, 
                text=title, 
                font=("Arial", 16, "bold"),
                text_color="#1f538d"  # Color azul oscuro para títulos
            )
            titulo.pack(pady=(10, 5))
            
        return marco

    def result_display(self, text="", row=None, col=0, padx=5, pady=10, parent=None,
                      fg_color=None, border_color=None, text_color=None, width=400, height=150):
        if row is None:
            row = self.current_row
            self.current_row += 1
        target = parent or self
        display = ctk.CTkTextbox(
            target, 
            width=width, 
            height=height,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color
        )
        if parent:
            display.pack(fill='both', expand=True, padx=padx, pady=pady)
        else:
            display.grid(row=row, column=col, padx=padx, pady=pady, sticky='w')
        display.insert("1.0", text)
        display.configure(state="disabled")
        return display

    def grid_layout(self, columns, elements, row=None, fg_color=None, border_color=None):
        if row is None:
            row = self.current_row
            self.current_row += 1
        container = ctk.CTkFrame(
            self,
            fg_color=fg_color,
            border_color=border_color
        )
        container.grid(row=row, column=0, columnspan=columns, pady=10, sticky='nsew')

        for i in range(columns):
            container.columnconfigure(i, weight=1)

        for index, element in enumerate(elements):
            if element:
                element.grid(row=0, column=index, padx=5, pady=10, sticky='w')

        return container

    def navbar(self, buttons, fg_color=None, border_color=None):
        """Crea una barra de navegación en la parte superior con botones distribuidos en columnas."""
        navbar_frame = ctk.CTkFrame(
            self,
            fg_color=fg_color,
            border_color=border_color
        )
        navbar_frame.grid(row=0, column=0, columnspan=len(buttons), pady=5, sticky="ew")
        
        for i, (text, link) in enumerate(buttons):
            btn = ctk.CTkButton(navbar_frame, text=text, command=lambda l=link: self.app.link(l))
            btn.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

        return navbar_frame
