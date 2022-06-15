import os

import PySimpleGUI as sg  # Part 1 - The import


if __name__ == '__main__':

    layout = [[sg.Text("请选择改名模式")],
              [sg.Text("1.添加前缀")],
              [sg.Input(key='input1'), sg.Button('执行1')],
              [sg.Text("2.添加后缀")],
              [sg.Input(key='input2'), sg.Button('执行2')],
              [sg.Text("3.在中间添加字符")],
              [sg.Text("位置（第几个字符后面）")],
              [sg.Input(key='input3')],
              [sg.Text("添加的字符")],
              [sg.Input(key='input4'), sg.Button('执行3')],
              [sg.Button('使用说明'),sg.Button('Quit')]]

    window = sg.Window('批量文件重命名工具', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == '使用说明':
            sg.Popup('''
            使用说明\n
            1.把这个程序放到文件夹中\n
            2.选择改名方式点击执行\n
            3.程序会对这个文件夹里的所有文件（不包括文件夹）进行改名
            ''',title='使用说明')
        try:
            if event == '执行1':
                if not values['input1'] :
                    sg.Popup('请至少输入点东西！')
                else:
                    oslist = os.listdir()
                    for i in oslist:
                        if os.path.isdir(i) or i == 'FileRenameter.py' or i== 'FileRenameter.exe':
                            #如果是路径或者是本程序 跳过
                            continue
                        else:
                            name = values['input1'] + i
                            os.rename(i, name)
                    sg.Popup('执行成功')

            if event == '执行2':
                if not values['input2'] :
                    sg.Popup('请至少输入点东西！')
                else:
                    oslist = os.listdir()
                    for i in oslist:
                        if os.path.isdir(i) or i == 'FileRenameter.py' or i== 'FileRenameter.exe':
                            #如果是路径或者是本程序 跳过
                            continue
                        else:
                            name = i + values['input2']
                            os.rename(i, name)
                    sg.Popup('执行成功')

            if event == '执行3':
                if not values['input3'] or not values['input4']:
                    sg.Popup('请至少输入点东西！')
                else:
                    oslist = os.listdir()
                    for i in oslist:
                        if os.path.isdir(i) or i == 'FileRenameter.py' or i== 'FileRenameter.exe':
                            #如果是路径或者是本程序 跳过
                            continue
                        else:
                            index = int(values['input3'])
                            name = i[:index] + values['input4'] + i[index:]
                            os.rename(i, name)
                    sg.Popup('执行成功')

        except Exception as e:
            sg.Popup('出现错误！请检查是否有需要把改名的文件正在运行')



    window.close()

    #pyinstaller -w -F FileRenameter.py -p D:\a_myCode\-myCode-workSpace\myPy\usefulKit\fileRenameter\venv\Lib\site-packages