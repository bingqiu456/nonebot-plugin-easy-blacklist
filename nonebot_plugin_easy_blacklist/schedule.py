from nonebot import require

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from . import config, load_data


async def t():
    await load_data.save_list()


if not config.config.schedule_save_blacklist:
    pass
else:
    scheduler.add_job(t, "interval", seconds=config.config.schedule_save_time, id="blacklist")
