from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
import sys,os
sys.path.insert(0, './store')
from datasql import datasql
from dataxml import dataxml
from store import store
from tab import tabWidget

app = QApplication(sys.argv)

def decode(qstring):
    return qstring

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(u'Ювелирный магазин')
        self.store=store()
        self.dataxml=dataxml()
        self.datasql=datasql()
        self.tabWidget=tabWidget(self.store,self)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.new=QAction(QIcon(),'New',self)
        self.new.setStatusTip('New database')
        self.new.triggered.connect(self.newAction)

        self.openxml=QAction(QIcon(),'Open XML',self)
        self.openxml.setStatusTip('Open data from XML')
        self.openxml.triggered.connect(self.openXMLAction)

        self.opensql=QAction(QIcon(),'Open SQL',self)
        self.opensql.setStatusTip('Open data from SQL')
        self.opensql.triggered.connect(self.openSQLAction)

        self.savexml=QAction(QIcon(),'Save XML',self)
        self.savexml.setStatusTip('Save data to XML')
        self.savexml.triggered.connect(self.saveXMLAction)

        self.savesql=QAction(QIcon(),'Save SQL',self)
        self.savesql.setStatusTip('Save data to SQL')
        self.savesql.triggered.connect(self.saveSQLAction)

        self.menubar=self.menuBar()
        self.menufile=self.menubar.addMenu('&File')
        self.menufile.addAction(self.new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.openxml)
        self.menufile.addAction(self.opensql)
        self.menufile.addSeparator()
        self.menufile.addAction(self.savexml)
        self.menufile.addAction(self.savesql)
        self.statusBar()

    def newAction(self):
        self.store.clean()
        self.tabWidget.update()

    def openXMLAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть XML',os.getcwd(),u'*.xml')[0]
        if filename:
            self.store.clean()
            self.dataxml.read(filename,self.store)
            self.tabWidget.update()

    def openSQLAction(self):
        filename=QFileDialog.getOpenFileName(self,u'Открыть SQL',os.getcwd(),u'*.sqlite')[0]
        if filename:
            self.store.clean()
            self.datasql.read(filename,self.store)
            self.tabWidget.update()

    def saveXMLAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить XML',os.getcwd(),u'*.xml')[0]
        if filename:
            self.dataxml.write(filename,self.store)

    def saveSQLAction(self):
        filename=QFileDialog.getSaveFileName(self,u'Сохранить SQL',os.getcwd(),u'*.sqlite')[0]
        if filename:
            self.datasql.write(filename,self.store)

mw=mainWindow()
mw.show()
sys.exit(app.exec_())
