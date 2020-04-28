from dbcombobox import dbComboBox

class materialsCombo(dbComboBox):
  def update(self):
    self.clear()
    for p in self._store.getMaterialCodes():
      self.addItem(p,self.store.getMaterialName(p))
    self.setCurrentCode(self._store.getProductMaterialCode(self.getCurrentRec()))
