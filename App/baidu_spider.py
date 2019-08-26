# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
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


class UiForm(object):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(500, 350)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 40, 251, 171))
        self.textEdit.setObjectName("textEdit")
        # str = '要显示的字符串'
        # self.textEdit.setText(str)
        # str1 = self.textEdit.toPlainText()
        # print(str1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BaiDuSpider"))
        self.label.setText(_translate("Form", "KeyWords:"))
        self.pushButton.setText(_translate("Form", "抓取"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.pushButton.clicked.connect(self.btnPress1_clicked)
        self.pushButton_2.clicked.connect(self.btnPress2_clicked)

    def btnPress1_clicked(self):
        # 以文本的形式输出到多行文本框
        # self.textEdit.setPlainText('Hello PyQt5!\n单击按钮')
        input_kws = self.textEdit.toPlainText()
        print(input_kws)
        kws = input_kws.split('\n')
        print(kws)
        print('正在抓取。。。')
        self.textEdit.setText("正在抓取。。。")
        bd_spider = BaiDuSpider(kws)
        bd_spider.run()
        self.textEdit.setText("抓取完成！")
        print('抓取完成！')

    def btnPress2_clicked(self):
        # 以Html的格式输出多行文本框，字体红色，字号6号
        self.textEdit.setHtml("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = UiForm()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
