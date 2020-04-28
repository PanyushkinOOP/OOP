from sells import sells
from generalListEdit import generalListEdit

class sellsListEdit(generalListEdit):
 def newRec(self,code=0,product=None,date='',surname='',name='',secname=''):self.appendList(sells(code,product,date,surname,name,secname))
 def setProduct(self,code,value):self.findByCode(code).setProduct(value)
 def setDate(self,code,value):self.findByCode(code).setDate(value)
 def setSurname(self,code,value):self.findByCode(code).setSurname(value)
 def setSecname(self,code,value):self.findByCode(code).setSecname(value)
 def getDate(self,code):return self.findByCode(code).getDate()
 def getSurname(self,code):return self.findByCode(code).getSurname()
 def getSecname(self,code):return self.findByCode(code).getSecname()
 def getProductCode(self,code):return self.findByCode(code).getProductCode()
 def getProductName(self,code):return self.findByCode(code).getProductName()
 def getProductType(self,code):return self.findByCode(code).getProductType()
# def getProductMaterial(self,code):return self.findByCode(code).getProductMaterial
 def getProductWeight(self,code):return self.findByCode(code).getProductWeight()
 def getProductPrice(self,code):return self.findByCode(code).getProductPrice()
 
