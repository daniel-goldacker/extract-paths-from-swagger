from config import ConfigFiles
from swagger import Swagger

with open(ConfigFiles.PATH_FILE, "w") as arquivo:
    arquivo.writelines("Infos of Swagger file:" + '\n')
    for infosSwagger in Swagger.extractInfosFromSwagger(ConfigFiles.SWAGGER_FILE):
        arquivo.writelines(' * [' + infosSwagger[1].upper() + '] ' + infosSwagger[0] + '\n')
