import time
import win32gui
import win32con
import pyautogui
import pyperclip

last_clipboard_content = ''


def geturl1(x, y):
    # 点击掌上海大
    pyautogui.click(156, 451)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1


def geturl2(x, y):
    # 点击掌上海大
    pyautogui.click(275, 451)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1


def geturl3(x, y):
    # 点击掌上海大
    pyautogui.click(398, 451)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1


# def check_child_window(hwnd, extra):
#     # 检测新弹出的窗口
#     if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
#         x, y = 100, 100
#         width, height = 440, 560
#         win32gui.SetWindowPos(hwnd, win32con.HWND_DOTTOPMOST, x, y, width, height, 0)
#         print(f"New window detected: {hwnd}")


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


while True:
    hwnd = check_window('上海海事大学')
    if hwnd:
        # 对窗口进行操作
        x, y = 100, 100
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, 400, 374, 0)

        geturl1(158, 407)
        win32gui.EnumWindows(check_new_window, None)

        # geturl1(153, 374)
        # check_new_window()
        #
        # geturl1(153, 308)
        # check_new_window()
        #
        # geturl1(153, 273)
        # check_new_window()
        #
        # geturl2(276, 407)
        # check_new_window()
        #
        # geturl2(276, 374)
        # check_new_window()
        #
        # geturl2(276, 341)
        # check_new_window()
        #
        # geturl2(276, 309)
        # check_new_window()
        #
        # geturl2(276, 274)
        # check_new_window()
        #
        # geturl3(399, 407)
        # check_new_window()
        #
        # geturl3(399, 374)
        # check_new_window()
        #
        # geturl3(399, 341)
        # check_new_window()
        #
        # geturl3(399, 309)
        # check_new_window()
        #
        # geturl3(399, 274)
        # check_new_window()

        break