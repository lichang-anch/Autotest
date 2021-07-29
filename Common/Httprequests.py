#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Author:lichang


import requests


class Httprequests(object):

    def __init__(self,url):
        self.url = url
        self.req = requests.session()
        # 自定义请求头，根据自身所在公司项目需求
        self.header = {'sign':'NUFoNQvVLy1l4FzFfsCDydEMkdujR8Dkiqnp99999999','Content-Type':'application/json','Authorization':'Bearer890bb1b3-bac2-4caa-9b8f-75f6bab7bbd9'}

    #封装get请求
    def get(self,url = '',params = '',data = '',headers = None,cookies = None):
        response = self.req.get(url = url ,params = params ,data = data, headers = headers ,cookies = cookies)
        return response

    #封装post请求
    def post(self,url = '',params = '',data='',headers = None,cookies = None):
        reponse = self.req.post(url = url,params=params,data=data,headers =headers,cookies = cookies)
        return reponse

    #封装put请求
    def put(self,url='',params = '',data='',headers=None,cookies=None):
        reponse = self.req.put(url = url ,params = params ,data =data,headers =headers,cookies=cookies)
        return reponse

    #封装delete请求
    def delete(self,url='',params='',data='',headers=None,cookies=None):
        reponse = self.req.delete(url = url,params = params,data = data,headers = headers,cookies = cookies)
        return reponse







