from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from Spravka_2 import *
     
class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # создаём и настраиваем графические элементы:
        self.initUI()
        #устанавливает связи между элементами
        self.connects()
        # старт:
        self.show()

    def initUI(self):
        ''' создаёт графические элементы '''
        self.btn_da = QPushButton('ДА')
        self.btn_da.setStyleSheet('QPushButton {font-size: 16pt;}')
        self.btn_net = QPushButton('НЕТ')
        self.btn_net.setStyleSheet('QPushButton {font-size: 16pt;}')
        self.vopr11 = QLabel('Относится к организациям')
        self.vopr12 = QLabel('со 100% государственным участием?')
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
        da1 = [True]
        self.two = SecWin(da1)
        self.hide()
    
    def next_net(self):
        da1 = [False]
        self.two = SecWin(da1)
        self.hide()
    
    def connects(self):
        self.btn_da.clicked.connect(self.next_da)
        self.btn_net.clicked.connect(self.next_net)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle('Выбор справки')
        self.resize(500, 200)
        self.move(900, 70)

def main():
    app = QApplication([])
    app.setStyleSheet("QLabel{font-size: 16pt;}")
    mw = MainWin()
    app.exec_()

main()