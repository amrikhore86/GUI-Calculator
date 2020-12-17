from PyQt5 import QtCore, QtGui, QtWidgets
from operator import eq


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.eq=''
        self.count=-1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 10, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.display.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.display.setAutoFillBackground(False)
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 100, 341, 391))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.clear_all = QtWidgets.QPushButton(self.groupBox)
        self.clear_all.setGeometry(QtCore.QRect(10, 20, 81, 61))
        self.clear_all.setObjectName("clear_all")
        self.div = QtWidgets.QPushButton(self.groupBox)
        self.div.setGeometry(QtCore.QRect(250, 20, 81, 61))
        self.div.setObjectName("div")
        self.dlt = QtWidgets.QPushButton(self.groupBox)
        self.dlt.setGeometry(QtCore.QRect(170, 20, 81, 61))
        self.dlt.setObjectName("dlt")
        self.clear = QtWidgets.QPushButton(self.groupBox)
        self.clear.setGeometry(QtCore.QRect(90, 20, 81, 61))
        self.clear.setObjectName("clear")
        self.but7 = QtWidgets.QPushButton(self.groupBox)
        self.but7.setGeometry(QtCore.QRect(10, 80, 81, 61))
        self.but7.setObjectName("but7")
        self.but8 = QtWidgets.QPushButton(self.groupBox)
        self.but8.setGeometry(QtCore.QRect(90, 80, 81, 61))
        self.but8.setObjectName("but8")
        self.but9 = QtWidgets.QPushButton(self.groupBox)
        self.but9.setGeometry(QtCore.QRect(170, 80, 81, 61))
        self.but9.setObjectName("but9")
        self.pro = QtWidgets.QPushButton(self.groupBox)
        self.pro.setGeometry(QtCore.QRect(250, 80, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pro.setFont(font)
        self.pro.setObjectName("pro")
        self.but4 = QtWidgets.QPushButton(self.groupBox)
        self.but4.setGeometry(QtCore.QRect(10, 140, 81, 61))
        self.but4.setObjectName("but4")
        self.but5 = QtWidgets.QPushButton(self.groupBox)
        self.but5.setGeometry(QtCore.QRect(90, 140, 81, 61))
        self.but5.setObjectName("but5")
        self.but6 = QtWidgets.QPushButton(self.groupBox)
        self.but6.setGeometry(QtCore.QRect(170, 140, 81, 61))
        self.but6.setObjectName("but6")
        self.sub = QtWidgets.QPushButton(self.groupBox)
        self.sub.setGeometry(QtCore.QRect(250, 140, 81, 61))
        self.sub.setObjectName("sub")
        self.but1 = QtWidgets.QPushButton(self.groupBox)
        self.but1.setGeometry(QtCore.QRect(10, 200, 81, 61))
        self.but1.setObjectName("but1")
        self.but2 = QtWidgets.QPushButton(self.groupBox)
        self.but2.setGeometry(QtCore.QRect(90, 200, 81, 61))
        self.but2.setObjectName("but2")
        self.but3 = QtWidgets.QPushButton(self.groupBox)
        self.but3.setGeometry(QtCore.QRect(170, 200, 81, 61))
        self.but3.setObjectName("but3")
        self.add = QtWidgets.QPushButton(self.groupBox)
        self.add.setGeometry(QtCore.QRect(250, 200, 81, 61))
        self.add.setObjectName("add")
        self.plusminus = QtWidgets.QPushButton(self.groupBox)
        self.plusminus.setGeometry(QtCore.QRect(10, 260, 81, 61))
        self.plusminus.setObjectName("plusminus")
        self.but0 = QtWidgets.QPushButton(self.groupBox)
        self.but0.setGeometry(QtCore.QRect(90, 260, 81, 61))
        self.but0.setObjectName("but0")
        self.dot = QtWidgets.QPushButton(self.groupBox)
        self.dot.setGeometry(QtCore.QRect(170, 260, 81, 61))
        self.dot.setObjectName("dot")
        self.equals = QtWidgets.QPushButton(self.groupBox)
        self.equals.setGeometry(QtCore.QRect(250, 260, 81, 61))
        self.equals.setObjectName("equals")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.display.setText(_translate("MainWindow", "0"))
        self.clear_all.setText(_translate("MainWindow", "CE"))
        self.div.setText(_translate("MainWindow", "/"))
        self.dlt.setText(_translate("MainWindow", "DEL"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.but7.setText(_translate("MainWindow", "7"))
        self.but8.setText(_translate("MainWindow", "8"))
        self.but9.setText(_translate("MainWindow", "9"))
        self.pro.setText(_translate("MainWindow", "x"))
        self.but4.setText(_translate("MainWindow", "4"))
        self.but5.setText(_translate("MainWindow", "5"))
        self.but6.setText(_translate("MainWindow", "6"))
        self.sub.setText(_translate("MainWindow", "-"))
        self.but1.setText(_translate("MainWindow", "1"))
        self.but2.setText(_translate("MainWindow", "2"))
        self.but3.setText(_translate("MainWindow", "3"))
        self.add.setText(_translate("MainWindow", "+"))
        self.plusminus.setText(_translate("MainWindow", "+-"))
        self.but0.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.equals.setText(_translate("MainWindow", "="))
        
        self.but0.clicked.connect(self.act_but0)
        self.but1.clicked.connect(self.act_but1)
        self.but2.clicked.connect(self.act_but2)
        self.but3.clicked.connect(self.act_but3)
        self.but4.clicked.connect(self.act_but4)
        self.but5.clicked.connect(self.act_but5)
        self.but6.clicked.connect(self.act_but6)
        self.but7.clicked.connect(self.act_but7)
        self.but8.clicked.connect(self.act_but8)
        self.but9.clicked.connect(self.act_but9)
        self.clear.clicked.connect(self.act_clear)
        self.clear_all.clicked.connect(self.act_clear_all)
        self.dlt.clicked.connect(self.act_dlt)
        self.div.clicked.connect(self.act_div)
        self.pro.clicked.connect(self.act_pro)
        self.sub.clicked.connect(self.act_sub)
        self.add.clicked.connect(self.act_add)
        self.equals.clicked.connect(self.act_equals)
        self.dot.clicked.connect(self.act_dot)
        self.plusminus.clicked.connect(self.act_plusminus)
        
        
    def act_but0(self):
        self.eq=self.eq+'0'
        self.display.setText(self.eq)
        
    def act_but1(self):
        self.eq=self.eq+'1'
        self.display.setText(self.eq)
        
    def act_but2(self):
        self.eq=self.eq+'2'
        self.display.setText(self.eq)
        
    def act_but3(self):
        self.eq=self.eq+'3'
        self.display.setText(self.eq)
        
    def act_but4(self):
        self.eq=self.eq+'4'
        self.display.setText(self.eq)
        
    def act_but5(self):
        self.eq=self.eq+'5'
        self.display.setText(self.eq)
        
    def act_but6(self):
        self.eq=self.eq+'6'
        self.display.setText(self.eq)
        
    def act_but7(self):
        self.eq=self.eq+'7'
        self.display.setText(self.eq)
        
    def act_but8(self):
        self.eq=self.eq+'8'
        self.display.setText(self.eq)
        
    def act_but9(self):
        self.eq=self.eq+'9'
        self.display.setText(self.eq)
        
    def act_clear(self):
        self.display.setText("")
        
    def act_clear_all(self):
        self.eq=''
        self.display.setText(self.eq)
        
    def act_dlt(self):
        self.eq=self.eq[:-1]
        self.display.setText(self.eq)
        
    def act_div(self):
        self.display.setText("/")
        self.eq=self.eq+'/'
        
    def act_pro(self):
        self.display.setText("*")
        self.eq=self.eq + '*'
        
    def act_sub(self):
        self.display.setText("-")
        self.eq=self.eq+'-'
        
    def act_add(self):
        self.display.setText("+")
        self.eq=self.eq+'+'
        
    def act_equals(self):
        display=self.eq
        dis=str(eval(display))
        self.display.setText(dis)
        
    def act_dot(self):
        self.eq=self.eq+'.'
        self.display.setText(self.eq)
        
    def act_plusminus(self):
        pass
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    window=Ui_MainWindow()
    window.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
    
