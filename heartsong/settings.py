# -*- coding: utf-8 -*-

BOT_NAME = 'heartsong'

SPIDER_MODULES = ['heartsong.spiders']
NEWSPIDER_MODULE = 'heartsong.spiders'

ROBOTSTXT_OBEY = False  # 不遵守Robot协议

# 配置管道，数字代表优先级，因为本项目只有一个管道，所以可取1-1000中的任意值
ITEM_PIPELINES = {
    'heartsong.pipelines.HeartsongPipeline': 300,
}

