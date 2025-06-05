import sqlite3
import re
from panda.helpers.model_parser import PandaSchemaParser

SQLITE_TYPE_MAP = {
    'Int': 'INTEGER',
    'String': 'TEXT',
    'Float': 'REAL',
    'Bool': 'INTEGER',  # 0/1
}

def parse_default(attr):
    match = re.match(r'@default\((.+)\)', attr)
    if match:
        return match.group(1)
    return None

def generate_sqlite_schema(schema_path, db_path='app.db'):
    parser = PandaSchemaParser(schema_path)
    models = parser.parse()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    for model_name, fields in models.items():
        sql = f'CREATE TABLE IF NOT EXISTS {model_name.lower()} ('
        col_defs = []
        for field in fields:
            col = f'{field["name"]} '
            col_type = SQLITE_TYPE_MAP.get(field['type'], 'TEXT')
            col += col_type
            if any(attr == '@id' for attr in field['attributes']):
                col += ' PRIMARY KEY'
                if any('@default(autoincrement())' in attr for attr in field['attributes']):
                    col += ' AUTOINCREMENT'
            if any(attr == '@unique' for attr in field['attributes']):
                col += ' UNIQUE'
            default_val = next((parse_default(attr) for attr in field['attributes'] if attr.startswith('@default')), None)
            if default_val and 'autoincrement' not in default_val:
                col += f' DEFAULT {default_val}'
            col_defs.append(col)
        sql += ', '.join(col_defs) + ')'
        c.execute(sql)
    conn.commit()
    conn.close()

def seed_users(db_path='app.db'):
    users = [
        {'username': 'admin', 'password': 'admin123', 'role': 'admin'},
        {'username': 'editor', 'password': 'editor123', 'role': 'editor'},
        {'username': 'viewer', 'password': 'viewer123', 'role': 'viewer'},
    ]
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for user in users:
        try:
            c.execute('INSERT INTO user (username, password, role) VALUES (?, ?, ?)',
                      (user['username'], user['password'], user['role']))
        except sqlite3.IntegrityError:
            pass  # Ya existe
    conn.commit()
    conn.close()

# Ejemplo de uso:
# generate_sqlite_schema('schema.panda', 'app.db')
# seed_users('app.db') 