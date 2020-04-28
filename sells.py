from general import general 
from materials import materials
from products import products

class sells(general):
 def __init__(self,code=0,product='',date='',surname='',name='',secname=''):
  general.__init__(self,code,name)
  self.setProduct(product)
  self.setDate(date)
  self.setSurname(surname)
  self.setSecname(secname)

 def setProduct(self,value):self.__product=value
 def setDate(self,value):self.__date=value
 def setSurname(self,value):self.__surname=value
 def setSecname(self,value):self.__secname=value
 #def setProductCode(self,value):self.__productcode=value
 #def setProductName(self,value):self.__productname=value
 #def setProductType(self,value):self.__productype=value
 #def setProductWeight(self,value):self.__productweight=value
 #def setProductPrice(self,value):self.__productprice=value

 def getProduct(self):return self.__product
 def getDate(self):return self.__date
 def getSurname(self):return self.__surname
 def getSecname(self):return self.__secname
 def getProductCode(self):return self.__product.getCode()
 def getProductName(self):return self.__product.getName()
 def getProductType(self):return self.__productype
 def getProductWeight(self):return self.__productweight
 def getProductPrice(self):return self.__productprice

 def info(self):
     s = "%s (%s) %s %s %s %s" % (self.getCode(), self.getProduct().info(), self.getDate(), self.getSurname(), self.getName(), self.getSecname())
     return s

#m1 = materials(0, 'Gold', 1000)
#m2 = materials(0, 'Silver', 500)
#m3 = materials(0, 'Bronze', 250)
#m4 = materials(0, 'Platinum', 1500)
#p1 = products(0, 'Goldсoin', 'Ring', m1, 10, 10000)
#p2 = products(0, 'Argo', 'Necklace', m2, 30, 15000)
#p3 = products(0, 'Maria', 'Earrings', m3, 5, 1250)
#p4 = products(0, 'Darling', 'Necklace', m1, 40, 40000)
#p5 = products(0, 'Unity', 'Ring', m4, 15, 22500)
#g1 = sells(0, p3, '21.02.2018' , 'Pavlov', 'Ivan', 'Stepanovich')
#print(g1.info())
#g2 = sells(0, p1, '15.03.2018', 'Muhin', 'Sergey' , 'Sergeevich')
#print(g2.info())
#g3 = sells(0, p2, '06.06.2018', 'Petrushkin', 'Genadiy', 'Olegovhich')
#print(g3.info())
#g4 = sells(0, p5, '19.10.2018', 'Semenov', 'Anatolyi', 'Viktorovich')
#print(g4.info())
#g5 = sells(0, p4, '15.01.2019', 'Rukov', 'Semen', 'Petrovich')
#print(g5.info())
