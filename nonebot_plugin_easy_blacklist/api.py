import time
from nonebot.adapters.onebot.v11.event import Event
from . import core
from typing import List

core_list = core.blacklist()


def add_black(qq: str, time: int, ly: str, account: int) -> bool:
    core.add_count += 1
    return core_list.add(qq, time, ly, account)


def del_black(i: str) -> bool:
    core.del_count += 1
    return core_list.del_black(i)


def many_add(i: List[str]) -> bool:
    core.add_count += len(i)
    return core_list.many_add(i)


def many_del(i: List[str]) -> list[bool]:
    core.del_count += len(i)
    return core_list.many_del(i)


def search(i: str) -> bool:
    core.search_time = int(time.time())
    core.sum_black += 1
    l = core_list.search(i)
    core.search_time_ = int(time.time())
    return l


def many_search(i: List[str]) -> list[bool]:
    core.sum_black += len(i)
    return core_list.many_search(i)


async def check_hmd(event: Event) -> bool:
    v: bool = search(event.get_user_id())[0]
    if not v:
        return True
    else:
        return False
