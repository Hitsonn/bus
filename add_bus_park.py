import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog, QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap, QImage, QTransform, QColor
from bus_class import Bus

template_2 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>391</width>
    <height>225</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Возврат в парк</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="6" column="0">
     <widget class="QPushButton" name="pushButton">
      <property name="text">
       <string>Добавить</string>
      </property>
     </widget>
    </item>
    <item row="2" column="0">
     <widget class="QLabel" name="label_2">
      <property name="text">
       <string>ФИО водителя</string>
      </property>
     </widget>
    </item>
    <item row="4" column="0">
     <widget class="QLabel" name="label_3">
      <property name="text">
       <string>Номер маршрута</string>
      </property>
     </widget>
    </item>
    <item row="0" column="0">
     <widget class="QLabel" name="label">
      <property name="text">
       <string>Номер автобуса</string>
      </property>
     </widget>
    </item>
    <item row="6" column="1">
     <widget class="QPushButton" name="pushButton_2">
      <property name="text">
       <string>Отмена</string>
      </property>
     </widget>
    </item>
    <item row="5" column="0" colspan="2">
     <widget class="QLineEdit" name="lineEdit_3"/>
    </item>
    <item row="3" column="0" colspan="2">
     <widget class="QLineEdit" name="lineEdit_2"/>
    </item>
    <item row="1" column="0" colspan="2">
     <widget class="QLineEdit" name="lineEdit"/>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class AddBusPark(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template_2)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.close)

    def save(self):
        if self.lineEdit.text() and self.lineEdit.text() and self.lineEdit.text():
            buslist_park.append(Bus(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()))
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Заполните все поля")
            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                print("OK!")
