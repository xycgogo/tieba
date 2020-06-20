# -*- coding: UTF-8 -*-
'''
@author: 'xycgogo'
@date: 2019/6/18 17:27
@file: $NAME.py
'''
from __future__ import unicode_literals

import sys

from requests import session
import re
#from libs.stmp_email import send_email
import requests
import random
import time
import hashlib
import time


class TiebaSign():
    def __init__(self): #,USERNAME,PASSWORD):
        self.session = session()
        self.USERNAME = "西西的小耳机呀"
        self.PASSOWRD = "hnvnv5lrg0uu"

    def login(self):
        '''
        登录微博
        :return:
        '''
        self.session.get("http://www.baidu.com")
        resp = self.session.get("https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3")
        print(resp.text)
        #data = {
        #    'username':self.USERNAME,
        #    'password':self.PASSOWRD
        #}
        #self.headers = {
        #    'Referer': 'https://passport.tieba.cn/signin/login?entry=mtieba&r=http%3A%2F%2Fm.tieba.cn',
        #    'Content-Type': 'application/x-www-form-urlencoded'
        #}
        #login_url = 'https://passport.tieba.cn/sso/login'
        #resp = self.session.post(login_url,data,headers=self.headers)

        #if resp.json()['retcode'] != 20000000:
        #    print('登录失败，错误原因为：{}'.format(resp.json()['msg']))
        #    sys.exit(1)
        #else:
        #    #self.cookie = resp.headers['Set-Cookie']  # 获取cookie
        #    #self.uid = resp.json()['data']['uid']
        #    cookie_dict[self.USERNAME] = resp.headers['Set-Cookie']
        #    uid_dict[self.USERNAME] = resp.json()['data']['uid']
        #    #return resp.json()
			
    def get_tbs(self,bduss):
        # 获取tbs
        headers = {
            'Host': 'tieba.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Cookie': 'BDUSS=' + bduss,
        }
        url = 'http://tieba.baidu.com/dc/common/tbs'
        return requests.get(url=url, headers=headers).json()['tbs']

    def encodeData(self, data):
        SIGN_KEY = 'tiebaclient!!!'
        s = ''
        keys = data.keys()
        for i in sorted(keys):
            s += i + '=' + str(data[i])
        sign = hashlib.md5((s + SIGN_KEY).encode('utf-8')).hexdigest().upper()
        data.update({'sign': str(sign)})
        return data


    def tieba_lzl(self):
        # 客户端楼中楼
        fid = '2085792'
        tid = '6279800471'
        kw = '罗云熙'
        bduss = 'HNDR0FxTHR-d1o5dy1RMzZZNUdXWHNTRX5zbX43ejBTN1JWR35GZTdUOERBYmxkRVFBQUFBJCQAAAAAAAAAAAEAAACzZEP-zvfO97XE0KG2-rv60b0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN0kV0DdJFdV'
        tbs = self.get_tbs(bduss)
        content = "#罗云熙# #罗云熙遇见阳光遇见你# #罗云熙周小山# #熙字如金# #罗云熙未来可期# #全世界最好的罗云熙# #罗云熙月上重火# #罗云熙上官透# #罗云熙逆流而上# #健康头皮 强韧姜来# #罗云熙代言施华蔻# #罗云熙米兰时装周# #罗云熙掮客#" + self.session.get('https://chp.shadiao.app/api.php').text
        quote_id = '127738901178'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ka=open',
            'User-Agent': 'bdtb for Android 9.7.8.0',
            'Connection': 'close',
            'Accept-Encoding': 'gzip',
            'Host': 'c.tieba.baidu.com',
        }

        data = {
                'BDUSS':bduss,
                '_client_type':'2',
                '_client_id':'wappc_1534235498291_488',
                '_client_version':'9.7.8.0',
                '_phone_imei':'000000000000000',
                'anonymous':'1',
                'content':content,
                'fid':fid,
                'kw':kw,
                'model':'MI+5',
                'net_type':'1',
                'new_vcode':'1',
                'post_from':'3',
                'quote_id':quote_id,
                'tbs':tbs,
                'tid':tid,
                'timestamp':str(int(time.time())),
                'vcode_tag':'12',
            }
        data = self.encodeData(data)
        url = 'http://c.tieba.baidu.com/c/c/post/add'
        res = requests.post(url=url, data=data, headers=headers, timeout=2).json()
        print(res)


    #回帖
    def tieba_reply(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ka=open',
            'User-Agent': 'bdtb for Android 9.7.8.0',
            'Connection': 'close',
            'Accept-Encoding': 'gzip',
            'Host': 'c.tieba.baidu.com',
        }
        #self.headers = {
        #    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36',
        #    'Cookie': self.cookie,
        #    'referer': "http://tieba.baidu.com/p/6279800471"
        #}
        #self.url = 'http://tieba.baidu.com/f/commit/post/add' 
        url = 'http://c.tieba.baidu.com/c/c/post/add' 

        resp = self.session.get("http://tieba.baidu.com/dc/common/tbs")
        #tbs = resp.json()['tbs']
        fid = '2085792'
        tid = '6279800471'
        kw = '罗云熙'
        bduss = 'HNDR0FxTHR-d1o5dy1RMzZZNUdXWHNTRX5zbX43ejBTN1JWR35GZTdUOERBYmxkRVFBQUFBJCQAAAAAAAAAAAEAAACzZEP-zvfO97XE0KG2-rv60b0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN0kV0DdJFdV'
        tbs = self.get_tbs(bduss)
        print(tbs)
        #tbs = '6539439022b6a6f11569813544'
        #print(post_url)
        #text = random.choice(MESSAGE) + random.choice(VIDEO)
        content = "#罗云熙# #罗云熙遇见阳光遇见你# #罗云熙周小山# #熙字如金# #罗云熙未来可期# #全世界最好的罗云熙# #罗云熙月上重火# #罗云熙上官透# #罗云熙逆流而上# #健康头皮 强韧姜来# #罗云熙代言施华蔻# #罗云熙米兰时装周# #罗云熙掮客#" + self.session.get('https://chp.shadiao.app/api.php').text
        data = {
            'BDUSS': bduss,
            '_client_type': '2',
            '_client_version': '9.7.8.0',
            '_phone_imei': '000000000000000',
            'anonymous': '1',
            'content': content,
            'fid': fid,
            'from': '1008621x',
            'is_ad': '0',
            'kw': kw,
            'model': 'MI+5',
            'net_type': '1',
            'new_vcode': '1',
            'tbs': tbs,
            'tid': tid,
            'timestamp': str(int(time.time())),
            'vcode_tag': '11',
        }
        data = self.encodeData(data)
        res = requests.post(url=url, data=data, headers=headers, timeout=2).json()
        print(res)
        #self.data = {
        #    'ie': 'utf-8',
        #    'kw': '罗云熙',
        #    'fid': '2085792',
        #    'tid': '6279800471',
        #    'floor_num': '753',
        #    'quote_id': '127738901178',
        #    'rich_text': '1',
        #    'tbs': '6539439022b6a6f11569813544',
        #    'content': text,
        #    'basilisk': '1',
        #    'lp_type': '0',
        #    'lp_sub_type': '0',
        #    'new_vcode': '1',
        #    'tag': '11',

        #    'basilisk': '1',
        #    #'mouse_pwd: 39,33,38,61,32,37,37,33,34,24,32,61,33,61,32,61,33,61,32,61,33,61,32,61,33,61,32,61,33,24,34,33,38,37,41,24,32,40,35,33,61,32,33,41,33,15698135552171
        #    #'mouse_pwd_t: 1569813555217
        #    #'mouse_pwd_isclick: 1
        #    'repostid': '127738901178',
        #    'geetest_success': '1',
        #    '_BSK': 'TRdeCBYJG1JTQQtaCEUNblB5QAlSVhEZFkQFFwkZUlJVQ1ceQFJQFFwTf2B6dRodEUYHFgwVR0tBVhUSQQBADEEHXwMBGRRUDRMJFVJVWkZWFRZeChIIEhZEFFNKE1AGFAMYV1JZR1EaF0QIFgkbfmd+LhRNFA0DEw8Ud219fxcYFkYEEQMWFg5yFwBQQgNFQwMDEAV4HQMBAwEHDwEAAAQBC1IEU1RQUAdTBwgNBwoNBQcQBgYTAncbGBFNAhAIQgdUAF8JAAYACQAdEVwFFgwVR0tBVhUSRQFADEFQB11CUBobWQARDxQFDwcDFRZGCBIIEC9ZG18KXVAaAxcIERtiXVpSWkRKFH1tEAMCTAZaFjFYXwMCAhhJBQEdFHdFQ1VRZFxSeVsWGVQFUR8CAxYRc3lneHgYFllaUlETflVRWQ0fQXUOQ15YUxYPBh0FGgcOAwYXDQMZY1NUA0QIGVMCBhsFDxodEVgGFgwXGw8MBhUBBgdUBEgaTgYBAhoIDAEBAB0YHgIGChgCDQEKBUsaSQFVBR0GBgkRHRsGBwQaAAcABhoVGAEGVBpUAlMFGBkeCA4IBhkABwMCGhUcAg8JBR5WDlgETx0ZBAIAFAUFBwIdGh0CCgUDFQQHAFYfQxpEXwAXDBkKAQICBAEHBB8bVwIbChJGEEMEGkRCABcMGQkBCwUYFloHEQMUR0tFVx5AV1UUXBFXVFpKXR0RQQUWDBdVTFpQTVldXEJCDmUSQ1hbUREREUgVb1pXQVpPURNaX1ZXPxYcFEoTXQQUAxpUXRcYFl0EEQMUVVhcQVdOFAQHRAsRBwYIDwEGBAUYFFsAGw4TCwADBVIDUAdKE1AHFAMYAAMBBBgURwIbDhFfRVxRFl8OWEZDUFtSVlUZGhVPFG1bUk1dRVwQUV0GUzwWGxMdF0ELGgsRe2F4ehcfG0MHGwoQQg1FFXsDQkJUUVwUU19ARhhQWlBMRx9aXF1BBxoRVxRUX0EaVkhUXVBGGEJaQxVYVldXRlpOUBNXC1RCGVVVV0JWURhYWVZSTV1cVxxBVw5QTUEPX1VaQRVcXlBAWVFYQR9XVV5cHFFHEUIOWyNdVFhTV0xCH11dR0JaQUAYX1ZTU0YLWQ9UB0MdWFNXTVNSRxhEU0dAVlpSVVJTQE5FAkQJXV1XV0tLEx8XWQAUDxEJGAcABAEeVgVVBUoFCQEFGxQTXQcWDhZBQUxRHxtAABBYFDZfCAIDF0s=',
        #}
        #self.action = "发帖"			
        #self.post_data();			

    def post_data(self):
        respon = self.session.post(self.url, self.data, headers=self.headers)
        print(respon.json())
        #try:
        #    if(respon.json()['code'] == '100000'):
        #        print(self.action + "成功")
        #    else:
        #        print(self.action + "失败")
        #        print(respon.json())
        #        time.sleep(3)
        #except:
        #        print(self.action + "链接无法打开：" + self.url)	


if __name__ == '__main__':
#    for USERNAME,PASSWORD in  USERDICT.items():
#        print("登录%s" % USERNAME)
        tieba = TiebaSign() #USERNAME,PASSWORD)
            #tieba.login()
        for i in range(0, 5):
            tieba.tieba_lzl()
            tieba.tieba_reply()
            time.sleep(10)
            



