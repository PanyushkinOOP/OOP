from PyQt5 import QtWidgets, QtCore
from editform import editForm

class productsEditForm(editForm):
  def __init__(self,store,parrent=None):
    editForm.__init__(self,store,parrent=None)
    
    self.nameEdit=QtWidgets.QLineEdit()
    self.typeEdit=QtWidgets.QLineEdit()
    self.materialEdit=QtWidgets.QLineEdit()
    self.weightEdit=QtWidgets.QLineEdit()
    self.priceEdit=QtWidgets.QLineEdit()

    self._grid.addWidget(QtWidgets.QLabel('Название'),0,0)
    self._grid.addWidget(self.nameEdit,0,1)
    self._grid.addWidget(QtWidgets.QLabel('Тип'),1,0)
    self._grid.addWidget(self.typeEdit,1,1)
    self._grid.addWidget(QtWidgets.QLabel('Материал'),2,0)
    self._grid.addWidget(self.materialEdit,2,1)
    self._grid.addWidget(QtWidgets.QLabel('Вес'),3,0)
    self._grid.addWidget(self.weightEdit,3,1)
    self._grid.addWidget(QtWidgets.QLabel('Цена'),4,0)
    self._grid.addWidget(self.priceEdit,4,1)
    
  def update(self):
    if self.getCurrentCode() in self._store.getProductCodes():
      self.nameEdit.setText(self._store.getProductName(self.getCurrentCode()))
      self.typeEdit.setText(self._store.getProductType(self.getCurrentCode()))
      self.materialEdit.setText(str(self._store.getProductMaterialCode(self.getCurrentCode())))
      self.weightEdit.setText(str(self._store.getProductWeight(self.getCurrentCode())))
      self.priceEdit.setText(str(self._store.getProductPrice(self.getCurrentCode())))
      
  def save(self):
    self._store.setProductName(self.getCurrentCode(),self.decode(self.nameEdit.text()))
    self._store.setProductType(self.getCurrentCode(),self.decode(self.typeEdit.text()))
    self._store.setProductMaterial(self.getCurrentCode(),self.decode(self.materialEdit.text()))
    self._store.setProductWeight(self.getCurrentCode(),self.decode(self.weightEdit.text()))
    self._store.setProductPrice(self.getCurrentCode(),self.decode(self.priceEdit.text()))
    
  def new(self):
    code=self._store.getProductNewCode()
    self._store.newProduct(code)
    self._store.setProductName(code,self.decode(self.nameEdit.text()))
    self._store.setProductType(code,self.decode(self.typeEdit.text()))
    self._store.setProductMaterial(code,self.decode(self.materialEdit.text()))
    self._store.setProductWeight(code,self.decode(self.weightEdit.text()))
    self._store.setProductPrice(code,self.decode(self.priceEdit.text()))

  def delr(self):
    self._store.removeProducts(self.getCurrentCode())
    if self._store.getProductsCodes():self.setCurrentCode(self._store.getProductCodes()[0])
