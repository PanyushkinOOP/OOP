from materials import materials
from generalListEdit import generalListEdit

class materialsListEdit(generalListEdit):
 def newRec(self,code=0,name='',priceForGramm=''):self.appendList(materials(code,name,priceForGramm))
 def setPriceForGramm(self,code,value):self.findByCode(code).setPriceForGramm(value)
 def getPriceForGramm(self,code):return self.findByCode(code).getPriceForGramm()
