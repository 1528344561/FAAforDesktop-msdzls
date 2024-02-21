import os
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication

from function.get_paths import get_root_path


class MyMainWindow0(QMainWindow):
    """读取.ui文件创建类 并加上一些常用方法"""

    # 注意：
    # 若ui界面文件是个对话框，那么MyApp就必须继承 QDialog
    # 若ui界面文件是个MainWindow，那么MyApp就必须继承 QMainWindow
    def __init__(self):
        # 继承父方法
        super().__init__()

        # 根目录获取
        self.path_root = get_root_path()

        # 加载 ui文件
        uic.loadUi(self.path_root + '\\resource\\ui\\fvm_2.0.ui', self)

        # 加载图标
        self.setWindowIcon(QIcon(self.path_root + '\\resource\\logo\\png-512x512.png'))

        # 设置窗口名称
        self.setWindowTitle("FAA - 本软件免费且开源 - 反馈交流: 786921130")

        # 设定字体
        c_font = QFont()  # custom_font
        c_font.setFamily("Microsoft YaHei")
        self.setFont(c_font)  # LayMain

        # 打印默认输出提示
        self.start_print()

    def printf(self, mes):
        """打印文本到输出框 """
        text_browser = self.TextBrowser
        text_browser.append(mes)  # 在TextBrowser显示提示信息
        cursor = self.TextBrowser.textCursor()
        text_browser.moveCursor(cursor.End)
        QtWidgets.QApplication.processEvents()  # 实时输出

    def start_print(self):
        """打印默认输出提示"""
        self.printf("**************必看*************")
        self.printf("此软件请配合美食大战老鼠桌面版使用")
        self.printf("此软件请配合美食大战老鼠桌面版使用")
        self.printf("软件主要用于:")
        self.printf("完成繁琐的日常活动.由于该软件不内置秒杀功能,建议刷关[普通关卡]交给桌面版完成,其余日常活动[悬赏,勇士等]交给FAA完成")
        self.printf("由于我们是配合桌面版使用,你可以选择开启秒杀,也可以使用FAA自带的放卡方案!具体方法接着往下看.")
        self.printf("以下介绍使用步骤:")
        self.printf("⓪打开桌面版两个游戏,在上面 '1P游戏名' '2P游戏名' 的文本框内填入两个号的名字(窗口的标题),其下面的文本框留空")
        self.printf("①如果你要开秒杀,则去掉 '自动放卡战斗' 选择框 ,如果你想使用FAA的放卡功能,则保持勾选.")
        self.printf("②让两个游戏号在游戏内加上好友")
        self.printf("③在右边勾选要进行的日常内容选项.")
        self.printf("④若要开秒杀,预先在桌面版内设置好一个合适的秒杀时间.")
        self.printf("⑤保存配置,点击开始")
        
        self.printf("\n\n在此特别感谢原作者 - 直视深渊")
        self.printf("------------以下为原作者的温馨提示-----------")
        self.printf("为确保使用安全")
        self.printf("[1] 务必有二级密码")
        self.printf("[2] 有一定的礼卷防翻牌异常")
        self.printf("[3] 高星或珍贵不绑卡挂拍卖/提前转移")
        self.printf("跨服和勇士功能罕见情况下会卡死, 但不会导致其他问题")
        self.printf("支持360游戏大厅 - 4399 或 QQ 渠道")
        self.printf("请认真阅读[文档], 以解决多数问题, 文档在[1]文件夹中README.md [2]Github主页下 [3]交流群精华消息")
        self.printf("运行直接闪退, 是窗口和游戏名称填写有误, 参考[文档]中[重要信息填写]部分")
        self.printf("开始后没反应, 请将软件移动到系统盘(C)之外, 或使用管理员身份运行")
        self.printf("[Github] https://github.com/StareAbyss/FoodsVsMouses_AutoAssistant")
        self.printf("[反馈&交流QQ] 786921130 欢迎加入")
        self.printf("[开源][免费][绿色] 请为我在Github点个免费的Star支持我吧")

    def closeEvent(self, event):
        """
        对MainWindow的函数closeEvent进行重构, 退出软件时弹窗提醒 并且结束所有进程(和内部的线程)
        """

        # 退出提示
        # self.reply = QMessageBox.question(
        #     self,
        #     '提示',
        #     "确认退出吗？",
        #     QMessageBox.Yes | QMessageBox.No,
        #     QMessageBox.No
        # )
        # if self.reply == QMessageBox.Yes:
        #     event.accept()
        #     # 用过sys.exit(0)和sys.exit(app.exec_())，但没起效果
        #     os._exit(0)
        # else:
        #     event.ignore()

        event.accept()
        # 用过sys.exit(0)和sys.exit(app.exec_())，但没起效果
        os._exit(0)


if __name__ == "__main__":
    def main():
        # 实例化 PyQt后台管理
        app = QApplication(sys.argv)

        # 实例化 主窗口
        my_main_window = MyMainWindow0()

        my_main_window.show()

        # 运行主循环，必须调用此函数才可以开始事件处理
        sys.exit(app.exec_())


    main()
