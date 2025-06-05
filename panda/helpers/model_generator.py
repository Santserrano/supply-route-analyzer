from panda.helpers.model_parser import PandaSchemaParser

class ModelGenerator:
    def __init__(self, schema_path):
        self.parser = PandaSchemaParser(schema_path)
        self.models = self.parser.parse()

    def generate_classes(self, output_path):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('# Este archivo es generado automáticamente a partir de schema.panda\n\n')
            for model_name, fields in self.models.items():
                f.write(f'class {model_name}:
')
                # Constructor
                f.write('    def __init__(self')
                for field in fields:
                    f.write(f', {field["name"]}=None')
                f.write('):\n')
                for field in fields:
                    f.write(f'        self.{field["name"]} = {field["name"]}\n')
                f.write('\n')

# Ejemplo de uso:
# generator = ModelGenerator('schema.panda')
# generator.generate_classes('models.py') 