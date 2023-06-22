from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QTextBrowser, \
    QGridLayout, QLineEdit
from PyQt6.QtCore import Qt, QRegularExpression, pyqtSlot


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.labelbinaer = QLabel("Binärzahl:", self)

        self.labelhexa = QLabel("Hexadezimalzahl:", self)

        self.bin = QLineEdit(self)
        self.bin.setInputMask("Bbbbbbbb")

        self.hex = QLineEdit(self)
        self.hex.setInputMask("HH")

        self.bin.setText("0")
        self.hex.setText("0")

        self.bin.editingFinished.connect(self.calc)
        self.hex.editingFinished.connect(self.calc)

        self.textbrowser = QTextBrowser(self)
        self.textbrowser.resize(80, 120)

        self.buttonrechnen = QPushButton("Berechnen", self)

        self.buttonschliesen = QPushButton("Schließen", self)
        self.buttonschliesen.clicked.connect(QApplication.instance().quit)
        self.buttonschliesen.setFixedWidth(150)
        self.buttonschliesen.setFixedHeight(30)

        layout = QGridLayout(self)
        layout.addWidget(self.labelbinaer)
        layout.addWidget(self.bin)
        layout.addWidget(self.labelhexa)
        layout.addWidget(self.hex)
        layout.addWidget(self.textbrowser)
        layout.addWidget(self.buttonschliesen)
        layout.addWidget(self.buttonrechnen)

    @pyqtSlot()
    def calc(self):
        str_bin = self.bin.text()
        str_hex = self.hex.text()
        print(str_bin + str_hex)
        self.textbrowser.append(str_bin + str_hex)
