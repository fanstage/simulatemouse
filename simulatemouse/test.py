import time
import win32gui
import win32con
import pyautogui

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
        pyautogui.click(140, 1020)
        pass
    time.sleep(1)