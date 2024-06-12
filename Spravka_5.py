from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

class FivWin(QWidget):
    def __init__(self, da1):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
        self.da1 = da1
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        # создаём и настраиваем графические элементы:
        self.initUI()
        #устанавливает связи между элементами
        #self.connects()
        # старт:
        self.show()
        print(self.da1)

    def initUI(self):
        ''' создаёт графические элементы '''
        if self.da1[0] or self.da1[1] or self.da1[2] or self.da1[3]:
            otvet = 'Можно сделать формальную справку'
        else:
            otvet = 'Необходимо сделать полную справку'
        self.otv1 = QLabel(otvet)
        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.otv1, alignment = Qt.AlignCenter)
        self.setLayout(self.layoutV)
  
    def connects(self):
        self.btn_da.clicked.connect(self.next_da)
        self.btn_net.clicked.connect(self.next_net)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle('Выбор справки')
        self.resize(500, 200)
        self.move(900, 70)
