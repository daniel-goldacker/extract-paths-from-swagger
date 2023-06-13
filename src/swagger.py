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



    def collectDataStatisticsSwaggerByMethod(arquivo_swagger):
        with open(arquivo_swagger, 'r') as arquivo:
            try:
                swaggerData = yaml.safe_load(arquivo)

                statistics = {
                    'GET': 0,
                    'POST': 0,
                    'PUT': 0,
                    'PATCH': 0,
                    'DELETE': 0
                }

                for path, pathDetails in swaggerData.get('paths', {}).items():
                    for method in pathDetails.keys():
                        methodUpper = method.upper()
                        if methodUpper in statistics:
                            statistics[methodUpper] += 1

                return statistics
            except yaml.YAMLError as e:
                print("Error loading swagger file:", e)