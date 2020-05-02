import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class flyDepot(QMainWindow):
    
    def __init__(self,*args, **kwargs):
        super(flyDepot, self).__init__(*args, **kwargs)

        # Generate the window in the middle of the screen
        self.setGeometry((QApplication.desktop().width())/2,
                         (QApplication.desktop().height())/2,260,160)
        self.setWindowTitle("Fly Depot v.0")

        # Widget for username field
        self.username = QLineEdit(self)
        self.username.move(20,40)
        self.username.resize(100,30)
        self.username.setPlaceholderText("Username")
        self.username.returnPressed.connect(self.loginClick)
        
        # Widget for password field
        self.password = QLineEdit(self)
        self.password.move(20,80)
        self.password.resize(100,30)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.loginClick)
        
        # Login button
        self.loginButton = QPushButton(self)
        self.loginButton.setText("Login")
        self.loginButton.resize(100,40)
        self.loginButton.move(140,60)
        self.loginButton.clicked.connect(self.loginClick)
    
        
        self.show()

    def loginClick(self):
        self.msgBox = QMessageBox()
        if self.password.text() == "fruitflies":
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("Login successful, welcome {s}".format(s=self.username.text()))
        else:
            self.msgBox.setIcon(QMessageBox.Critical)
            self.msgBox.setText("Login failed")
            self.msgBox.setDetailedText("Password incorrect")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Ok)
        self.msgBox.exec_()

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = flyDepot()
    sys.exit(app.exec_())