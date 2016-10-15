# -*- coding: utf-8 -*-

# import scrapy # 可以用这句代替下面三句，但不推荐
from scrapy.spiders import Spider
from scrapy import Request
from scrapy.conf import settings

class HeartsongSpider(Spider):
    name = "heartsong"
    allowed_domains = ["heartsong.top"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        # 主页，此例只下载主页，看是否有登录信息
        "http://www.heartsong.top/forum.php"
    ]

    cookie = settings['COOKIE']  # 带着Cookie向网页发请求

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    # 爬虫的起点
    def start_requests(self):
        # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
        yield Request(self.start_urls[0], callback=self.parse, cookies=self.cookie,
                      headers=self.headers, meta=self.meta)

    # Request请求的默认回调函数
    def parse(self, response):
        with open("check.html", "wb") as f:
            f.write(response.body)  # 把下载的网页存入文件




