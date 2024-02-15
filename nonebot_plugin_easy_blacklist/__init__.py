from .config import Config
from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent
from nonebot.params import CommandArg
from nonebot.message import event_preprocessor
from nonebot.permission import SUPERUSER
from nonebot.exception import IgnoredException
from datetime import datetime
from nonebot.log import logger
import time
from . import api, core, load_data, config, schedule, run_state

__plugin_meta__ = PluginMetadata(
    name="黑名单插件",
    description="一个轻量级的黑名单插件,支持api接入全平台,内存占用优化中",
    usage="高效率,支持多消息场景",
    type="application",
    config=Config,
    homepage="https://github.com/bingqiu456/nonebot-plugin-easy-blacklist",
    supported_adapters={"~onebot.v11"}
)

core_list = api.core_list

add_black = on_command("添加黑名单", permission=SUPERUSER)
search_black = on_command("搜索黑名单", permission=SUPERUSER)
del_black = on_command("删除黑名单", permission=SUPERUSER)

if config.config.check_global:
    logger.success("全局检测黑名单开启成功！")


    @event_preprocessor
    async def _(event: GroupMessageEvent):
        v: bool = api.search(event.get_user_id())[0]
        if not v:
            pass
        else:
            raise IgnoredException(f"检测到:{event.get_user_id()}属于黑名单")
else:
    logger.warning("全局检测黑名单未开启,开启方法见文档")


@add_black.handle()
async def _(event: GroupMessageEvent, foo: Message = CommandArg()):
    t = str(foo).split(maxsplit=1)

    try:
        qid = foo[0].data["qq"]
    except IndexError:
        qid = t[0]

    ly = "" if len(t) == 1 else t[1]
    core.sum_black += 1
    if core_list.search(qid)[0]:
        await add_black.finish("该用户已经存在")
    h = int(time.time())
    core_list.add(
        qq=qid,
        time=h,
        ly=ly,
        account=event.get_user_id()
    )
    load_data.j_[qid] = [qid, h, ly, event.get_user_id()]
    if not config.config.schedule_save_blacklist:
        await load_data.save_list()
    core.add_count += 1
    await add_black.finish("已添加完毕")


@search_black.handle()
async def _(foo: Message = CommandArg()):
    p = str(foo).split("\r\n")
    for p_ in p:
        core.sum_black += 1
        m = core_list.search(p_)
        if m[0]:
            time_ = datetime.utcfromtimestamp(m[1]).strftime("%Y-%m-%d %H:%M:%S")
            await search_black.send(f"此人属于黑名单\n添加时间:{time_}\n操作人:{m[2]}\n添加原因:{m[3]}")
        else:
            await search_black.send("此人不属于黑名单")
    await search_black.finish()


@del_black.handle()
async def _(foo: Message = CommandArg()):
    core.del_count += 1
    try:
        qid = foo[0].data["qq"]
    except IndexError:
        qid = str(foo)
    if core_list.del_black(qid):
        load_data.j_.pop(qid)
        if not config.config.schedule_save_blacklist:
            await load_data.save_list()
        await del_black.finish("已删除该用户黑名单")
    else:
        await del_black.finish("该用户不是黑名单")
