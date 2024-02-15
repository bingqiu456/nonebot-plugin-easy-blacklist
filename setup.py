# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
name = "nonebot_plugin_easy_blacklist", 
version = "1.5", 
packages = setuptools.find_packages(),
author="bingyue", 
author_email="hello-yiqiu@qq.com", 
description="""一个轻量级的黑名单插件,支持api接入全平台,内存占用优化中""", 
url="https://github.com/bingqiu456/nonebot-plugin-easy-blacklist", 
install_requires=[ 
"aiofiles>=0.8.0", 
"nonebot2>=2.1.3",
"nonebot-adapter-onebot>=2.1.3",
"nonebot-plugin-apscheduler>=0.3.0"
],
keywords=["nonebot_plugin_easy_blacklist","easy_blacklist","blacklist"], 
)
