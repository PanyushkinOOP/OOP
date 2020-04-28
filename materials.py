from general import general

class materials(general):
 def __init__(self,code=0,name='',priceForGramm=''):
  general.__init__(self,code,name)
  self.setPriceForGramm(priceForGramm)
 def setPriceForGramm(self,value):self.__priceForGramm=value
 def getPriceForGramm(self):return self.__priceForGramm
 def info(self):
     s = "%s %s %s" % (self.getCode(), self.getName(), self.getPriceForGramm())
     return s

#m1 = materials(0, 'Gold', 1000)
#print(m1.info())
#m2 = materials(0, 'Silver', 500)
#print(m2.info())
#m3 = materials(0, 'Bronze', 250)
#print(m3.info())
#m4 = materials(0, 'Platinum', 1500)
#print(m4.info())
