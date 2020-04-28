from general import general
from materials import materials

class products(general):
 def __init__(self,code=0,name='',type1='',material='',weight='',price=''):
  general.__init__(self,code,name)
  self.setType(type1)
  self.setMaterial(material)
  self.setWeight(weight)
  self.setPrice(price)

 def setType(self,value):self.__type=value
 def setMaterial(self,value):self.__material=value
 def setWeight(self,value):self.__weight=value
 def setPrice(self,value):self.__price=value
 def setMaterialCode(self):self.__materialcode=value
 def setMaterialName(self):self.__materialname=value
 def setMaterialPriceForGramm(self):self.__materialpriceforgramm=value

 def getType(self):return self.__type
 def getMaterial(self):return self.__material
 def getWeight(self):return self.__weight
 def getPrice(self):return self.__price
 def getMaterialCode(self):return self.__material.getCode()
 def getMaterialName(self):return self.__materialname
 def getMaterialPriceForGramm(self):return self.__materialpriceforgramm

 def info(self):
     s = "%s %s %s (%s) %s %s" % (self.getCode(), self.getName(), self.getType(), self.getMaterial().info(), self.getWeight(), self.getPrice())
     return s

#m1 = materials(0, 'Gold', 1000)
#m2 = materials(0, 'Silver', 500)
#m3 = materials(0, 'Bronze', 250)
#m4 = materials(0, 'Platinum', 1500)
#p1 = products(0, 'Goldсoin', 'Ring', m1, 10, 10000)
#print(p1.info())
#p2 = products(0, 'Argo', 'Necklace', m2, 30, 15000)
#print(p2.info())
#p3 = products(0, 'Maria', 'Earrings', m3, 5, 1250)
#print(p3.info())
#p4 = products(0, 'Darling', 'Necklace', m1, 40, 40000)
#print(p4.info())
#p5 = products(0, 'Unity', 'Ring', m4, 15, 22500)
#print(p5.info())
