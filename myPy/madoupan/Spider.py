import random
import re
import requests
from queue import Queue
from lxml import etree
import resourse


class Spider:

    def __init__(self):
        '''初始化方法'''
        self.url_img_queue = Queue()
        self.url_page = "https://madoupan.com/?p="
        self.url_img = "https://madoupan.com"
        self.user_agents = resourse.user_agent
        self.newest = ""
        self.getNewest()


    def getPage(self,url):
        '''请求页面并返回结果'''

        response = requests.get(
            url,
            headers = {"User-Agent": random.choice(self.user_agents)}# 随机取一个ua 防止反爬虫)
        )
        response.encoding = "UTF-8"
        return response.text


    def param_img(self,url,pageNum):
        '''
        爬取如https://www.tujigu.com/a/44979/页面 中的所有图片，并加载到图片下载队列中
        '''
        html = etree.HTML(self.getPage(url))
        # 解析图片链接
        img_list = html.xpath("//div[@class='article-content']/p/img/@src")
        #图片链接拼接 并存入图片url队列
        for s in img_list:
            self.url_img_queue.put(self.url_img + s)
        #返回标题用于创建目录
        return html.xpath("//header/h1/text()")[0]



    def param_head(self,url):
        '''
        解析如https://www.tujigu.com/a/44979/页面
        判断改页面是否有效（是否404）
        '''
        #把getpage获得的字符串页面转换成 xpath能识别)的Element对象
        html = etree.HTML(self.getPage(url))
        head = html.xpath("//body[@class = 'error404']")
        return len(head) == 1;

    def downlod(self):
        '''把图片地址队列中 图片保存到本地'''

        while(not self.url_img_queue.empty()):
            url = self.url_img_queue.get()
            name_num = re.search(r"(\d+).jpg",url)
            if(name_num == None):
                print(url+"图片索引错误")
                return
            name_num = name_num.group()
            response = requests.get(url,
                                    headers={"User-Agent": random.choice(self.user_agents)}  # 随机取一个ua 防止反爬虫)
                                    )
            print("正在下载："+name_num)
            with open(name_num, 'wb') as f:
                f.write(response.content)
                f.close()




    def getNewest(self):
        '''
        从本地获得储存的页码 判断网页更新没有，如果更新了本地也一起更新
        '''

        # 打开本地储存的最新地址
        f = open("newest")
        newest = f.readline().strip()#strip()去首尾空格
        newest = int(newest)
        f.close()

        # 看看网页更新没有
        while(1):
            newest = newest+1
            if(self.param_head(self.url_page+str(newest))):
                break

        #获得网页 的最新地址保存到本地
        newest = newest-1
        f = open('newest','w')
        f.write(str(newest))
        f.close()
        self.newest = str(newest)

if __name__ == '__main__':
    spide = Spider()
    spide.url_img_queue.put("https://tjg.gzhuibei.com/a/1/32423/35.jpg")
    spide.downlod()