import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog, QApplication, QMainWindow, QInputDialog, QMessageBox
from bus_class import Bus

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>835</width>
    <height>678</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="2" column="1">
     <widget class="Line" name="line">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
    </item>
    <item row="2" column="0">
     <widget class="QTextEdit" name="textEdit"/>
    </item>
    <item row="1" column="0">
     <widget class="QPushButton" name="pushButton">
      <property name="text">
       <string>Выпуск на линию</string>
      </property>
     </widget>
    </item>
    <item row="0" column="0">
     <widget class="QLabel" name="label">
      <property name="text">
       <string>Автобусы в парке</string>
      </property>
     </widget>
    </item>
    <item row="0" column="2">
     <widget class="QLabel" name="label_2">
      <property name="text">
       <string>Автобусы на маршруте</string>
      </property>
     </widget>
    </item>
    <item row="2" column="2">
     <widget class="QTextEdit" name="textEdit_2"/>
    </item>
    <item row="1" column="2">
     <widget class="QPushButton" name="pushButton_2">
      <property name="text">
       <string>Возврат в парк</string>
      </property>
     </widget>
    </item>
    <item row="3" column="0" colspan="3">
     <widget class="QPushButton" name="pushButton_3">
      <property name="text">
       <string>Добавить автобус</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>835</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
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

buslist_park = [Bus('777', 'Иванов Иван Иванович', '15'),
                Bus('111', 'Петров Петр Петрович', '11'),
                Bus('333', 'Семенов Семен Семенович', '8'),
                Bus('001', 'Баранов Конствнтин Юрьевич', '15'),
                Bus('002', 'Филимонов Федор Михайлович', '11'),
                Bus('003', 'Сапелкин Дмитрий Инокентьевич', '8')]
buslist_rout = []


def add_bus_park(num):
    global buslist_park, buslist_rout
    buslist_park.append(*list(filter(lambda x: x.car_number == num, buslist_rout)))
    buslist_rout = list(filter(lambda x: x.car_number != num, buslist_rout))


def add_bus_rout(num):
    global buslist_park, buslist_rout
    buslist_rout.append(*list(filter(lambda x: x.car_number == num, buslist_park)))
    buslist_park = list(filter(lambda x: x.car_number != num, buslist_park))


def add_bus(bus):
    buslist_park.append(bus)


class BusPark(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setWindowTitle('Управление автопарком')
        self.initUI()

    def initUI(self):
        self.update_buslists()
        self.pushButton.clicked.connect(self.add_rout)
        self.pushButton_2.clicked.connect(self.add_park)
        self.pushButton_3.clicked.connect(self.add_bus)

    def update_buslists(self):
        self.buslist_park = buslist_park
        self.buslist_rout = buslist_rout
        self.textEdit.clear()
        self.textEdit_2.clear()

        for bus in self.buslist_park:
            self.textEdit.insertPlainText(f'{bus.get_data()[0]} - {bus.get_data()[1]} - {bus.get_data()[2]}\n')

        for bus in self.buslist_rout:
            self.textEdit_2.insertPlainText(f'{bus.get_data()[0]} - {bus.get_data()[1]} - {bus.get_data()[2]}\n')

    def add_rout(self):
        try:
            bus_list = []
            for bus in self.buslist_park:
                bus_list.append(bus.get_data()[0])
            num, ok_pressed = QInputDialog.getItem(
                self, "Выезд на маршрут", "Выберете номер автобуса",
                (bus_list), 1, False)
            if ok_pressed:
                add_bus_rout(num)
                self.update_buslists()
        except Exception:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Автобуса с таким номером нет в парке!")
            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                print("OK!")

    def add_park(self):
        try:
            bus_list = []
            for bus in self.buslist_rout:
                bus_list.append(bus.get_data()[0])
            num, ok_pressed = QInputDialog.getItem(
                self, "Возврат в парк", "Выберете номер автобуса",
                (bus_list), 1, False)
            if ok_pressed:
                add_bus_park(num)
                self.update_buslists()
        except Exception:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Автобус с таким номером на маршрут не выезжал!")
            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                print("OK!")

    def add_bus(self):
        self.second_form = AddBusPark(self)
        self.second_form.show()


class AddBusPark(QMainWindow):
    def __init__(self, other):
        self.other = other
        super().__init__()
        f = io.StringIO(template_2)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.close)

    def save(self):
        if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text():
            buslist_park.append(Bus(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()))
            self.other.update_buslists()
            self.close()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Заполните все поля")
            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                pass



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = BusPark()
    ex.show()
    sys.exit(app.exec())
