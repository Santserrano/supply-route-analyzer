from panda.ui import PandaPage
from panda.auth import role_required, current_user
from panda.engine import LogisticsCalculator
import customtkinter as ctk

class Page(PandaPage):
    @role_required("admin", "editor")
    @auth_protect("admin", "editor")
    
    def setup(self):
        # Configurar colores
        self.primary_color = "#1f538d"
        self.secondary_color = "#2d7dd2"
        self.accent_color = "#97c1d9"
        self.bg_color = "#f0f4f8"
        self.text_color = "#000000"  # Negro puro para máximo contraste
        self.error_color = "#ef476f"
        self.success_color = "#06d6a0"
        self.title_color = "#1f538d"  # Color para títulos

        # Configurar el fondo de la página
        self.configure(fg_color=self.bg_color)

        # Encabezado
        header_frame = self.frame(
            fg_color=self.primary_color,
            corner_radius=10
        )
        self.label(
            f"Bienvenido, {current_user().username}",
            size=16,
            text_color="white",
            parent=header_frame
        )
        self.label(
            "Calculadora Logística",
            size=24,
            text_color="white",
            parent=header_frame
        )
        self.button(
            "Volver a la página 2",
            link="pagina2",
            parent=header_frame,
            fg_color=self.accent_color,
            hover_color=self.secondary_color,
            text_color="white"
        )

        # Contenedor principal para inputs y resultados
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.grid_columnconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_columnconfigure(1, weight=1)

        # Frame para los inputs
        input_frame = ctk.CTkFrame(
            main_container,
            fg_color="white",
            border_color=self.accent_color,
            corner_radius=10
        )
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        # Título del frame de inputs
        input_title = ctk.CTkLabel(
            input_frame,
            text="Parámetros del Viaje",
            font=("Arial", 16, "bold"),
            text_color=self.title_color
        )
        input_title.pack(pady=(10, 5))
        
        # Campos de entrada con estilo
        self.origen = self.entry(
            "Coordenadas origen (lat,lon)",
            placeholder="Ej: 40.7128,-74.0060",
            parent=input_frame,
            fg_color="white",
            border_color=self.accent_color,
            text_color=self.text_color,
            placeholder_text_color="#666666" 
        )
        self.destino = self.entry(
            "Coordenadas destino (lat,lon)",
            placeholder="Ej: 34.0522,-118.2437",
            parent=input_frame,
            fg_color="white",
            border_color=self.accent_color,
            text_color=self.text_color,
            placeholder_text_color="#666666"
        )
        self.carga = self.entry(
            "Carga en toneladas",
            placeholder="Ej: 10.0",
            parent=input_frame,
            fg_color="white",
            border_color=self.accent_color,
            text_color=self.text_color,
            placeholder_text_color="#666666"
        )
        self.litros_km = self.entry(
            "Consumo (litros/km)",
            placeholder="Ej: 0.3",
            parent=input_frame,
            fg_color="white",
            border_color=self.accent_color,
            text_color=self.text_color,
            placeholder_text_color="#666666"
        )
        self.precio_litro = self.entry(
            "Precio por litro",
            placeholder="Ej: 1.5",
            parent=input_frame,
            fg_color="white",
            border_color=self.accent_color,
            text_color=self.text_color,
            placeholder_text_color="#666666"
        )
        self.velocidad = self.entry(
            "Velocidad promedio (km/h)",
            placeholder="Ej: 80.0",
            parent=input_frame,
            fg_color="white",
            border_color=self.accent_color,
            text_color=self.text_color,
            placeholder_text_color="#666666"
        )
        
        # Botón de cálculo con estilo
        self.button(
            "Calcular",
            command=self.calcular_viaje,
            parent=input_frame,
            fg_color=self.secondary_color,
            hover_color=self.primary_color,
            text_color="white",
            width=200,
            height=40
        )

        # Frame para resultados
        resultados_frame = ctk.CTkFrame(
            main_container,
            fg_color="white",
            border_color=self.accent_color,
            corner_radius=10
        )
        resultados_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        # Título del frame de resultados
        resultados_title = ctk.CTkLabel(
            resultados_frame,
            text="Resultados",
            font=("Arial", 16, "bold"),
            text_color=self.title_color
        )
        resultados_title.pack(pady=(10, 5))
        
        self.resultados_display = self.result_display(
            parent=resultados_frame,
            fg_color="white",
            border_color=self.accent_color,
            text_color=self.text_color,
            width=400,
            height=400
        )

    def calcular_viaje(self):
        try:
            # Crear instancia del calculador
            calc = LogisticsCalculator()
            
            # Obtener y validar coordenadas
            origen = calc.parse_coordenadas(self.origen.get())
            destino = calc.parse_coordenadas(self.destino.get())
            
            # Obtener y validar otros parámetros
            carga = float(self.carga.get())
            litros_km = float(self.litros_km.get())
            precio_litro = float(self.precio_litro.get())
            velocidad = float(self.velocidad.get())
            
            # Realizar cálculo
            resultado = calc.calcular_viaje(
                origen=origen,
                destino=destino,
                carga=carga,
                litros_km=litros_km,
                precio_litro=precio_litro,
                velocidad=velocidad
            )
            
            # Salida
            texto_resultado = f"""
            📍 Distancia: {resultado.distancia:.2f} km
            ⏱️ Tiempo estimado: {resultado.tiempo_estimado:.2f} horas
            ⛽ Litros usados: {resultado.litros_usados:.2f} lts
            💰 Costo total: ${resultado.costo_combustible:.2f}
            """
            self.resultados_display.configure(state="normal")
            self.resultados_display.delete("1.0", "end")
            self.resultados_display.insert("1.0", texto_resultado)
            self.resultados_display.configure(state="disabled")
            
        except ValueError as e:
            self.resultados_display.configure(state="normal")
            self.resultados_display.delete("1.0", "end")
            self.resultados_display.insert("1.0", f"❌ Error: {str(e)}")
            self.resultados_display.configure(state="disabled")
        except Exception as e:
            self.resultados_display.configure(state="normal")
            self.resultados_display.delete("1.0", "end")
            self.resultados_display.insert("1.0", f"❌ Error inesperado: {str(e)}")
            self.resultados_display.configure(state="disabled")