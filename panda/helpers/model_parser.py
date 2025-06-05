import re

class PandaSchemaParser:
    def __init__(self, schema_path):
        self.schema_path = schema_path
        self.models = {}

    def parse(self):
        with open(self.schema_path, 'r', encoding='utf-8') as f:
            content = f.read()
        model_blocks = re.findall(r'model\s+(\w+)\s*\{([^}]*)\}', content, re.MULTILINE | re.DOTALL)
        for model_name, body in model_blocks:
            fields = self._parse_fields(body)
            self.models[model_name] = fields
        return self.models

    def _parse_fields(self, body):
        fields = []
        for line in body.strip().split('\n'):
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            # Ejemplo: id Int @id @default(autoincrement())
            parts = line.split()
            if len(parts) < 2:
                continue
            field_name = parts[0]
            field_type = parts[1]
            attributes = parts[2:]
            fields.append({
                'name': field_name,
                'type': field_type,
                'attributes': attributes
            })
        return fields

# Ejemplo de uso:
# parser = PandaSchemaParser('schema.panda')
# models = parser.parse()
# print(models) 