import os

import yaml

from pii.libraries.utils.struct_util import DotDict

# envFile = os.getcwd() + "/.env.yml"
from pii.web.context import AppContext

envFile = os.path.dirname(__file__) + "/../.env.yml"

if not os.path.exists(envFile):
    print("Pls set .env.yml file. (You can copy from .env.example)")
    exit(1)

with open(rf"{envFile}") as file:
    ymlData = yaml.load(file, Loader=yaml.FullLoader)


class Config(DotDict):
    @property
    def env(self) -> str:
        return self.get("pii.env")

    @property
    def isProd(self) -> bool:
        return self.env == "prod"


class PiiIns:
    config = Config(ymlData)
    app = AppContext()
