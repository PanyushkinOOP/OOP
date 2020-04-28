from materialsListEdit import materialsListEdit
from productsListEdit import productsListEdit
from sellsListEdit import sellsListEdit

class store:
 def __init__(self):
  self.__materials=materialsListEdit()
  self.__products=productsListEdit()
  self.__sells=sellsListEdit()
 def removeMaterial(self,code):
  b = True
  for c in self.getProductCodes():
      if self.getProductMaterialCode(c) == code:
          b = False
          break
  if b:
      self.__materials.removeList(code)
  
 def removeProduct(self,code):
  d = True
  for e in self.getSellCodes():
      if self.getSellProductCode(e) == code:
          d = False
          break
  if d:
      self.__products.removeList(code)
 def clear(self):
  self.__materials.clear()
  self.__products.clear()
  self.__sells.clear()
 def newMaterial(self,code=0, name='',priceForGramm=0):self.__materials.newRec(code,name,priceForGramm)
 def findMaterialByCode(self,code):return self.__materials.findByCode(code)
 def getMaterialNewCode(self):return self.__materials.getNewCode()
 def getMaterialCodes(self):return self.__materials.getCodes()
 def getMaterialName(self,code):return self.__materials.getName(code)
 def getMaterialPriceForGramm(self,code):return self.__materials.getPriceForGramm(code)
 def getMaterialNewCode(self):return self.__materials.getNewCode()

 def setMaterialName(self,code,value):self.__materials.SetName(code,value)
 def setMaterialPriceForGramm(self,code,value):self.__materials.SetPriceforGramm(code,value)
 
 
 def newProduct(self,code=0,name='',type1='',material=None,weight=0,price=0):self.__products.newRec(code,name,type1,material,weight,price)
 def findProductByCode(self,code):return self.__products.findByCode(code)

 def setProductName(self,code,value):return self.__products.setName(code,value)
 def setProductType(self,code,value):return self.__products.setType(code,value)
 def setProductWeight(self,code,value):return self.__products.setWeight(code,value)
 def setProductPrice(self,code,value):return self.__products.setPrice(code,value)

 def newProduct(self,code=0,name='',type1='',material='',weight='',price=''):self.__products.newRec(code,name,type1,material,weight,price)
 def findProductByCode(self,code):return self.__products.findByCode(code)
 def getProductNewCode(self):return self.__products.getNewCode()
 def getProductCodes(self):return self.__products.getCodes()
 def getProductNewCode(self):return self.__products.getNewCode()
 def getProductName(self,code):return self.__products.getName(code)
 def getProductType(self,code):return self.__products.getType(code)
 def getProductWeight(self,code):return self.__products.getWeight(code)
 def getProductPrice(self,code):return self.__products.getPrice(code)
 
 def getProductMaterialName(self,code):return self.__products.getMaterialName(code)
 def getProductMaterialPriceForGramm(self,code):return self.__products.getMaterialPriceForGramm(code)
 def getProductMaterialCode(self,code):return self.__products.getMaterialCode(code)
 def getProductNewCode(self):return self.__products.getNewCode()
 

 def removeSell(self,code):self.__sells.removeList(code)
 def newSell(self,code=0,product=None,date='',surname='',name='',secname=''):self.__sells.newRec(code,product,date,surname,name,secname)
 def findSellByCode(self,code):return self.__sells.findByCode(code)
 
 def setSellDate(self,code,value):self.__sells.setDate(code,value)
 def setSellSurname(self,code,value):self.__sells.setSurname(code,value)
 def setSellName(self,code,value):self.__sells.setName(code,value)
 def setSellSecname(self,code,value):self.__sells.setSecname(code,value)

 def newSell(self,code=0,product='',date='',surname='',name='',secname=''):self.__sells.newRec(code,product,date,surname,name,secname)
 def findSellByCode(self,code):return self.__sells.findByCode(code)
 def getSellNewCode(self):return self.__sells.getNewCode()
 def getSellCodes(self):return self.__sells.getCodes()
 def getSellNewCode(self):return self.__sells.getNewCode()
 def getSellDate(self,code):return self.__sells.getDate(code)
 def getSellSurname(self,code):return self.__sells.getSurname(code)
 def getSellName(self,code):return self.__sells.getName(code)
 def getSellSecname(self,code):return self.__sells.getSecname(code)

 def getSellProductCode(self,code):return self.__sells.getProductCode(code)
 def getSellProductName(self,code):return self.__sells.getProductName(code)
 def getSellProductType(self,code):return self.__sells.getProductType(code)
 def getSellProductMaterial(self,code):return self.__sells.getProductMaterial(code)
 def getSellProductWeight(self,code):return self.__sells.getProductWeight(code)
 def getSellProductPrice(self,code):return self.__sells.getProductPrice(code)
 def getSellProductCodes(self,code):return self.__sells.getNewCode()
 def getSellNewCode(self):return self.__sells.getNewCode()
 
                                                             





