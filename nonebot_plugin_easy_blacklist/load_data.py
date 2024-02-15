from nonebot.log import logger
import json
from . import api
from nonebot import require

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store

data_file = store.get_data_file("nonebot_plugin_easy_blacklist", "blacklist_by.json")

try:
    j_ = json.loads(data_file.read_text())
except (IndexError, FileNotFoundError, TypeError):
    logger.warning("黑名单数据不存在,已经创建")
    with open(store.get_data_dir("nonebot_plugin_easy_blacklist") / "blacklist_by.json", "w+", encoding="utf_8") as f:
        f.write("{}")
        f.close()
    j_ = json.loads(data_file.read_text())

logger.success("正在初始化黑名单")

for k in j_:
    api.add_black(k, j_[k][1], j_[k][2], j_[k][3])
logger.success("初始化成功")


async def save_list():
    data_file.write_text(json.dumps(j_))
