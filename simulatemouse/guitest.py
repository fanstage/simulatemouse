from tkinter import Tk, StringVar
from tkinter.ttk import Label, Entry, Button, Treeview
from ttkbootstrap import Style
import datetime
import win32gui
import win32con
import pyautogui
import pyperclip


def geturl1(x, y):
    # 点击掌上海大
    pyautogui.click(156, 451)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1


def check_new_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        x, y = 100, 100
        width, height = 440, 560
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, width, height, 0)
        print(f"New window detected: {hwnd}")
        # 点击三个点
        pyautogui.click(433, 120)
        pyautogui.PAUSE = 1
        # 点击复制链接
        pyautogui.click(307, 272)
        pyautogui.PAUSE = 1
        # 获取剪贴板内容
        link = pyperclip.paste()
        # 创建一个文本文件，将剪贴板内容写入文本文件，并且下次写入就换行
        print("link:", link)
        tree.insert('', 'end',
                    values=(entry_var1.get(), '1', link, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # 叉掉
        pyautogui.click(531, 120)
        pyautogui.PAUSE = 1
        return False


def check_window(title):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetWindowText(hwnd)] = hwnd
        return True

    hwnds = {}
    win32gui.EnumWindows(callback, hwnds)
    return hwnds.get(title, None)


def on_button_click():
    while True:
        hwnd = check_window(entry_var1.get())
        if hwnd:
            # 对窗口进行操作
            x, y = 100, 100
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, 400, 374, 0)
            geturl1(158, 407)
            win32gui.EnumWindows(check_new_window, None)


root = Tk()
style = Style(theme='darkly')
Label(root, text='official account').grid(row=0, column=0, pady=10)
entry_var1 = StringVar()
Entry(root, textvariable=entry_var1).grid(row=0, column=1, pady=10)

Label(root, text='row').grid(row=1, column=0, pady=10)
entry_var1 = StringVar()
Entry(root, textvariable=entry_var1).grid(row=1, column=1, pady=10)


Label(root, text='col').grid(row=2, column=0, pady=10)
entry_var2 = StringVar()
Entry(root, textvariable=entry_var2).grid(row=2, column=1, pady=10)


Button(root, text='获取', command=on_button_click).grid(row=1, column=2, pady=10)


tree = Treeview(root, columns=('name', 'index', 'link', 'date'), show='headings')
tree.heading('name', text='名称')
tree.heading('index', text='序号')
tree.heading('link', text='链接')
tree.heading('date', text='日期')
tree.grid(row=3, columnspan=4)
root.mainloop()