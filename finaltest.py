import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox  
from timetabletest import Ui_Data_form
class Ui_Data_form(object):
    def setupUi(self, Data_form):
        
        Data_form.setObjectName("Data_form")
        Data_form.resize(828, 655)
        Data_form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Data_form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(Data_form)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 801, 571))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 10, 491, 551))
        self.label.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 491, 551))
        self.label_2.setStyleSheet("background-image:url(G:/python files/class.gif);\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 411, 551))
        self.label_3.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-bottom-right-radius:50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(180, 150, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(180, 100, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(180, 200, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(180, 250, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(180, 300, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(180, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(180, 400, 170, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(510, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Professor = QtWidgets.QLineEdit(self.widget)
        self.Professor.setGeometry(QtCore.QRect(400, 100, 330, 21))
        self.Professor.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.Professor.setObjectName("Professor")
        self.Course = QtWidgets.QLineEdit(self.widget)
        self.Course.setGeometry(QtCore.QRect(400, 150, 330, 21))
        self.Course.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.Course.setObjectName("Course")
        self.duration = QtWidgets.QLineEdit(self.widget)
        self.duration.setGeometry(QtCore.QRect(400, 250, 330, 21))
        self.duration.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.duration.setObjectName("duration")
        self.CourseCode = QtWidgets.QLineEdit(self.widget)
        self.CourseCode.setGeometry(QtCore.QRect(400, 200, 330, 21))
        self.CourseCode.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.CourseCode.setObjectName("CourseCode")
        self.group = QtWidgets.QLineEdit(self.widget)
        self.group.setGeometry(QtCore.QRect(400, 300, 330, 21))
        self.group.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.group.setObjectName("group")
        self.room = QtWidgets.QLineEdit(self.widget)
        self.room.setGeometry(QtCore.QRect(400, 350, 330, 21))
        self.room.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.room.setObjectName("room")
        self.lab = QtWidgets.QLineEdit(self.widget)
        self.lab.setGeometry(QtCore.QRect(400, 390, 330, 21))
        self.lab.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.lab.setObjectName("lab")
        self.data = QtWidgets.QPushButton(self.widget)
        self.data.setGeometry(QtCore.QRect(510, 430, 101, 41))
        self.data.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 131, 120, 219), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 131, 120, 219), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(85, 98, 112, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-left:5px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))\n"
"\n"
"}\n"
"\n"
"")
        self.data.setObjectName("data")
        self.cancelData = QtWidgets.QPushButton(self.widget)
        self.cancelData.setGeometry(QtCore.QRect(400, 500, 121, 21))
        self.cancelData.setStyleSheet("background-color:rgba(93, 192, 184,0.8);")
        self.cancelData.setObjectName("cancelData")
        self.Start_solving = QtWidgets.QPushButton(self.widget)
        self.Start_solving.setGeometry(QtCore.QRect(600, 500, 131, 21))
        self.Start_solving.setStyleSheet("background-color:rgba(93, 192, 184,0.8);")
        self.Start_solving.setObjectName("Start_solving")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(360, 10, 91, 91))
        self.label_12.setStyleSheet("border-image:url(G:/python files/logo1.png);\n"
"")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_10.raise_()
        self.Professor.raise_()
        self.Course.raise_()
        self.duration.raise_()
        self.CourseCode.raise_()
        self.group.raise_()
        self.room.raise_()
        self.lab.raise_()
        self.data.raise_()
        self.cancelData.raise_()
        self.Start_solving.raise_()
        self.label_12.raise_()
        Data_form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Data_form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 21))
        self.menubar.setObjectName("menubar")
        Data_form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Data_form)
        self.statusbar.setObjectName("statusbar")
        Data_form.setStatusBar(self.statusbar)

        self.retranslateUi(Data_form)
        QtCore.QMetaObject.connectSlotsByName(Data_form)

        self.data.clicked.connect(self.on_adddata)
        self.cancelData.clicked.connect(self.on_cancel)


    def retranslateUi(self, Data_form):
        _translate = QtCore.QCoreApplication.translate
        Data_form.setWindowTitle(_translate("Data_form", "MainWindow"))
        self.label_4.setText(_translate("Data_form", "Name Of Course:"))
        self.label_5.setText(_translate("Data_form", "Name Of Lecturer:"))
        self.label_6.setText(_translate("Data_form", "Subject Course Code:"))
        self.label_7.setText(_translate("Data_form", "Number Of Hours:"))
        self.label_8.setText(_translate("Data_form", "Number of Batches :"))
        self.label_9.setText(_translate("Data_form", "Name of Lab"))
        self.label_11.setText(_translate("Data_form", "Practical(true/False):"))
        self.label_10.setText(_translate("Data_form", "Data Entry"))
        self.Professor.setPlaceholderText(_translate("Data_form", "Name Of Lecturer:"))
        self.Course.setPlaceholderText(_translate("Data_form", "Name Of Course:"))
        self.duration.setPlaceholderText(_translate("Data_form", "Number Of Hours:"))
        self.CourseCode.setPlaceholderText(_translate("Data_form", "Subject Course Code:"))
        self.group.setPlaceholderText(_translate("Data_form", "Number of Batches:"))
        self.room.setPlaceholderText(_translate("Data_form", "Name of Lab"))
        self.lab.setPlaceholderText(_translate("Data_form", "Practical(true/False):"))
        self.data.setText(_translate("Data_form", "ADD_DATA"))
        self.cancelData.setText(_translate("Data_form", "Cancel_cancelData"))
        self.Start_solving.setText(_translate("Data_form", "Start Solving"))
    def on_adddata(self):
       
        professor = self.Professor.text()
        course = self.Course.text()
        course_code = self.CourseCode.text()
        duration = self.duration.text()
        group_name = self.group.text()
        room = self.room.text()
        lab = self.lab.text()

       
        db = mysql.connector.connect(host='localhost', user='root', password='Tan@9045', database='timetable')
        cursor = db.cursor()

       
        try:
            query = 'INSERT INTO data (professor, course, course_code, duration , group_name, room, lab ) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            data_tuple = (professor, course, course_code, duration , group_name, room, lab)

            cursor.execute(query, data_tuple)
            db.commit()

            QMessageBox.information(None, 'Success', 'Data added successfully!', QMessageBox.Ok)
        except mysql.connector.Error as err:
            QMessageBox.critical(None, 'Error', f'Database error: {err}', QMessageBox.Ok)
        finally:
            cursor.close()
            db.close()


    def on_cancel(self):
        self.Professor.clear()
        self.Course.clear()
        self.duration.clear()
        self.CourseCode.clear()
        self.group.clear()
        self.room.clear()
        self.lab.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Data_form = QtWidgets.QMainWindow()
    ui = Ui_Data_form()
    ui.setupUi(Data_form)
    Data_form.show()
    sys.exit(app.exec_())
