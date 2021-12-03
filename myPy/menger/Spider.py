import random
import re
import threading

import requests
from queue import Queue
from lxml import etree
import resourse


class Spider:

    def __init__(self):
        '''初始化方法'''
        self.user_agents = resourse.user_agent
        self.url_img_queue = Queue()
        self.lock = threading.Lock()


    def getPage(self,url,cookie=None):
        '''请求页面并返回结果'''
        cookies = ''
        if cookie:
            cookies = {'pwd': cookie}

        response = requests.get(
            url,
            headers = {"User-Agent": random.choice(self.user_agents)},# 随机取一个ua 防止反爬虫)
            cookies = cookies
        )
        response.encoding = "UTF-8"
        return response.text


    def param_head(self, url):
        '''
        解析查看密码，这个网站喜欢把查看密码放到head标签中
        '''
        html = self.getPage(url)
        head = re.search(r'访问密码：(\d+)', html)
        return head.group(1)


    def param_img(self,url):
        '''
        爬取页面中的所有图片，并加载到图片下载队列中
        '''
        html = etree.HTML(self.getPage(url,self.param_head(url)))
        # 解析图片链接
        img_list = html.xpath("//div[@class='note-content']/img/@src")
        if not img_list:
            img_list = html.xpath("//div[@class='note-content']/p/img/@src")
        #图片链接拼接 并存入图片url队列
        for s in img_list:
            self.url_img_queue.put(s)
        #返回标题用于创建目录
        mktime = html.xpath("//header/time/text()")[0]
        return html.xpath("//header/h2/text()")[0],re.match(r'\d\d\d\d-\d\d-\d\d',mktime).group()





    def downlod(self):
        '''把图片地址队列中 图片保存到本地'''

        while(not self.url_img_queue.empty()):
            self.lock.acquire()
            url = self.url_img_queue.get()
            name_num = str(self.url_img_queue.qsize())
            self.lock.release()
            response = requests.get(url,
                                    headers={"User-Agent": random.choice(self.user_agents)}  # 随机取一个ua 防止反爬虫)
                                    )
            print("正在下载："+name_num)
            with open(name_num+'.jpg', 'wb') as f:
                f.write(response.content)
                f.close()





if __name__ == '__main__':
    spide = Spider()
    html,mktime = spide.param_img('http://w.zhaowho.cn/163825989223542')
    print(html)
    print(mktime)