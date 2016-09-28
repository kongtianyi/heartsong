# -*- coding: utf-8 -*-

import scrapy

class HeartsongItem(scrapy.Item):
    title = scrapy.Field()  # 帖子的标题
    url = scrapy.Field()  # 帖子的网页链接
    author = scrapy.Field()  # 帖子的作者
    post_time = scrapy.Field()  # 发表时间
    content = scrapy.Field()  # 帖子的内容