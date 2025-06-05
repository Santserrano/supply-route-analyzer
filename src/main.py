from panda.engine.app import App
from panda.helpers.db_generator import generate_sqlite_schema, seed_users

# Generar base de datos y semilla de usuarios
generate_sqlite_schema('schema.panda', 'app.db')
seed_users('app.db')

ROLE_TO_PAGE = {
    'admin': 'ops',
    'editor': 'ops',
    'viewer': 'pagina2',
}

if __name__ == "__main__": # Renderizado de todas las ventanas "pages/*"
    app = App(role_to_page=ROLE_TO_PAGE)
    app.mainloop()
