'''
Created on 21-Jul-2016

@author: arti
'''

import sys
from PyQt4 import QtGui

class Application(QtGui.QMainWindow):
    
    def __init__(self):
        super(Application, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.statusBar().showMessage('Ready')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()


def main():
    
    app = QtGui.QApplication(sys.argv)
    App = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()