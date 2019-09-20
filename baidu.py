#_*_coding:utf-8_*_
#/usr/bin/env python
import requests
def interface(url):
    r = requests.get(url)
    print (r.status_code)
    print (r.text)
if __name__=='__main__':
    a = 'http://wwww.baidu.com'
    h = interface(a)


