from config import ConfigFiles
from swagger import Swagger

with open(ConfigFiles.PATH_FILE, "w") as arquivo:
    arquivo.writelines("Statistics for Swagger file:" + '\n')
    statisticsSwagger = Swagger.collectDataStatisticsSwaggerByMethod(ConfigFiles.SWAGGER_FILE)
    totalMethodEndpoint = 0
    for method, count in statisticsSwagger.items():
        totalMethodEndpoint += count
        arquivo.writelines(f" * {method}: {count}" + '\n')

    arquivo.writelines('\n')
    arquivo.writelines("Paths for Swagger file:" + '\n')
    for infosSwagger in Swagger.extractInfosFromSwagger(ConfigFiles.SWAGGER_FILE):
        arquivo.writelines(' * [' + infosSwagger[1].upper() + '] ' + infosSwagger[0] + '\n')

    arquivo.writelines('\n')
    arquivo.writelines("Total Endpoints: " + str(totalMethodEndpoint) + '\n')