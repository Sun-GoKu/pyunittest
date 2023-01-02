import os
import configparser
import getpathInfo

path = getpathInfo.get_Path()

config_path = os.path.join(path,'config.ini')

config = configparser.ConfigParser()    # 创建对象（调用configparser模块对象来读取配置文件）
config.read(config_path,encoding='utf-8')   #读取文件，如果配置文件不存在则会创建

class ReadConfig():
    def get_http(self,name):
        value = config.get('HTTP',name)     # get方法，获得指定节点的指定key的value值（第一个参数是节点，第二个参数是key）
        return value

    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value

    def get_mysql(self,name):
        value = config.get('DATABASE',name)
        return value


if __name__ == "__main__":
    print('HTTP中的baseurl值为：',ReadConfig().get_http('baseurl'))
    print('EMAIL中的on_ff值为：',ReadConfig().get_email('on_off'))
