#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
import re
import shutil
import traceback
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
#Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkinter.messagebox import *
#Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog  #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('文件移动助手')
        self.master.geometry('591x415')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.lab_chosewayVar = StringVar(value='请选择文件选取方式')
        self.style.configure('Tlab_choseway.TLabel', anchor='w', font=('宋体',9))
        self.lab_choseway = Label(self.top, text='请选择文件选取方式', textvariable=self.lab_chosewayVar, style='Tlab_choseway.TLabel')
        self.lab_choseway.setText = lambda x: self.lab_chosewayVar.set(x)
        self.lab_choseway.text = lambda : self.lab_chosewayVar.get()
        self.lab_choseway.place(relx=0.041, rely=0.369, relwidth=0.218, relheight=0.06)

        self.lab_chosedirtoVar = StringVar(value='选择移动目标目录')
        self.style.configure('Tlab_chosedirto.TLabel', anchor='w', font=('宋体',9))
        self.lab_chosedirto = Label(self.top, text='选择移动目标目录', textvariable=self.lab_chosedirtoVar, style='Tlab_chosedirto.TLabel')
        self.lab_chosedirto.setText = lambda x: self.lab_chosedirtoVar.set(x)
        self.lab_chosedirto.text = lambda : self.lab_chosedirtoVar.get()
        self.lab_chosedirto.place(relx=0.041, rely=0.193, relwidth=0.205, relheight=0.041)

        self.lab_chosedirfromVar = StringVar(value='选择原始文件目录')
        self.style.configure('Tlab_chosedirfrom.TLabel', anchor='w', font=('宋体',9))
        self.lab_chosedirfrom = Label(self.top, text='选择原始文件目录', textvariable=self.lab_chosedirfromVar, style='Tlab_chosedirfrom.TLabel')
        self.lab_chosedirfrom.setText = lambda x: self.lab_chosedirfromVar.set(x)
        self.lab_chosedirfrom.text = lambda : self.lab_chosedirfromVar.get()
        self.lab_chosedirfrom.place(relx=0.041, rely=0.077, relwidth=0.205, relheight=0.041)

        self.text_dirfromVar = StringVar(value='选择文件夹')
        self.text_dirfrom = Entry(self.top, textvariable=self.text_dirfromVar, font=('宋体',9))
        self.text_dirfrom.setText = lambda x: self.text_dirfromVar.set(x)
        self.text_dirfrom.text = lambda : self.text_dirfromVar.get()
        self.text_dirfrom.place(relx=0.271, rely=0.058, relwidth=0.502, relheight=0.08)

        self.text_dirtoVar = StringVar(value='选择文件夹')
        self.text_dirto = Entry(self.top, textvariable=self.text_dirtoVar, font=('宋体',9))
        self.text_dirto.setText = lambda x: self.text_dirtoVar.set(x)
        self.text_dirto.text = lambda : self.text_dirtoVar.get()
        self.text_dirto.place(relx=0.271, rely=0.161, relwidth=0.502, relheight=0.08)

        self.button_dirfromVar = StringVar(value='选择')
        self.style.configure('Tbutton_dirfrom.TButton', font=('宋体',9))
        self.button_dirfrom = Button(self.top, text='选择', textvariable=self.button_dirfromVar, command=self.button_dirfrom_Cmd, style='Tbutton_dirfrom.TButton')
        self.button_dirfrom.setText = lambda x: self.button_dirfromVar.set(x)
        self.button_dirfrom.text = lambda : self.button_dirfromVar.get()
        self.button_dirfrom.place(relx=0.812, rely=0.058, relwidth=0.135, relheight=0.072)

        self.button_dirtoVar = StringVar(value='选择')
        self.style.configure('Tbutton_dirto.TButton', font=('宋体',9))
        self.button_dirto = Button(self.top, text='选择', textvariable=self.button_dirtoVar, command=self.button_dirto_Cmd, style='Tbutton_dirto.TButton')
        self.button_dirto.setText = lambda x: self.button_dirtoVar.set(x)
        self.button_dirto.text = lambda : self.button_dirtoVar.get()
        self.button_dirto.place(relx=0.812, rely=0.161, relwidth=0.135, relheight=0.072)

        self.style.configure('TLine1.TSeparator', background='#000000')
        self.Line1 = Separator(self.top, orient='horizontal', style='TLine1.TSeparator')
        self.Line1.place(relx=0.014, rely=0.308, relwidth=0.934, relheight=0.0024)

        self.topRadioVar = StringVar()
        self.style.configure('Tradio_start.TRadiobutton', font=('宋体',9))
        self.radio_start = Radiobutton(self.top, text='以下字符开头', value='radio_start', variable=self.topRadioVar, style='Tradio_start.TRadiobutton')
        self.radio_start.setValue = lambda x: self.topRadioVar.set('radio_start' if x else '')
        self.radio_start.value = lambda : 1 if self.topRadioVar.get() == 'radio_start' else 0
        self.radio_start.place(relx=0.041, rely=0.466, relwidth=0.158, relheight=0.08)

        self.style.configure('Tradio_end.TRadiobutton', font=('宋体',9))
        self.radio_end = Radiobutton(self.top, text='以下字符结尾', value='radio_end', variable=self.topRadioVar, style='Tradio_end.TRadiobutton')
        self.radio_end.setValue = lambda x: self.topRadioVar.set('radio_end' if x else '')
        self.radio_end.value = lambda : 1 if self.topRadioVar.get() == 'radio_end' else 0
        self.radio_end.place(relx=0.257, rely=0.466, relwidth=0.158, relheight=0.08)

        self.style.configure('Tradio_content.TRadiobutton', font=('宋体',9))
        self.radio_content = Radiobutton(self.top, text='包含以下字符', value='radio_content', variable=self.topRadioVar, style='Tradio_content.TRadiobutton')
        self.radio_content.setValue = lambda x: self.topRadioVar.set('radio_content' if x else '')
        self.radio_content.value = lambda : 1 if self.topRadioVar.get() == 'radio_content' else 0
        self.radio_content.place(relx=0.501, rely=0.466, relwidth=0.158, relheight=0.08)

        self.check_reVar = IntVar(value=0)
        self.style.configure('Tcheck_re.TCheckbutton', font=('宋体',9))
        self.check_re = Checkbutton(self.top, text='反选', variable=self.check_reVar, style='Tcheck_re.TCheckbutton')
        self.check_re.setValue = lambda x: self.check_reVar.set(x)
        self.check_re.value = lambda : self.check_reVar.get()
        self.check_re.place(relx=0.758, rely=0.466, relwidth=0.158, relheight=0.08)

        self.text_chosewayVar = StringVar(value='')
        self.text_choseway = Entry(self.top, textvariable=self.text_chosewayVar, font=('宋体', 9))
        self.text_choseway.setText = lambda x: self.text_chosewayVar.set(x)
        self.text_choseway.text = lambda: self.text_chosewayVar.get()
        self.text_choseway.place(relx=0.041, rely=0.578, relwidth=0.902, relheight=0.225)

        self.button_helpVar = StringVar(value='使用说明')
        self.style.configure('Tbutton_help.TButton', font=('宋体',9))
        self.button_help = Button(self.top, text='使用说明', textvariable=self.button_helpVar, command=self.button_help_Cmd, style='Tbutton_help.TButton')
        self.button_help.setText = lambda x: self.button_helpVar.set(x)
        self.button_help.text = lambda : self.button_helpVar.get()
        self.button_help.place(relx=0.056, rely=0.835, relwidth=0.169, relheight=0.08)

        self.button_doitVar = StringVar(value='开始移动')
        self.style.configure('Tbutton_doit.TButton', font=('宋体',9))
        self.button_doit = Button(self.top, text='开始移动', textvariable=self.button_doitVar, command=self.button_doit_Cmd, style='Tbutton_doit.TButton')
        self.button_doit.setText = lambda x: self.button_doitVar.set(x)
        self.button_doit.text = lambda : self.button_doitVar.get()
        self.button_doit.place(relx=0.733, rely=0.835, relwidth=0.169, relheight=0.08)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.radio_content.setValue(1)

    def button_dirfrom_Cmd(self, event=None):
        dir_from = tkFileDialog.askdirectory()
        self.text_dirfrom.setText(dir_from)

    def button_dirto_Cmd(self, event=None):
        dir_to = tkFileDialog.askdirectory()
        self.text_dirto.setText(dir_to)

    def button_help_Cmd(self, event=None):
        text = '''
            注意！！！！
            软件执行的是【剪切】操作，会导致源文件没有，移动到目标文件夹。
            用于帮助文件分类，比如说把1000个视频和图片从一个文件夹中分离。
            会移动源文件目录：
                如【目录1/目录2】匹配目录1则目录1中所有内容包括目录2都会被移动
                如果匹配目录2没匹配目录1，则都不会移动
            
            1.选择源文件夹和目标文件夹
                
                文件夹可以粘贴到文本框，也可以手动选择
            
            2.筛选文件，如筛选以【.mp3】结尾，则会移动所有MP3文件
                
                选择反选，则移动除了MP3以外的文件
            
            3.点击【开始移动】，软件会把选中的文件进行移动
        '''
        showinfo(title='使用说明',message=text)

    def button_doit_Cmd(self, event=None):
        #检查两个文件是否正确
        if not os.path.exists(self.text_dirfrom.text())   :
            showerror(title='路径错误',message='源文件目录检测失败，请检查！')
            return
        if not os.path.exists(self.text_dirto.text()):
            showerror(title='路径错误', message='目标目录检测失败，请检查！')
            return

        #检查输入的字符
        move_all = False
        if not self.text_choseway.text():
            move_all = askyesno(title='提示', message='没有输入字符，将复制全部文件？')
            if not move_all:return

        files = os.listdir(self.text_dirfrom.text())

        try:
            #输入空字符想移动全部文件
            if move_all:
                for f in files:
                    shutil.move(self.text_dirfrom.text()+'/'+f, self.text_dirto.text()+'/'+f)
            else:
                files2 = list() #正选列表
                files3 = list() #反选列表
                if self.radio_start.value():
                    for f in files:
                        if f.startswith(self.text_choseway.text()):
                            files2.append(f)
                        else:
                            files3.append(f)

                if self.radio_end.value():
                    for f in files:
                        if f.endswith(self.text_choseway.text()):
                            files2.append(f)
                        else:
                            files3.append(f)

                if self.radio_content.value():
                    for f in files:
                        if f.find(self.text_choseway.text()) != -1:
                            files2.append(f)
                        else:
                            files3.append(f)
                #是否反选
                if self.check_re.value():
                    for f in files3:
                        shutil.move(self.text_dirfrom.text() + '/' + f, self.text_dirto.text() + '/' + f)
                else:
                    for f in files2:
                        shutil.move(self.text_dirfrom.text() + '/' + f, self.text_dirto.text() + '/' + f)
            showinfo(title='成功', message='操作完成！！')
        except Exception as e:
            showerror(title='复制出错', message='''
            文件移动出错，请检查：
                1.是否有需要移动的文件在运行或者被占用
                
                2.本程序是否有权限访问目标文件
                    可以以管理员身份运行本程序尝试解决
            ''')

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

