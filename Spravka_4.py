from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from Spravka_5 import *
spis = []
with open('Spisok.txt', "r", encoding = "UTF-8") as file:
    for line in file:
        spis.append(line)
     
class FouWin(QWidget):
    def __init__(self, da1):
        ''' окно проверки ИНН '''
        super().__init__()
        self.da1 = da1
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # создаём и настраиваем графические элементы:
        self.initUI()
        #устанавливает связи между элементами
        self.connects()
        # старт:
        self.show()
        #проверка работы
        #print(self.da1)

    def initUI(self):
        ''' создаёт графические элементы '''
        self.title1 = QLabel('Введите ИНН')
        self.title2 = QLabel()
        self.button = QPushButton('Проверить')
        self.button.setStyleSheet('QPushButton {font-size: 16pt;}')
        self.INN = QLineEdit('')
        self.INN.setPlaceholderText('Здесь введите ИНН')
        self.INN.setStyleSheet('QLineEdit {font-size: 16pt;}')
                       
        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.title1, alignment = Qt.AlignCenter)
        self.layoutV.addWidget(self.title2, alignment = Qt.AlignCenter)
        self.layoutV.addWidget(self.INN, alignment = Qt.AlignCenter)
        self.layoutV.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layoutV)
  
    def next_prov(self):
        INN_VV = self.INN.text()
        if len(INN_VV) == 10 or len(INN_VV) == 12:
            if INN_VV in spis:
                self.da1.append(True)
            else:
                self.da1.append(False)
            self.five = FivWin(self.da1)
            self.hide()
        else:
            self.title2.setText('Введен неверный ИНН')
        
    def connects(self):
        self.button.clicked.connect(self.next_prov)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle('Выбор справки')
        self.resize(500, 200)
        self.move(900, 70)
