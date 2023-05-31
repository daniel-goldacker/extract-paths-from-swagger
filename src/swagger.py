import yaml

class Swagger:

    def extractPathsFromSwagger(swaggerFileExtract):
        with open(swaggerFileExtract, 'r') as file:
            try:
                swaggerData = yaml.safe_load(file)
                paths = swaggerData.get('paths', {})

                return list(paths.keys())
            except yaml.YAMLError as e:
                print("Error loading swagger file:", e)
