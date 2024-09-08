# python_for_ustc_wlt
python实现自动登录中科大网络通

需求包：

- requests
- BeautifulSoup
- lxml

BeautifulSoup 和 lxml 包可以解析返回的数据以判断是否成功登录， 不需要此功能可以选择使用set_only.py

首次运行后生成config.ini文件，需要在其中设置登录信息后重新运行主程序