import requests
# 设置用户信息和端口
user = 'String'     # 用户名
password = 'String' # 登录密码
output = 8          # 出口
time = 0            # 0 代表永久登录
cmd = 'set'

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

# 发送POST请求
response = requests.post(url, data=data)
response.encoding = 'GBK'

# 通过访问baidu.com检查网络连接情况
response = requests.get('http://www.baidu.com')
if response.status_code == 200:
    print("\033[32m" + "网络连接正常" + "\033[0m")
