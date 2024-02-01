from nonebot import on_fullmatch
from nonebot.permission import SUPERUSER
from . import core
import time


start_time = int(time.time())

get_in = on_fullmatch("黑名单详情",permission=SUPERUSER)


@get_in.handle()
async def _():
    b = int(time.time())
    await get_in.finish(
        f"从现在已经运行了{b-start_time}秒\n"\
        f"总添加黑名单调用:{core.add_count}次\n" \
        f"总删除黑名单调用:{core.del_count}次\n" \
        f"总搜索黑名单调用:{core.sum_black}次\n" \
        f"上一次搜索用了:{core.search_time_-core.search_time}秒"
    )