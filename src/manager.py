from config import ConfigFiles
from swagger import Swagger

with open(ConfigFiles.PATH_FILE, "w") as arquivo:
    arquivo.writelines("Paths in Swagger file:" + '\n')
    for path in Swagger.extractPathsFromSwagger(ConfigFiles.SWAGGER_FILE):
        arquivo.writelines(path + '\n')
