#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
import os, sys
import socket
from tkinter import *
from tkinter.ttk import *
import threading
from tkinter.messagebox import *
import mySniffer_IP as mys

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Sniffer')
        self.master.geometry('560x350')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Label1.TLabel', font=('宋体',9))
        self.Label1 = Label(self.top, text='请输入以太网卡ip：', style='Label1.TLabel')
        self.Label1.place(relx=0.2, rely=0.15,anchor=CENTER)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, text='', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.35, rely=0.15, relwidth=0.477, relheight=0.098,anchor=W)

        self.Text2 = Text(self.top,  font=('宋体',9))
        self.Text2.place(relx=0.475, rely=0.5, relwidth=0.8, relheight=0.5,anchor=CENTER)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, text='开始', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.3, rely=0.9, relwidth=0.25, relheight=0.1,anchor=CENTER)

        self.style.configure('Command2.TButton',font=('宋体',9))
        self.Command2 = Button(self.top, text='停止', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.7, rely=0.9, relwidth=0.25, relheight=0.1,anchor=CENTER)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def show(self):
        '''讲抓到的包打印到页面'''
        while True:
            # 读取数据包
            raw_buffer = sniffer.recvfrom(65535)[0]  # 获取数据包，接收最大字节数为65565
            # 读取前20字节
            ip_header = mys.IP(raw_buffer[0:24])
            # 输出协议和双方通信的IP地址
            # now_time = dt.datetime.now().strftime('%T')  # 获取系统当前时间
            result = 'Protocol: ' + str(ip_header.protocol) + ' ' + str(ip_header.src_address) + ' : ' + str(
                ip_header.src_port) + ' -> ' + str(ip_header.dst_address) + ' : ' + str(
                ip_header.dst_port) + '  size:' + str(ip_header.len)  + '\n'  # 设置输出的字符串
            self.Text2.insert('end', result)  # 将每条输出插入到界面
            time.sleep(1)

    def Command1_Cmd(self, event=None):
        '''开始抓包按钮'''
        #TODO, Please finish the function here!
        var = self.Text1.get()
        if os.name == "nt":  # 判断系统是否为window
            socket_protocol = socket.IPPROTO_IP  # 设置协议为ip协议
        else:
            socket_protocol = socket.IPPROTO_ICMP
        global sniffer

        # 创建一个原始套接字
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        try:

            sniffer.bind((var, 0))  # 套接字绑定地址，0默认所有端口
        except:
            showerror(title='错误', message='socket连接错误')  # 若绑定失败则弹窗解释

        # 设置ip头部
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        # Windows下要打开混杂模式
        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            # 设置开启混杂模式，socket.SIO_RCVALL默认接收所有数据，socket.RCVALL_ON开启
        show_th = threading.Thread(target=self.show)  # 创建一个线程，执行函数为show()
        show_th.setDaemon(True)
        show_th.start()

    def Command2_Cmd(self, event=None):
        '''停止抓包按钮'''
        #TODO, Please finish the function here!
        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)  # 关闭混杂模式，第一个参数是接收所有数据，第二个对应关闭
        sniffer.close()  # 关闭套接字

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
