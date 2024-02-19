from win32gui import FindWindowEx, FindWindow, EnumWindows
import win32gui
"""
窗口结构
Type:DUIWindow Name: channel-name # 360层级
    |- Type: TabContentWnd
        |- Type: CefBrowserWindow
            |- Type: Chrome_WidgetWin_0 # 窗口浏览器层级
                |- Type: WrapperNativeWindowClass
                    |- Type: NativeWindowClass # Flash游戏层级

"""

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)
def find_window(part_title):
    for hwnd, title in hwnd_title.items():
        if part_title in title:
            return hwnd
def faa_get_handle(channel, mode="game"):
    """
    解析频道名称 获取句柄, 仅支持360游戏大厅,
    号1：输入你为游戏命名 例如'锑食‘
    号2：输入你命名的角色名 + 空格 + | + 空格 游戏命名。例如：'深渊之下 | 锑食'
    :param channel: 频道名称
    :param mode: "360" -> "browser" -> "flash"
    :return: handel
    """
    if '|' in channel:
        handle = FindWindow("DUIWindow", channel)  # 360窗口 该层级有刷新框
        if mode in ["browser", "flash"]:
            handle = FindWindowEx(handle, None, "TabContentWnd", "")
            handle = FindWindowEx(handle, None, "CefBrowserWindow", "")
            handle = FindWindowEx(handle, None, "Chrome_WidgetWin_0", "")  # 该层级 有 服务器序号输入框
        if mode == "flash":
            handle = FindWindowEx(handle, None, "WrapperNativeWindowClass", "")
            handle = FindWindowEx(handle, None, "NativeWindowClass", "")  # game窗口
    else:
        handle = find_window(channel)
        print('游戏窗口句柄:'+str(handle))
        if mode in ["flash","browser"]:
            handle = FindWindowEx(handle, None, "Afx:400000:b:10005:900010:0", "")
            handle = FindWindowEx(handle, None, None, "")
            handle = FindWindowEx(handle, None, None, "")
            handle = FindWindowEx(handle, None, None, "Chrome Legacy Window")
            # handle = FindWindowEx(handle, None, None, "") # game窗口
    return handle


if __name__ == '__main__':
    # print(faa_get_handle(channel="锑食", mode="360"))
    # print(faa_get_handle(channel="锑食", mode="browser"))
    # print(faa_get_handle(channel="锑食", mode="flash"))  # 刷新游戏后改变
    print(faa_get_handle(channel="光辉",mode="flash"))