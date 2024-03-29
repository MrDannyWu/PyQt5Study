# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import requests
from bs4 import BeautifulSoup
import datetime


class BaiDuSpider(object):
    """
    Baidu Spider
    """
    # def __init__(self, kws, pages):
    #     self.kws = kws
    #     self.pages = pages
    def __init__(self, kws):
        self.kws = kws
        # self.pages = pages

    def get_html(self, url, header):
        try:
            resp = requests.get(url, headers=header)
            resp.encoding = 'utf-8'
            return resp.text, resp.url
        except:
            try:
                resp = requests.get(url, headers=header)
                resp.encoding = 'utf-8'
                return resp.text, resp.url
            except:
                # print(requests.get(url, headers=header))
                # print('Connection Error!')
                return '', ''

    def parse(self, kw, response, file_name):
        # html = etree.HTML(response)
        soup = BeautifulSoup(response, 'lxml')
        items = soup.select('#content_left .c-container h3 a')
        for item in items:
            title = item.text
            baidu_url = item.get('href')
            # print(title, baidu_url)
            # resp = requests.get()
            response = self.get_html(baidu_url, '')
            # resp = requests.get(baidu_url)
            # article_url = resp.url
            # print(kw, title, baidu_url, response[1])
            with open(file_name, 'a', encoding='utf-8')as f:
                f.write(kw.replace(',', '') + ',' + title.strip().replace(',', '') + ',' + baidu_url.strip() + ',' + response[1].strip() + '\n')

    def run(self):
        # page为0 10 20
        file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + 'baidu_search_results.csv'
        with open(file_name, 'w')as f:
            f.write('kw,title,baidu_url,article_url' + '\n')
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'BIDUPSID=873B1CF1320F20F15C87A2F2B1EC5A6F; PSTM=1564986934; BD_UPN=12314753; BAIDUID=026A2884882CF38C5E121381F2F8691A:FG=1; BDUSS=NRS3FBVjdUamhmcnJsZS04LXc0Vm9RYUZueE94TlJSTTV3OVRGTTZhcDFXMjlkSVFBQUFBJCQAAAAAAAAAAAEAAAB-vqpjztLP687Ssru5u7rDYW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHXOR111zkddZV; H_PS_PSSID=29493_1457_21098_29522_29521_29099_29568_29221_26350_29459; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=7; sug=3; sugstore=0; ORIGIN=0; bdime=0; COOKIE_SESSION=1316_0_6_3_0_4_0_0_4_3_0_0_0_0_0_0_0_0_1566789077%7C6%230_0_1566782230%7C1; H_PS_645EC=d0bbERl3iVeyBGan7bn8rzdW2Va1vxXlmJbBPKIJNLPpMVRynAzzOO5yZuM',
            'Host': 'www.baidu.com',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        base_url = 'https://www.baidu.com/s?wd={}&pn={}'
        for kw in self.kws:
            for i in range(3):
                url = base_url.format(kw.strip(), i*10)
                response = self.get_html(url, header)
                # print(response)
                self.parse(kw.strip(), response[0], file_name)


