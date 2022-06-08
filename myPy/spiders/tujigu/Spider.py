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
        self.url_page = "https://www.tujigu.com/a/"
        self.url_img = "https://tjg.gzhuibei.com/a/1/{}/{}.jpg"
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
        #解析头部信息
        html = etree.HTML(self.getPage(url))
        head = html.xpath("//head/title/text()")[0]
        if(head.find("404")>=0):
            print(url+"404")
            return
        #从头部获得图片数目
        nums = re.search(r"\[\d+P\]",head)
        if(nums == None):
            print(url+"erro!!!")
            return
        nums = int(nums.group()[1:-2])
        #构造图片url，并存入图片url队列
        url_img_mothe = self.url_img.format(str(pageNum),'{}')
        for i in range(nums):
            self.url_img_queue.put(url_img_mothe.format(str(i+1)))
        return head



    def param_head(self,url):
        '''
        解析如https://www.tujigu.com/a/44979/页面
        判断改页面是否有效（是否404）
        '''
        #把getpage获得的字符串页面转换成 xpath能识别的Element对象
        html = etree.HTML(self.getPage(url))
        head = html.xpath("//head/title/text()")[0]
        return head.find("404")

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
            if(self.param_head(self.url_page+str(newest))>=0):
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