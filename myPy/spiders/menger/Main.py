import os
import threading
import random

from Spider import Spider


class Main:
    def __init__(self):
        self.spider = Spider()
        # 储存路径，存在哪里自己改
        self.path = "G:\\图集\\python\\menger"


    def downlod(self):
        '''多线程下载模块'''
        self.spider.downlod()

    def spiders(self,url,name):
        '''多线程爬虫调用模块'''
        #解析页码,获得标题和
        temp = 0
        while (1):
            try:
                head, mktime = self.spider.param_img(url)
                break
            except Exception as e:
                temp = temp + 1
                print('重试:', temp)
        dir = mktime
        if name:
            dir = dir + '-' + name + '-'
        dir = dir+head
        #创建目录
        os.chdir(self.path)
        if(os.path.exists(dir)):
            print(dir+"目录已经存在")
            return
        os.mkdir(dir)
        os.chdir(dir)
        #调用多线程
        print(dir + "开始下载")
        t_list = []
        for i in range(5):
            t = threading.Thread(target=self.downlod)
            t.start()
            t_list.append(t)
        #主线程自己也去下载
        self.spider.downlod()
        #让主线程等待所有子线程完成后再下载下一部 图集
        for i in t_list:
            i.join()
        print(dir+"下载完毕")




    def main(self):
        '''用户主程序'''
        while (1):
            url = input("输入url地:")
            name = input("知道这是谁吗：")
            self.spiders(url, name)





if  __name__ == '__main__':
    main = Main()
    main.main()
