import yaml

class Swagger:
    def extractInfosFromSwagger(swaggerFileExtract):
        with open(swaggerFileExtract, 'r') as file:
            try:
                swaggerData = yaml.safe_load(file)
                paths = swaggerData.get('paths', {})

                infosExtractSwagger = []
                for path, methods in paths.items():
                    for method in methods.keys():
                        infosExtractSwagger.append((path, method))

                return infosExtractSwagger
            except yaml.YAMLError as e:
                print("Error loading swagger file:", e)