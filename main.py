import requests
from bs4 import BeautifulSoup
# 设置用户信息和端口
user = 'String'     # 用户名
password = 'String' # 登录密码
output = 8          # 8 为移动国际出口
time = 0            # 0 为永久开启
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

# HTML内容
html_content = response.text

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'lxml')

# 找到包含登录日志的表格
log_table = soup.find_all('table')[-1]  # 假设日志总是在最后一个表格

# 提取表格中的所有行
log_rows = log_table.find_all('tr')

# 创建一个空列表来存储日志
logs = []

# 遍历除表头之外的所有行
for row in log_rows[1:]:
    cols = row.find_all('td')
    if cols:
        log_entry = {
            "时间": cols[0].text.strip(),
            "IP地址": cols[1].text.strip(),
            "消息": cols[2].text.strip()
        }
        logs.append(log_entry)

# 打印提取的登录日志
print("登录日志:")
for log in logs:
    print("\033[34m" + log['时间'] + "\033[0m" + " - " + "\033[32m" + log['消息'] + "\033[0m")

# 通过访问baidu.com检查网络连接情况
response = requests.get('http://www.baidu.com')
if response.status_code == 200:
    print("\033[32m" + "网络连接正常" + "\033[0m")
