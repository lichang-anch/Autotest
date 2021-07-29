#coding：utf-8
import yaml
import os
def read(filepath):
    #将yaml文件所在路径传递给参数path
    path = filepath
    #获取yaml文件全路径
    yamlpath = os.path.join(path,"conf.yaml")
    #读取yaml文件
    f = open(yamlpath,"r",encoding="utf-8")
    cfg = f.read()
    #用load方法转换成字典
    d =  yaml.load(cfg,Loader=yaml.FullLoader)
    print (type(d))
    #获取字典value以列表形式返回
    var = []
    for m in d.values():
        list = m
        var.append(list)
    return var
    #关闭文件
    f.close


if __name__ == "__main__":
    osk = read(r'D:\NeustaAutotest\Test_data')
    print (osk)
    print (type(osk))


