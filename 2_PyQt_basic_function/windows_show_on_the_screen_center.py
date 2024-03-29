import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    """
    窗口显示在屏幕的中间
    下面的脚本显示了如何在屏幕中心显示窗口。
    QtGui,QDesktopWidget类提供了用户的桌面信息,包括屏幕大小。
    """

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(500, 300)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())