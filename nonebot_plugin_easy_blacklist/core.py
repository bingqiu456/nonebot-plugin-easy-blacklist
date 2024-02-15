from typing import List

add_count = 0
del_count = 0
sum_black = 0

search_time = 0
search_time_ = 0


class blacklist(object):
    """blacklist_system"""

    def __init__(self):
        self.x = -1
        self.y = -1
        self.arg = False
        self.time = None
        self.ly = ""
        self.account = -1

    def add(self, qq: str, time: int, ly: str, account: int) -> bool:
        """
        添加qq号
        qq: str
        """
        q = self
        qq = bin(int(qq))[2:]
        for i in qq:
            i = int(i)
            if i == 0:
                if q.x == -1:
                    q.x = blacklist()
                q = q.x

            if i == 1:
                if q.y == -1:
                    q.y = blacklist()
                q = q.y
        q.arg = True
        q.time = time
        q.ly = ly
        q.account = account
        return True

    def search(self, qq: str) -> bool:
        """
        搜索qq号
        返回bool
        True代表存在 False代表不存在
        """
        i = 0
        k = self
        qq = bin(int(qq))[2:]
        while i < len(qq):
            p = int(qq[i])
            if p == 1:
                if k.y == -1:
                    return [False]
                else:
                    k = k.y
            else:
                if k.x == -1:
                    return [False]
                else:
                    k = k.x
            i += 1
        return [k.arg, k.time, k.account, k.ly]

    def many_add(self, q: List[str]) -> bool:
        """
        批量添加
        """
        for i in q:
            self.add(i[0], i[1], i[2], i[3])
        return True

    def many_search(self, q: List[str]) -> List[bool]:
        """
        批量搜索
        """
        ans = []
        for i in q:
            ans.append(self.search(i))
        return ans

    def del_black(self, qq: str) -> bool:
        """
        删除
        qq: str
        """
        k = self
        qq = bin(int(qq))[2:]
        for j in range(0, len(qq) - 1):
            if qq[j] == "0":
                k = k.x
            else:
                k = k.y

        if qq[-1] == "0":
            if k.x.y == -1 and k.x.x == -1:
                k.x = -1
        if qq[-1] == "1":
            if k.y.x == -1 and k.y.y == -1:
                k.y = -1

        return True

    def many_del(self, qq: List[str]) -> List[bool]:
        """
        批量删除
        """
        for j in range(0, len(qq)):
            qq[j] = self.del_black(qq[j])
        return qq
