# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assignment2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate


class Ui_Vaccine_Day_Calculator(object):
    def setupUi(self, Vaccine_Day_Calculator):
        Vaccine_Day_Calculator.setObjectName("Vaccine_Day_Calculator")
        Vaccine_Day_Calculator.resize(713, 518)
        self.centralwidget = QtWidgets.QWidget(Vaccine_Day_Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 451, 121))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(20)
        font.setItalic(False)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.calendarWidget_Current = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_Current.setGeometry(QtCore.QRect(20, 170, 312, 183))
        self.calendarWidget_Current.setMinimumDate(QDate.currentDate())#to keep caledars to current date
        self.calendarWidget_Current.setMaximumDate(QDate.currentDate())#to prevent from any negative due dates
        self.calendarWidget_Current.setObjectName("calendarWidget_Current")
        self.calendarWidget_Vaccine = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_Vaccine.setGeometry(QtCore.QRect(370, 170, 312, 183))
        self.calendarWidget_Vaccine.setMinimumDate(QDate.currentDate())#to keep calendars to current date
        self.calendarWidget_Vaccine.setMaximumDate(QtCore.QDate(2024, 12, 31))
        self.calendarWidget_Vaccine.setObjectName("calendarWidget_Vaccine")
        self.lblCurrent = QtWidgets.QLabel(self.centralwidget)
        self.lblCurrent.setGeometry(QtCore.QRect(80, 140, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(12)
        self.lblCurrent.setFont(font)
        self.lblCurrent.setObjectName("lblCurrent")
        self.lblSelectVac = QtWidgets.QLabel(self.centralwidget)
        self.lblSelectVac.setGeometry(QtCore.QRect(370, 140, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(12)
        self.lblSelectVac.setFont(font)
        self.lblSelectVac.setObjectName("lblSelectVac")
        self.lblDisplayDays = QtWidgets.QLabel(self.centralwidget)
        self.lblDisplayDays.setGeometry(QtCore.QRect(60, 360, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblDisplayDays.setFont(font)
        self.lblDisplayDays.setObjectName("lblDisplayDays")
        self.btnCalcVac = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcVac.setGeometry(QtCore.QRect(20, 410, 211, 41))
        self.btnCalcVac.setObjectName("btnCalcVac")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(470, 410, 231, 41))
        self.btnExit.setObjectName("btnExit")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(250, 410, 201, 41))
        self.btnReset.setObjectName("btnReset")
        Vaccine_Day_Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Vaccine_Day_Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName("menubar")
        Vaccine_Day_Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Vaccine_Day_Calculator)
        self.statusbar.setObjectName("statusbar")
        Vaccine_Day_Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Vaccine_Day_Calculator)
        QtCore.QMetaObject.connectSlotsByName(Vaccine_Day_Calculator)

        self.btnCalcVac.clicked.connect(self.vacCal)#connects function to the button that calculates days
        self.btnReset.clicked.connect(self.calClr)#connects clear button to the clear label function
        self.btnExit.clicked.connect(self.exitAp)#connects exit application button
        

    def retranslateUi(self, Vaccine_Day_Calculator):
        _translate = QtCore.QCoreApplication.translate
        Vaccine_Day_Calculator.setWindowTitle(_translate("Vaccine_Day_Calculator", "Vaccine_Day_Calculator"))
        self.label.setText(_translate("Vaccine_Day_Calculator", "Covid 19 Vaccine time tracker"))
        self.lblCurrent.setText(_translate("Vaccine_Day_Calculator", "This is the current date:"))
        self.lblSelectVac.setText(_translate("Vaccine_Day_Calculator", "select the date of your vaccination:"))
        self.lblDisplayDays.setText(_translate("Vaccine_Day_Calculator", "(The amount of time left until your vaccine will be displayed here)"))
        self.btnCalcVac.setText(_translate("Vaccine_Day_Calculator", "Calculate the time until your vaccination"))
        self.btnExit.setText(_translate("Vaccine_Day_Calculator", "Exit Application"))
        self.btnReset.setText(_translate("Vaccine_Day_Calculator", "Reset Calander dates to current date"))

    def vacCal(self):#function to calculate the days
        cur = self.calendarWidget_Current.selectedDate()#variable for current date
        vac = self.calendarWidget_Vaccine.selectedDate()#variable for vaccine date
        nofdays = cur.daysTo(vac)#Days to function subtracts the amount of days and converts it to days/integer format

        if nofdays == 0:#if statement if vaccine day is the same day as the current day
            self.lblDisplayDays.setText(f'Your vaccine is due today please go get it!')
        elif nofdays > 0:#if statement if vaccine day is anytime after current day
            self.lblDisplayDays.setText(f'Your Vaccine is due in {nofdays} days!')

    def calClr(self):#resets label to clear days displayed
        self.lblDisplayDays.setText("(The amount of time left until your vaccine will be displayed here)")

    def exitAp(self):#to exit application
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vaccine_Day_Calculator = QtWidgets.QMainWindow()
    ui = Ui_Vaccine_Day_Calculator()
    ui.setupUi(Vaccine_Day_Calculator)
    Vaccine_Day_Calculator.show()
    sys.exit(app.exec_())
