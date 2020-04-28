from PyQt5 import QtWidgets, QtCore
from editform import editForm

class sellsEditForm(editForm):
  def __init__(self,store,parrent=None):
    editForm.__init__(self,store,parrent=None)
    
    self.productEdit=QtWidgets.QLineEdit()
    self.dateEdit=QtWidgets.QLineEdit()
    self.surnameEdit=QtWidgets.QLineEdit()
    self.nameEdit=QtWidgets.QLineEdit()
    self.secnameEdit=QtWidgets.QLineEdit()

    self._grid.addWidget(QtWidgets.QLabel('Изделие'),0,0)
    self._grid.addWidget(self.productEdit,0,1)
    self._grid.addWidget(QtWidgets.QLabel('Дата'),1,0)
    self._grid.addWidget(self.dateEdit,1,1)
    self._grid.addWidget(QtWidgets.QLabel('Фамилия'),2,0)
    self._grid.addWidget(self.surnameEdit,2,1)
    self._grid.addWidget(QtWidgets.QLabel('Имя'),3,0)
    self._grid.addWidget(self.nameEdit,3,1)
    self._grid.addWidget(QtWidgets.QLabel('Отчество'),4,0)
    self._grid.addWidget(self.secnameEdit,4,1)
    
  def update(self):
      if self.getCurrentCode() in self._store.getSellCodes():
        self.productEdit.setText(str(self._store.getSellProductCode(self.getCurrentCode())))
        self.dateEdit.setText(self._store.getSellDate(self.getCurrentCode()))
        self.surnameEdit.setText(self._store.getSellSurname(self.getCurrentCode()))
        self.nameEdit.setText(self._store.getSellName(self.getCurrentCode()))
        self.secnameEdit.setText(self._store.getSellSecname(self.getCurrentCode()))
      
  def save(self):
    self._store.setSellProduct(self.getCurrentCode(),self.decode(self.productEdit.text()))
    self._store.setSellDate(self.getCurrentCode(),self.decode(self.dateEdit.text()))
    self._store.setSellSurname(self.getCurrentCode(),self.decode(self.surnameEdit.text()))
    self._store.setSellName(self.getCurrentCode(),self.decode(self.nameEdit.text()))
    self._store.setSellSecname(self.getCurrentCode(),self.decode(self.secnameEdit.text()))
    
  def new(self):
    code=self._store.getSellNewCode()
    self._store.newSell(code)
    self._store.setSellProduct(code,self.decode(self.productEdit.text()))
    self._store.setSellDate(code,self.decode(self.dateEdit.text()))
    self._store.setSellSurname(code,self.decode(self.surnameEdit.text()))
    self._store.setSellName(code,self.decode(self.nameEdit.text()))
    self._store.setSellSecname(code,self.decode(self.secnameEdit.text()))

  def delr(self):
    self._store.removeSell(self.getCurrentCode())
    if self._store.getSellCodes():self.setCurrentCode(self._store.getSellCodes()[0])
