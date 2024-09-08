import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout,          QGridLayout, QPushButton)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("MY cool first GUI")
    self.setGeometry(700, 300, 500, 500)
    self.setWindowIcon(QIcon("PYTHON MINI PROJECTS/PyQt5 projects/dog.jpg"))
    self.button = QPushButton("Click me!", self)
    self.label = QLabel("Hello", self)
    self.initUI()
    '''
    label = QLabel( self)
    label.setFont(QFont("Arial", 40))
    label.setGeometry(0,0, 500, 100)
    label.setStyleSheet("color: blue;"
                        "background-color: gray;"
                        "font-weight: bold;"
                        "font-style: italic;"
                        "text-decoration: underline;")
    
    label.setAlignment(Qt.AlignCenter)
    
    pixmap = QPixmap("PYTHON MINI PROJECTS/PyQt5 projects/dog.jpg")
    label.setGeometry(0,0, 250, 250)
    label.setPixmap(pixmap)
    label.setScaledContents(True)

    label.setGeometry((self.width() - label.width()) // 2, 
                      (self.height() - label.height()) // 2, 
                      label.width(), 
                      label.height())'''
  
  def initUI(self):
    
    self.button.setGeometry(150, 200, 200, 100)
    self.button.setStyleSheet("font-size: 30px;")
    self.button.clicked.connect(self.on_click)

    self.label.setGeometry(150, 300, 200, 100)
    self.label.setStyleSheet("font-size: 50px;")

  def on_click(self):
    self.label.setText("Goodbye")
    '''
    self.button.setText("Clicked")
    self.button.setDisabled(True)'''
    '''
    central_widget = QWidget()
    self.setCentralWidget(central_widget)

    label1 = QLabel("#1", self)
    label2 = QLabel("#2", self)
    label3 = QLabel("#3", self)
    label4 = QLabel("#4", self)
    label5 = QLabel("#5", self)

    label1.setStyleSheet("background-color: red;")
    label2.setStyleSheet("background-color: yellow;")
    label3.setStyleSheet("background-color: green;")
    label4.setStyleSheet("background-color: blue;")
    label5.setStyleSheet("background-color: purple;")

    vbox = QVBoxLayout()

    vbox.addWidget(label1)
    vbox.addWidget(label2)
    vbox.addWidget(label3)
    vbox.addWidget(label4)
    vbox.addWidget(label5)

    central_widget.setLayout(vbox) '''






def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()