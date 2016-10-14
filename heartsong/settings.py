# -*- coding: utf-8 -*-

BOT_NAME = 'heartsong'

SPIDER_MODULES = ['heartsong.spiders']
NEWSPIDER_MODULE = 'heartsong.spiders'

ROBOTSTXT_OBEY = False  # 不遵守Robot协议

# 配置管道，数字代表优先级，因为本项目只有一个管道，所以可取1-1000中的任意值
ITEM_PIPELINES = {
    'heartsong.pipelines.HeartsongPipeline': 300,
}

MONGO_HOST = "127.0.0.1"  # 数据库主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "Spider"  # 数据库名
MONGO_COLL = "heartsong"  # collection名
# MONGO_USER = "zhangsan"  # 若数据库设置了访问权限
# MONGO_PSW = "123456"
