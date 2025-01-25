from typing import Dict
from mcdreforged.api.all import *


class Config(Serializable):
    # 0:guest 1:user 2:helper 3:admin 4:owner
    permission: Dict[str, int] = {
        "help": 0,
        "list": 0,
        "add": 3,
        "del": 3,
        "move": 2,
        "msg": 2,
        "info": 1,
    }
