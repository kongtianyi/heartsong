# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "QGfS_2132_nofavfid=1; QGfS_2132_saltkey=GN4BcGg4; QGfS_2132_lastvisit=1478302547; QGfS_2132_st_t=0%7C1478306901%7C6c837d3b8b5892fd86ea3bb15bf4426e; QGfS_2132_forum_lastvisit=D_48_1478306883D_36_1478306901; QGfS_2132_visitedfid=36D48; QGfS_2132_seccode=1.fa43f9a3cb6efdd635; QGfS_2132_ulastactivity=29d9HUFm42onqH11DCnfZh8MN%2FFmPt0TEe15bNf2oeHflNI%2BJiwJ; QGfS_2132_auth=d713PkyUoDmnvp%2BestZH5F4lo%2BK0ewxTT1A02ulX%2FbRufbG%2B6T%2FIATHA5uYS9yoQzeNH3qz%2BupceANNs4IWF9w; QGfS_2132_lastcheckfeed=14%7C1478307120; QGfS_2132_security_cookiereport=12adOGUyzEnhcSY%2FZb5MgT52%2BxCPi3KZn%2Fh7pNHlxvWLnqDlLbAd; QGfS_2132_lip=202.102.144.8%2C1478307120; QGfS_2132_st_p=14%7C1478308725%7Cacf78675ed42e1121abb06c3d6b494cb; QGfS_2132_viewid=tid_196; QGfS_2132_sid=wbBi5Q; pgv_pvi=8246475216; pgv_info=ssi=s3823508970; QGfS_2132_smile=1D1; QGfS_2132_lastact=1478308730%09misc.php%09patch"
    trans = transCookie(cookie)
    print trans.stringToDict()


