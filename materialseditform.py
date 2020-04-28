from PyQt5 import QtWidgets, QtCore
from editform import editForm

class materialsEditForm(editForm):
  def __init__(self,store,parrent=None):
    editForm.__init__(self,store,parrent=None)

    self.nameEdit=QtWidgets.QLineEdit()
    self.priceForGrammEdit=QtWidgets.QLineEdit()

    self._grid.addWidget(QtWidgets.QLabel('название'),0,0)
    self._grid.addWidget(self.nameEdit,0,1)
    self._grid.addWidget(QtWidgets.QLabel('ЦенаЗаГрамм'),1,0)
    self._grid.addWidget(self.priceForGrammEdit,1,1)

  def update(self):
    if self.getCurrentCode() in self._store.getMaterialCodes():
      self.nameEdit.setText(self._store.getMaterialName(self.getCurrentCode()))
      self.priceForGrammEdit.setText(str(self._store.getMaterialPriceForGramm(self.getCurrentCode())))

  def save(self):
    self._store.setPublName(self.getCurrentCode(),self.decode(self.nameEdit.text()))
    self._store.setPublShortname(self.getCurrentCode(),self.decode(self.priceForGrammEdit.text()))

  def new(self):
    code=self._store.getMaterialNewCode()
    self._store.newMaterial(code)
    self._store.setMaterialName(code,self.decode(self.nameEdit.text()))
    self._store.setMaterialPriceForGramm(code,self.decode(self.priceForGrammEdit.text()))

  def delr(self):
    self._store.removeMaterial(self.getCurrentCode())
    if self._store.getMaterialCodes():self.setCurrentCode(self._store.getMaterialCodes()[0])
