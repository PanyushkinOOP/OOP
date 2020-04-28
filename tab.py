from PyQt5 import QtWidgets, QtCore
from materialseditform import materialsEditForm
from productseditform import productsEditForm
from sellseditform import sellsEditForm

class tabWidget(QTabWidget):
    def __init__(self, store, parent=None):
        QTabWidget.__init__(self,parent)
        self.__materialsEditForm=materialsEditForm(store=store)
        self.addTab(self.__materialEditForm,u'Материалы')
        self.__productsEditForm=productsEditForm(store=store)
        self.addTab(self.__productsEditForm,u'Изделия')
        self.__sellsEditForm=customersEditForm(store=store)
        self.addTab(self.__sellsEditForm,u'Покупатели')

    def update(self):
        self.__sellsEditForm.tableUpdate()
        self.__productsEditForm.tableUpdate()