class UiMainWindow(object):

    def get_html(self, url, header):
        try:
            resp = requests.get(url, headers=header)
            resp.encoding = 'utf-8'
            return resp.text, resp.url
        except:
            try:
                resp = requests.get(url, headers=header)
                resp.encoding = 'utf-8'
                return resp.text, resp.url
            except:
                # print(requests.get(url, headers=header))
                # print('Connection Error!')
                return '', ''

    def parse(self, kw, response, file_name):
        # html = etree.HTML(response)
        soup = BeautifulSoup(response, 'lxml')
        items = soup.select('#content_left .c-container h3 a')
        for item in items:
            title = item.text
            baidu_url = item.get('href')
            # print(title, baidu_url)
            # resp = requests.get()
            response = self.get_html(baidu_url, '')
            # resp = requests.get(baidu_url)
            # article_url = resp.url
            # print(kw, title, baidu_url, response[1])
            with open(file_name, 'a', encoding='utf-8')as f:
                f.write(kw.replace(',', '') + ',' + title.strip().replace(',', '') + ',' + baidu_url.strip() + ',' + response[1].strip() + '\n')

    def run(self, kws):
        # page为0 10 20
        file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + 'baidu_search_results.csv'
        with open(file_name, 'w')as f:
            f.write('kw,title,baidu_url,article_url' + '\n')
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'BIDUPSID=873B1CF1320F20F15C87A2F2B1EC5A6F; PSTM=1564986934; BD_UPN=12314753; BAIDUID=026A2884882CF38C5E121381F2F8691A:FG=1; BDUSS=NRS3FBVjdUamhmcnJsZS04LXc0Vm9RYUZueE94TlJSTTV3OVRGTTZhcDFXMjlkSVFBQUFBJCQAAAAAAAAAAAEAAAB-vqpjztLP687Ssru5u7rDYW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHXOR111zkddZV; H_PS_PSSID=29493_1457_21098_29522_29521_29099_29568_29221_26350_29459; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=7; sug=3; sugstore=0; ORIGIN=0; bdime=0; COOKIE_SESSION=1316_0_6_3_0_4_0_0_4_3_0_0_0_0_0_0_0_0_1566789077%7C6%230_0_1566782230%7C1; H_PS_645EC=d0bbERl3iVeyBGan7bn8rzdW2Va1vxXlmJbBPKIJNLPpMVRynAzzOO5yZuM',
            'Host': 'www.baidu.com',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        base_url = 'https://www.baidu.com/s?wd={}&pn={}'
        for kw in kws:
            for i in range(3):
                url = base_url.format(kw.strip(), i*10)
                response = self.get_html(url, header)
                # print(response)
                self.parse(kw.strip(), response[0], file_name)

    def setupUi(self, MainWindow):
        # 新建一个主窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 350)

        # 设置ico图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # 设置背景图片
        # palette = QtGui.QPalette()
        # palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("bk.jpg")))
        # win.setPalette(palette)

        # 主窗体居中
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 新建标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 新建文本输入框
        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(120, 40, 251, 171))
        self.textEdit.setObjectName("textEdit")
        # self.textEdit.setStyleSheet("textEdit{background: transparent;}")

        # 新建确定按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")

        # 新建清空按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage('就绪')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "百度爬虫-DannyWu"))
        self.label.setText(_translate("Form", "关键词:"))
        self.pushButton.setText(_translate("Form", "抓取"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.pushButton.clicked.connect(self.btnPress1_clicked)
        self.pushButton_2.clicked.connect(self.btnPress2_clicked)

    def btnPress1_clicked(self):
        # 以文本的形式输出到多行文本框
        # self.textEdit.setPlainText('Hello PyQt5!\n单击按钮')
        input_kws = self.textEdit.toPlainText()

        print(input_kws)
        kws_split = input_kws.split('\n')
        if len(kws_split) == 1 and kws_split[0].strip() == '':
            self.statusbar.showMessage('请输入一个或多个关键词！')
            # self.textEdit.setText("请输入一个或多个关键词！")
        else:
            # self.statusbar.showMessage('正在抓取。。。')
            print(len(kws_split))
            self.textEdit.setText("正在抓取。。。")
            kws = []
            for i in kws_split:
                if i != '':
                    kws.append(i)
            print(kws)
            print('正在抓取。。。')

            # bd_spider = BaiDuSpider(kws)
            # bd_spider.run()
            self.run(kws)
            self.textEdit.setText("抓取完成！")
            self.statusbar.showMessage('抓取完成')
            print('抓取完成！')

    def btnPress2_clicked(self):
        # 以Html的格式输出多行文本框，字体红色，字号6号
        self.textEdit.setHtml("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # widget = QtWidgets.QWidget()
    win = QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())