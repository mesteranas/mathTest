import sys
from custome_errors import *
sys.excepthook = my_excepthook
import winsound
import random
import gui
import guiTools
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt,QTimer
language.init_translation()
class main1 (qt.QMainWindow):
    def __init__(self,level):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        self.timer=QTimer()
        if level==1:
            self.a1=4
            self.a2=10
        elif level==2:
            self.a1=6
            self.a2=20
        elif level==3:
            self.a1=10
            self.a2=50
        elif level==4:
            self.a1=15
            self.a2=75
        elif level==5:
            self.a1=20
            self.a2=100
        elif level==6:
            self.a1=30
            self.a2=500
        elif level==7:
            self.a1=30
            self.a2=1000
        elif level==8:
            self.a1=50
            self.a2=10000
        elif level==9:
            self.a1=75
            self.a2=1000000
        elif level==10:
            self.a1=200
            self.a2=1000000000
        layout=qt.QVBoxLayout()
        self.rmaining=qt.QLabel(_("remaining time :60"))
        layout.addWidget(self.rmaining)
        self.question        =qt.QLineEdit()
        self.question.setReadOnly(True)
        self.question.setAccessibleName(_("question"))
        layout.addWidget(self.question)
        self.re=qt.QDoubleSpinBox()
        self.re.setRange(-10000000,10000000)
        self.re.setAccessibleName(_("result"))
        layout.addWidget(self.re)
        self.sub=qt.QPushButton(_("submit"))
        self.sub.setDefault(True)
        self.sub.clicked.connect(self.onsub)
        layout.addWidget(self.sub)
        self.uestion()
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.timer.timeout.connect(self.uptime)
        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def uptime(self):
        t=int(self.rmaining.text().split(":")[1])
        t-=1
        if t==0:
            self.timer.stop()
            self.rmaining.setText(_("remaining time :60"))
            qt.QMessageBox.information(self,_("alert"),_("the time has been ended you'll go to next question"))
            self.uestion()
        else:
            self.rmaining.setText(str(_("remaining time :{}".format(t))))

    def uestion(self):
        try:
            self.timer.stop()
            self.rmaining.setText("remaining time :60")
        except:
            pass
        c=random.randint(2,self.a1)
        o=["+","-","*"]
        r=[]
        for _ in range(c):
            t=str(random.randint(1,self.a2))
            r.append(t)
            r.append(random.choice(o))
        r.pop(-1)
        self.question.setText("".join(r))
        self.timer.start(1000)
    def onsub(self):
        a=eval(self.question.text())
        if a==self.re.value():
            qt.QMessageBox.information(self,_("done"),_("great"))
        else:
            qt.QMessageBox.information(self,_("error"),_("the true anser is {}".format(a)))
        self.uestion()
class main(qt.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(_("select your level in this test"))
        self.l=qt.QSlider()
        self.l.setRange(1,10)
        self.l.setAccessibleName(_("level"))
        self.next=qt.QPushButton(_("next"))
        self.next.setDefault(True)
        self.next.clicked.connect(self.m)
        layout=qt.QVBoxLayout()
        layout.addWidget(self.l)
        layout.addWidget(self.next)
        self.setLayout(layout)
    def m(self):
        self.hide()
        main1(self.l.value()).show()

App=qt.QApplication([])
w=main()
w.show()
App.exec()