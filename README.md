<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://cdn.bingyue.top/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
    <h2>Nonebot-Plugin-easy-blacklist<h2>
    <br></br>
    _✨ 一个轻量级的黑名单插件,支持api接入全平台,内存占用优化中✨_
    <br></br>
</div>


## 如何下载

**两种方法，一种pip安装，一种nb安装**

1.`nonebot`安装

```bash
nb plugin install nonebot-plugin-easy-blacklist
```

1.`pip`安装

```bash
pip install nonebot-plugin-easy-blacklist
```

---

## 配置项

**schedule_save_blacklist**

类型:`bool`

> 定时保存黑名单数据，如果在消息量大的场景建议定时保存，默认是False

**schedule_save_time**

类型:`int`

> 隔多久保存一次数据，默认为120，也就是120秒

---

## 指令

- 添加黑名单+`艾特[QQ号]`+空格+原因 **可以不填写原因**
- 删除黑名单+`[QQ号]`
- 搜索黑名单+`[QQ号]` **可批量搜索见如下示例**

![](https://pic.imgdb.cn/item/65b7abdf871b83018aa99e0c.png)

---

## 规则

> 注:规则功能仅支持onebot11

如果你需要添加一个功能，而这个功能黑名单用户不能用，我们的api模块还提供了`check_hmd`参数，添加方法如下

改之前

```python
a = on_command("test")
```

改之后

```python
a = on_command("test",rule=check_hmd)
```

---

## 功能性

- [x] 添加黑名单
- [x] 删除黑名单
- [x] 搜索黑名单
- [x] 批量添加黑名单
- [x] 批量搜索黑名单
- [x] 批量删除黑名单
- [x] 快速搜索
- [x] 开放`API`

---

## API文档

**API调用如下代码所示**

```python
from nonebot import require,on_command
require("nonebot_plugin_easy_blacklist")
from nonebot_plugin_easy_blacklist import api

a = on_command("test")

@a.handle()
async def _():
    api.add_black(qq="111",time=-1,ly="111",account=-1)
    await a.finish("ok")
```

### API大全

#### 添加黑名单

- 地址:**api.add_black**

请求参数

|   qq    |         账号id         | 必填 |
| :-----: | :--------------------: | :--: |
|  time   | 添加时间，用时间截表示 | 必填 |
|   ly    | 添加原因，不想填可用"" | 必填 |
| account |       添加人的id       | 必填 |

返回参数 **bool**

| bool | 返回值为True | 表示添加成功 |
| ---- | ------------ | ------------ |

---

#### 搜索黑名单

- 地址:**api.search**

请求参数

| qq   | 账号id | 必填 |
| ---- | ------ | ---- |

返回参数 **List[bool,time,account,ly]**

| bool    | False代表不存在，True代表存在 | 获取的结果         |
| ------- | ----------------------------- | ------------------ |
| time    | 加入该黑名单的时间            | 加入该黑名单的时间 |
| account | 添加人的id                    | 添加人的id         |
| ly      | 添加你为黑名单的理由          | 理由               |

---

#### 删除黑名单

- 地址:**api.del_black**

请求参数

| qq   | 删除的id | 删除的id |
| ---- | -------- | -------- |

返回参数 **bool**

| bool | 返回值为True | 表示删除成功 |
| ---- | ------------ | ------------ |

---

#### 批量添加黑名单

- 地址:**api.many_add**

请求参数:**List[[qq,time,ly,account],[qq,time,ly,account]]**

|   qq    |         账号id         | 必填 |
| :-----: | :--------------------: | :--: |
|  time   | 添加时间，用时间截表示 | 必填 |
|   ly    | 添加原因，不想填可用"" | 必填 |
| account |       添加人的id       | 必填 |

返回参数 **bool**

| bool | 返回值为True | 表示删除成功 |
| ---- | ------------ | ------------ |

---

#### 批量搜索黑名单

- 地址:**api.many_search**

请求参数:**List[qq,qq,qq]**

| qq   | 账号id | 你要查找的账号id |
| ---- | ------ | ---------------- |

返回参数:**List[[bool,time,account,ly],[bool,time,account,ly]]**

| bool    | False代表不存在，True代表存在 | 获取的结果         |
| ------- | ----------------------------- | ------------------ |
| time    | 加入该黑名单的时间            | 加入该黑名单的时间 |
| account | 添加人的id                    | 添加人的id         |
| ly      | 添加你为黑名单的理由          | 理由               |

---

#### 批量删除黑名单

- 地址:**api.many_del**

请求参数:**List[qq,qq,qq]**

| qq   | 账号id | 你要查找的账号id |
| ---- | ------ | ---------------- |
|      |        |                  |

返回参数:**List[bool,bool]**

| bool | 返回值为True | 表示删除成功 |
| ---- | ------------ | ------------ |
|      |              |              |

---

## 性能

>实测数据，因电脑配置不同，仅供参考

**在黑名单id数量10000000，内存占用266m，1秒内可以被搜索93万次**
