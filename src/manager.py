from swagger import extractPathsFromSwagger

swaggerFile = './src/swagger-file/openapi.json'
pathFile = "./src/paths-file/paths.txt"

paths = extractPathsFromSwagger(swaggerFile)

with open(pathFile, "w") as arquivo:
    arquivo.writelines("Paths in Swagger file:" + '\n')
    for path in paths:
        arquivo.writelines(path + '\n')
