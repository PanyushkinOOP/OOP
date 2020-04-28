from PyQt5 import QtWidgets, QtCore
import sys,os 

class buttonForm(QtWidgets.QWidget):
  def __init__(self,parrent=None):
    QtWidgets.QWidget.__init__(self,parrent)
    
    self.__buttonsVBox=QtWidgets.QVBoxLayout()
    self.__newButton=QtWidgets.QPushButton(u"Добавить")
    self.__editButton=QtWidgets.QPushButton(u"Изменить")
    self.__delButton=QtWidgets.QPushButton(u"Удалить")
    
    self.__buttonsVBox.addWidget(self.__newButton)
    self.__buttonsVBox.addWidget(self.__editButton)
    self.__buttonsVBox.addWidget(self.__delButton)
    self.__buttonsVBox.addStretch(1)
    
    self.setLayout(self.__buttonsVBox)
    
    self.connect(self.__newButton,QtCore.SIGNAL('clicked()'),self.newClick)
    self.connect(self.__editButton,QtCore.SIGNAL('clicked()'),self.editClick)
    self.connect(self.__delButton,QtCore.SIGNAL('clicked()'),self.delClick)
  def newClick(self):self.emit(QtCore.SIGNAL('newRec()'))
  def editClick(self):self.emit(QtCore.SIGNAL('editRec()'))
  def delClick(self):self.emit(QtCore.SIGNAL('delRec()'))
