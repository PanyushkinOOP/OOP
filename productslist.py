from generallist import generalList

class productsList(generalList):
 def getType(self,code):return self.findByCode(code).getType()
 def getMaterial(self,code):return self.findByCode(code).getMaterial()
 def getWeight(self,code):return self.findByCode(code).getWeight()
 def getPrice(self,code):return self.findByCode(code).getPrice()
 def infoProducts(self, code):
  return return self.findByCode(code).info()
 def info(self):
  s=''
  for code in self.getCodes():
   s+=self.infoProducts(code) + '\n'
  if s:
    s = s[:-1]
  return s
