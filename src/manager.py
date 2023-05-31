import yaml

def extractPathsFromSwagger(swagger_file):
    with open(swagger_file, 'r') as file:
        try:
            swagger_data = yaml.safe_load(file)
            paths = swagger_data.get('paths', {})
            return list(paths.keys())
        except yaml.YAMLError as e:
            print("Error loading swagger file:", e)

swagger_file = './src/swagger-file/openapi.json'
paths = extractPathsFromSwagger(swagger_file)
print("Paths in Swagger file:")
for path in paths:
    print(path)