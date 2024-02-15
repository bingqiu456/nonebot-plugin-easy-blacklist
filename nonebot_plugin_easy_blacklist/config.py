from nonebot import get_driver
from pydantic import BaseModel


class Config(BaseModel):
    schedule_save_blacklist = False
    schedule_save_time = 120
    check_global = False


config = Config.parse_obj(get_driver().config.dict())
