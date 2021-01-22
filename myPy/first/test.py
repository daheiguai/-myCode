
import requests

HTML = requests.get("https://www.baidu.com/").encoding = 'utf-8'
print(HTML)