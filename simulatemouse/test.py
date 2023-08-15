import time
import win32gui
import win32con
import pyautogui
import pyperclip


last_clipboard_content = ''


def geturl1(x, y):
    global last_clipboard_content
    # 点击掌上海大
    pyautogui.click(156, 451)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1
    # 点击三个点
    pyautogui.click(934, 242)
    pyautogui.PAUSE = 1
    # 点击复制链接
    pyautogui.click(945, 390)
    pyautogui.PAUSE = 1
    # 获取剪贴板内容
    link = pyperclip.paste()
    # 创建一个文本文件，将剪贴板内容写入文本文件，并且下次写入就换行
    if link != last_clipboard_content:
        # 创建一个文本文件，将剪贴板内容写入文本文件，并且下次写入就换行
        with open('link.txt', 'a') as f:
            f.write(link + '\n')
        # 更新保存的上一次剪贴板内容
        last_clipboard_content = link
    pyautogui.PAUSE = 1
    # 叉掉
    pyautogui.click(1030, 239)
    pyautogui.PAUSE = 1


def geturl2(x, y):
    global last_clipboard_content
    # 点击掌上海大
    pyautogui.click(275, 451)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1
    # 点击三个点
    pyautogui.click(934, 242)
    pyautogui.PAUSE = 1
    # 点击复制链接
    pyautogui.click(945, 390)
    pyautogui.PAUSE = 1
    # 获取剪贴板内容
    link = pyperclip.paste()
    # 创建一个文本文件，将剪贴板内容写入文本文件，并且下次写入就换行
    if link != last_clipboard_content:
        # 创建一个文本文件，将剪贴板内容写入文本文件，并且下次写入就换行
        with open('link.txt', 'a') as f:
            f.write(link + '\n')
        # 更新保存的上一次剪贴板内容
        last_clipboard_content = link
    pyautogui.PAUSE = 1
    # 叉掉
    pyautogui.click(1030, 239)
    pyautogui.PAUSE = 1


def geturl3(x, y):
    global last_clipboard_content
    # 点击掌上海大
    pyautogui.click(398, 451)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1
    # 点击三个点
    pyautogui.click(934, 242)
    pyautogui.PAUSE = 1
    # 点击复制链接
    pyautogui.click(945, 390)
    pyautogui.PAUSE = 1
    # 获取剪贴板内容
    link = pyperclip.paste()
    # 创建一个文本文件，将剪贴板内容写入文本文件，并且下次写入就换行
    if link != last_clipboard_content:
        # 创建一个文本文件，将剪贴板内容写入文本文件，并且下次写入就换行
        with open('link.txt', 'a') as f:
            f.write(link + '\n')
        # 更新保存的上一次剪贴板内容
        last_clipboard_content = link
    pyautogui.PAUSE = 1
    # 叉掉
    pyautogui.click(1030, 239)
    pyautogui.PAUSE = 1


def check_window(title):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetWindowText(hwnd)] = hwnd
        return True

    hwnds = {}
    win32gui.EnumWindows(callback, hwnds)
    return hwnds.get(title, None)

while True:
    hwnd = check_window('上海海事大学')
    if hwnd:
        # 对窗口进行操作
        x, y = 100, 100
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, 400, 374, 0)
        geturl1(153, 407)
        geturl1(153, 374)
        geturl1(153, 308)
        geturl1(153, 273)
        geturl2(276, 407)
        geturl2(276, 374)
        geturl2(276, 341)
        geturl2(276, 309)
        geturl2(276, 274)
        geturl3(399, 407)
        geturl3(399, 374)
        geturl3(399, 341)
        geturl3(399, 309)
        geturl3(399, 274)
        break
    time.sleep(1)