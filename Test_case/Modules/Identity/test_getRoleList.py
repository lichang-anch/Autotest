import os
import sys
import pytest
import json
from Common.Httprequests import *
from Conf.url_conf import URLConf
import logging
from Lib.readyamls import read
class Test_getnotice:
    #classmethod可以用来为一个类创建一些预处理的实例。
    @classmethod
    def setup_class(cls):
        path ='/api/carrier/systemManage/identity/getRoleList'
        cls.url = URLConf.TEST_URL.value + path
        cls.http = Httprequests(cls.url)

    def setup(self):
        Authorizations = read(r'D:\NeustaAutotest\Test_data')
        self.headers = {'sign':'NUFoNQvVLy1l4FzFfsCDydEMkdujR8Dkiqnp99999999','Content-Type':'application/json','Authorization':Authorizations[0][0]}
        self.http = Httprequests(self.url)

    def teardown(self):
        pass

    def test_001_getRoleList(self):
        #入参
        logger = logging.getLogger('test_001_getRoleMenu')
        playroad = {"param":{"status":1}}
        reponse = Test_getnotice.http.post(self.url,data = json.dumps(playroad),headers = self.headers)
        logger.info(self.url)
        logger.info(self.headers)
        logger.info(json.dumps(playroad))
        logger.info(reponse.text)
        resultNote =reponse.json().get('code')
        resultmessage = reponse.json().get('message')
        assert resultNote == '0'
        assert resultmessage == '请求成功'



if __name__ == '__main__':
    pytest.main(['-s', '-q'])