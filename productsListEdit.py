from products import products
from generalListEdit import generalListEdit

class productsListEdit(generalListEdit):
 def newRec(self,code=0,name='',type1='',material=None,weight=0,price=0):self.appendList(products(code,name,type1,material,weight,price))
 def setType(self,code,value):self.findByCode(code).setType(value)
 def setMaterial(self,code,value):self.findByCode(code).setMaterial(value)
 def setWeight(self,code,value):self.findByCode(code).setWeight(value)
 def setPrice(self,code,value):self.findByCode(code).setPrice(value)
 def getType(self,code):return self.findByCode(code).getType()
 def getWeight(self,code):return self.findByCode(code).getWeight()
 def getPrice(self,code):return self.findByCode(code).getPrice()
 def getMaterialCode(self,code):return self.findByCode(code).getMaterialCode()
 def getMaterialName(self,code):return self.findByCode(code).getMaterialName()
 def getMaterialPriceForGramm(self,code):return self.findByCode(code).getMaterialPriceForGramm()
