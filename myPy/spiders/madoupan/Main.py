import os
import threading
import random

from Spider import Spider


class Main:
    def __init__(self):
        self.spider = Spider()
        # 储存路径，存在哪里自己改
        self.path = "G:\\图集\\python\\madoupan"


    def downlod(self):
        '''多线程下载模块'''
        self.spider.downlod()

    def spiders(self,pageNum):
        '''多线程爬虫调用模块'''
        if( int(pageNum)>int(self.spider.newest) or int(pageNum)<3):
            print("页码无效")
            return
        #解析页码
        url = self.spider.url_page+pageNum
        head = self.spider.param_img(url,pageNum)
        #创建目录
        os.chdir(self.path)
        if(os.path.exists(pageNum+head)):
            print(pageNum+"目录已经存在")
            return
        os.mkdir(pageNum+head)
        os.chdir(pageNum+head)
        #调用多线程
        print(pageNum+head + "开始下载")
        t_list = []
        for i in range(19):
            t = threading.Thread(target=self.downlod)
            t.start()
            t_list.append(t)
        #主线程自己也去下载
        self.spider.downlod()
        #让主线程等待所有子线程完成后再下载下一部 图集
        for i in t_list:
            i.join()
        print(pageNum+head+"下载完毕")




    def main(self):
        '''用户主程序'''
        while (1):
            #改变目录，否则刚刚下载完的图片目录不许删除，显示该目录以被占用
            os.chdir("c:\\")
            print("目前最新的序号是3-"+self.spider.newest)
            chose = input("1.单个下载\n2.区间下载\n3.随机下载\n")
            if (chose == '1'):
                self.spiders(input("输入序号：\n"))
            elif (chose == '2'):
                head = int(input("输入开始区间:\n"))
                end = int(input("输入结束区间:\n"))
                #子线程调用
                for i in range(head,end+1):
                    self.spiders(str(i))

            elif (chose == '3'):
                nums = input("随机几个本子？\n")
                if(not nums.isdigit()):
                    print("mmp?")
                    continue
                for i in range(int(nums)):
                    page = random.randint(3,int(self.spider.newest))
                    self.spiders(str(page))
            else:
                print("mmp?")





if  __name__ == '__main__':
    main = Main()
    main.main()
