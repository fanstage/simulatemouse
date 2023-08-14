import pyautogui
import pyperclip
import cv2
import numpy as np
last_clipboard_content = ''
screenshot = pyautogui.screenshot()
# 将 PIL 图像转换为 OpenCV 图像
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
# 加载要检测的图像（例如微信图标）
template = cv2.imread('wechat.png', 0)
# 使用模板匹配算法在屏幕截图中查找特定的图像
res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
# 设置阈值
threshold = 0.8

# 获取匹配结果
loc = np.where(res >= threshold)

# 如果找到了匹配的图像，则在匹配位置模拟鼠标点击
if len(loc[0]) > 0:
    print('找到了匹配的图像')
    # 获取匹配位置
    x, y = loc[1][0], loc[0][0]
    # 在匹配位置模拟鼠标点击
    pyautogui.click(x, y)
else:
    print('没有找到匹配的图像')

def paste(foo):
    pyperclip.copy(foo)
    pyautogui.hotkey('ctrl', 'v')


def geturl(x, y):
    global last_clipboard_content
    # 点击关于我们
    pyautogui.click(465, 1020)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1
    # 点击三个点
    pyautogui.click(1395, 67)
    pyautogui.PAUSE = 1
    # 点击复制链接
    pyautogui.click(1407, 220)
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
    pyautogui.click(1495, 68)
    pyautogui.PAUSE = 1


def geturl2(x, y):
    # 点击职工服务
    global last_clipboard_content
    pyautogui.click(1405, 1015)
    pyautogui.PAUSE = 1
    # 点击子级菜单
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1
    # 点击三个点
    pyautogui.click(1395, 67)
    pyautogui.PAUSE = 1
    # 点击复制链接
    pyautogui.click(1407, 220)
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
    pyautogui.click(1495, 68)
    pyautogui.PAUSE = 1


pyautogui.click(420, 1061)
pyautogui.PAUSE = 1
# foo用来接送输入的字符串
foo = u'上港家园'
pyautogui.click(860, 267)
paste(foo)
pyautogui.PAUSE = 1
pyautogui.click(868, 352)
pyautogui.PAUSE = 1
pyautogui.click(1185, 212)
pyautogui.PAUSE = 1
geturl(465, 877)
geturl(453, 907)
geturl(464, 941)
geturl(464, 974)
geturl2(1405, 841)
geturl2(1405, 873)
geturl2(1405, 907)
geturl2(1405, 940)
geturl2(1405, 973)








