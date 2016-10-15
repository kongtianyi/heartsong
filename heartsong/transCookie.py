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
    cookie = "QGfS_2132_saltkey=we948g3O; QGfS_2132_lastvisit=1474856564; QGfS_2132_visitedfid=46D51D36; QGfS_2132_auth=e30bYh1T8QizyTro6%2Fk2NaGj5H4G7RQG%2BwZb65x%2Fc2mV60v7FPRrcwPM1rMdrP%2BXprHlKCcPpCR3jBvQSGw%2B; QGfS_2132_lastcheckfeed=1%7C1476453891; QGfS_2132_nofavfid=1; QGfS_2132_smile=1D1; QGfS_2132_lip=202.102.144.8%2C1476455101; QGfS_2132_security_cookiereport=7a47cGXzFcb6q1iQwUGtJn2Kb1Vf%2FeFRcNfCvS4yTnnh8vloKJam; QGfS_2132_onlineusernum=3; QGfS_2132_sid=IYdAND; QGfS_2132_ulastactivity=ae8ciQTMElhskvnz3ZJb%2FRPUawZA8A7h%2FNuWshMmOhdKGsscWW%2Bb; pgv_pvi=8246475216; pgv_info=ssi=s8110682270; tjpctrl=1476498795993; QGfS_2132_lastact=1476497144%09home.php%09misc; QGfS_2132_sendmail=1"
    trans = transCookie(cookie)
    print trans.stringToDict()


