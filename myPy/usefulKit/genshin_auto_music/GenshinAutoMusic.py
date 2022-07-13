import os
import re
from queue import Queue
import time
import pyautogui as pag

press_list = Queue()

def main():
    name_list = list()
    for i in os.listdir():
        if re.match(r'.*\.txt', i):
            name_list.append(i)
    print('检测到以下曲谱文件：')
    for i in range(0, len(name_list)):
        print(str(i + 1) + '.' + name_list[i])
    print('注意：请选择规范的曲谱，否则报错！！！！！！')
    chose = input("请选择：")

    file = open(name_list[int(chose) - 1])
    text = file.readline()
    while text:
        if text.strip() == '-----':
            text = file.readline()
            continue
        word, thetime = text.split(' ')
        press_list.put(word.strip())
        press_list.put(thetime.strip())
        text = file.readline()
    file.close()
    time.sleep(5)
    while not press_list.empty():
        pag.write(press_list.get())
        time.sleep(float(press_list.get()))

if __name__ == '__main__':
    while 1:
        main()