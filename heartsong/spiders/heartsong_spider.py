# -*- coding: utf-8 -*-

# import scrapy # 可以用这句代替下面三句，但不推荐
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from scrapy import FormRequest
import random

class HeartsongSpider(Spider):
    name = "heartsong"
    allowed_domains = ["heartsong.top"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        # 起始url，这里只回复这一个页面，多个页面连续爬取请看mast分支
        "http://www.heartsong.top/forum.php?mod=viewthread&tid=136"
    ]

    # 用来保持登录状态，可把chrome上拷贝下来的字符串形式cookie转化成字典形式，粘贴到此处
    cookies = {'QGfS_2132_lastvisit': '1478302547', 'QGfS_2132_seccode': '1.fa43f9a3cb6efdd635', 'QGfS_2132_smile': '1D1', 'QGfS_2132_lip': '202.102.144.8%2C1478307120', 'QGfS_2132_ulastactivity': '29d9HUFm42onqH11DCnfZh8MN%2FFmPt0TEe15bNf2oeHflNI%2BJiwJ', 'QGfS_2132_auth': 'd713PkyUoDmnvp%2BestZH5F4lo%2BK0ewxTT1A02ulX%2FbRufbG%2B6T%2FIATHA5uYS9yoQzeNH3qz%2BupceANNs4IWF9w', 'QGfS_2132_nofavfid': '1', 'QGfS_2132_lastact': '1478308730%09misc.php%09patch', 'QGfS_2132_viewid': 'tid_196', 'QGfS_2132_sid': 'wbBi5Q', 'pgv_info': 'ssi', 'QGfS_2132_st_p': '14%7C1478308725%7Cacf78675ed42e1121abb06c3d6b494cb', 'QGfS_2132_visitedfid': '36D48', 'QGfS_2132_saltkey': 'GN4BcGg4', 'QGfS_2132_lastcheckfeed': '14%7C1478307120', 'QGfS_2132_forum_lastvisit': 'D_48_1478306883D_36_1478306901', 'QGfS_2132_st_t': '0%7C1478306901%7C6c837d3b8b5892fd86ea3bb15bf4426e', 'pgv_pvi': '8246475216', 'QGfS_2132_security_cookiereport': '12adOGUyzEnhcSY%2FZb5MgT52%2BxCPi3KZn%2Fh7pNHlxvWLnqDlLbAd'}

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    def start_requests(self):
        """
        这是一个重载函数，它的作用是发出第一个Request请求
        :return:
        """
        # 带着headers、cookies去请求self.start_urls[0],返回的response会被送到
        # 回调函数parse中
        yield Request(self.start_urls[0],
                             callback=self.parse, headers=self.headers,
                             cookies=self.cookies, meta=self.meta)

    def parse(self, response):
        """
        用以处理主题贴的首页
        :param response:
        :return:
        """
        selector = Selector(response)  # 创建选择器

        table = selector.xpath('//*[starts-with(@id, "pid")]')  # 取出所有的楼层
        if not table:
            # 这个链接内没有一个楼层，说明此主题贴可能被删了，
            # 把这类url保存到一个文件里，以便审查原因
            print "bad url!"
            f = open('badurl.txt', 'a')
            f.write(response.url)
            f.write('\n')
            f.close()
            return

        # 如有回复可见的隐藏区域，进行回复
        # locked = selector.xpath('//*[@class="locked"]')
        # if locked:
        #     re_a = locked.xpath('a/text()')
        #     if re_a and re_a.extract()[0] == u'回复':
        # 找到表单要提交到的地址
        form_action = selector.xpath('//*[@id="fastpostform"]/@action').extract()[0]
        action = "http://www." + self.allowed_domains[0] + "/" + form_action + "&inajax=1"
        replys = [
            '&#x56DE;&#x590D;&#x770B;&#x770B; &#x6709;&#x7528;&#x4E0D;',
            '&#x5389;&#x5BB3;&#x5389;&#x5BB3;&#xFF0C;&#x8C22;&#x8C22;&#x5206;&#x4EAB;&#xFF01;'
        ]  # utf-8编码的一些回复,具体使用什么编码要看具体的网站的编码
        reply = replys[random.randint(0, 1)]  #防止被管理员识别是机器回复，要随机一下
        formdata = {
            'formhash': selector.xpath('//*[@id="fastpostform"]/table/tr/td[2]/input[2]/@value').extract()[0],
            'usesig': selector.xpath('//*[@id="fastpostform"]/table/tr/td[2]/input[3]/@value').extract()[0],
            'subject': selector.xpath('//*[@id="fastpostform"]/table/tr/td[2]/input[4]/@value').extract()[0],
            'posttime': selector.xpath('//*[@id="posttime"]/@value').extract()[0],
            'message': reply
        }  # 表单数据，是从网页表单代码里分析出来的
        # 发出带表单的请求，当然，要有cookie
        yield FormRequest(action, callback=self.finish,
                          headers=self.headers,
                          cookies=self.cookies,
                          meta=self.meta,
                          formdata=formdata)
        return

    def finish(self, response):
        print "reply seccess!"