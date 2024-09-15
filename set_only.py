import requests
import os
import configparser

path = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(path, "config.ini")

# config 不存在时初始化文件：
if not os.path.exists(config_file_path):
    with open(config_file_path, 'w',encoding='utf-8') as f:
        f.write(
'''[config]
user = 
# 用户名
password = 
# 登录密码
output = 8
# 0: 1教育网出口(国际,仅用教育网访问,适合看文献)
# 1: 2电信网出口(国际,到教育网走教育网)
# 2: 3联通网出口(国际,到教育网走教育网)
# 3: 4电信网出口2(国际,到教育网免费地址走教育网)
# 4: 5联通网出口2(国际,到教育网免费地址走教育网)
# 5: 6电信网出口3(国际,默认电信,其他分流)
# 6: 7联通网出口3(国际,默认联通,其他分流)
# 7: 8教育网出口2(国际,默认教育网,其他分流)
# 8: 9移动网出口(国际,无P2P或带宽限制)
time = 0
# 3600: 1小时
# 14400: 4小时
# 39600: 11小时
# 50400: 14小时
# 0: 永久
cmd =set
# set 开通网络
# login 只登录
'''
    )
        print("\033[42;37m\033[1m已创建配置文件config.ini\033[0m")
        print("\033[42;37m\033[1m请在config.ini文件中配置登录信息后重新运行程序\033[0m")
        exit()

config_data = configparser.ConfigParser()
config_data.optionxform = str
config_data.read(config_file_path, encoding='utf-8')

user = config_data['config']['user']
password = config_data['config']['password']
output = config_data.getint('config','output')
time = config_data.getint('config','time')
cmd = config_data['config']['cmd']

# URL
url = 'http://wlt.ustc.edu.cn/cgi-bin/ip'

# 组装POST数据
data = {
    'name': user,
    'password': password,
    'cmd': cmd,
    'type': output,
    'exp': time
}
print("Requesting...",end='\r')
# 发送POST请求
response = requests.post(url, data=data)
response.encoding = 'GBK'
print("Checking internet...",end='\r')
# 通过访问baidu.com检查网络连接情况
response = requests.get('http://www.baidu.com')
if response.status_code == 200:
    print("\033[42;37m\033[1m网络连接正常,测试用网址：baidu.com\033[0m")
