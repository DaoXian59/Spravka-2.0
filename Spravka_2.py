from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from Spravka_3 import *
     
class SecWin(QWidget):
    def __init__(self, da1):
        ''' окно, в котором располагается приветствие '''
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
        print(self.da1)

    def initUI(self):
        ''' создаёт графические элементы '''
        self.btn_da = QPushButton('ДА')
        self.btn_da.setStyleSheet('QPushButton {font-size: 16pt;}')
        self.btn_net = QPushButton('НЕТ')
        self.btn_net.setStyleSheet('QPushButton {font-size: 16pt;}')
        self.vopr11 = QLabel('Это акционерное общество')
        self.vopr12 = QLabel('с долей участия государства более 50%?')
        self.vopr13 = QLabel('')
               
        self.layoutV = QVBoxLayout()
        self.layoutH = QHBoxLayout()
        self.layoutH.addWidget(self.btn_da)
        self.layoutH.addWidget(self.btn_net)
        self.layoutV.addWidget(self.vopr11, alignment = Qt.AlignCenter)
        self.layoutV.addWidget(self.vopr12, alignment = Qt.AlignCenter)
        self.layoutV.addWidget(self.vopr13, alignment = Qt.AlignCenter)
        self.layoutV.addLayout(self.layoutH)
        self.setLayout(self.layoutV)
  
    def next_da(self):
        self.da1.append(True)
        self.three = ThrWin(self.da1)
        self.hide()
    
    def next_net(self):
        self.da1.append(False)
        self.three = ThrWin(self.da1)
        self.hide()
    
    def connects(self):
        self.btn_da.clicked.connect(self.next_da)
        self.btn_net.clicked.connect(self.next_net)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle('Выбор справки')
        self.resize(500, 200)
        self.move(900, 70)
