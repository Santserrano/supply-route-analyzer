import sqlite3
import customtkinter as ctk
from panda.ui import PandaPage
from functools import wraps

_current_user = None

def current_user():
    return _current_user

def auth_protect(role):
    if current_user() != role:
        return 0
    else:
        return 1

def login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if current_user() is None:
            if hasattr(self, 'app'):
                self.app.show_login()
            else:
                print("No autenticado. Redirigiendo a login.")
        else:
            return func(self, *args, **kwargs)
    return wrapper

def role_required(*roles_or_usernames):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            user = current_user()
            if user is None:
                if hasattr(self, 'app'):
                    self.app.show_login()
                return None
            
            # Verificar si el usuario tiene alguno de los roles o usernames permitidos
            if user.role in roles_or_usernames or user.username in roles_or_usernames:
                return func(self, *args, **kwargs)
            
            # Si no tiene el rol requerido, mostrar mensaje y redirigir
            if hasattr(self, 'app'):
                self.app.show_error(f"Acceso denegado. Se requiere uno de los siguientes roles: {', '.join(roles_or_usernames)}")
                self.app.show_login()
            return None
        return wrapper
    return decorator

class AuthPage(PandaPage):
    def __init__(self, parent, role_to_page=None):
        self.role_to_page = role_to_page or {}
        super().__init__(parent)

    def setup(self):
        self.label("Iniciar Sesión", size=24, row=0, col=0)
        
        # Frame para los campos de entrada
        input_frame = self.frame()
        
        # Campos de entrada
        self.username_entry = self.entry("Usuario", parent=input_frame)
        self.password_entry = self.entry("Contraseña", parent=input_frame)
        
        # Botón de login
        self.button("Iniciar sesión", command=self.iniciar_sesion, parent=input_frame)
        
        # Etiqueta de error
        self.error_label = self.label("", size=12, parent=input_frame)

    def iniciar_sesion(self):
        global _current_user
        usuario = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT id, username, role FROM user WHERE username=? AND password=?", (usuario, password))
        result = c.fetchone()
        conn.close()

        if result:
            _current_user = type('User', (), {'id': result[0], 'username': result[1], 'role': result[2]})()
            page = self.role_to_page.get(_current_user.role)
            if page:
                self.app.link(page)
            else:
                self.error_label.configure(text=f"No hay página asignada para el rol: {_current_user.role}")
        else:
            self.error_label.configure(text="Usuario o contraseña incorrectos")

def require_username(username):
    user = current_user()
    if user is None or user.username != username:
        return False
    return True
