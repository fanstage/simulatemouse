import win32gui

def enum_windows_callback(hwnd, windows):
    if win32gui.IsWindowVisible(hwnd):
        text = win32gui.GetWindowText(hwnd)
        windows.append((hwnd, text))

def get_current_windows():
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows

# 获取当前所有窗口
windows = get_current_windows()
for hwnd, title in windows:
    print(f"Window handle: {hwnd}, title: {title}")
