from dbcombobox import dbComboBox

class produtcsCombo(dbComboBox):
  def update(self):
    self.clear()
    for a in self._store.getProductCodes():
      if not(a in self._store.getSellProductCodes(self.getCurrentRec())):
        self.addItem(a,self._store.getProductName(a))
