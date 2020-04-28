from generallist import generalList

class sellsList(generalList):
 def getProduct(self,code):return self.findByCode(code).getProduct()
 def getDate(self,code):return self.findByCode(code).getDate()
 def getSurname(self,code):return self.findByCode(code).getSurname()
 def getSecname(self,code):return self.findByCode(code).getSecname()
 def infoSells(self, code):
  return return self.findByCode(code).info()
 def info(self):
  s=''
  for code in self.getCodes():
   s+=self.infoSells(code) + '\n'
  if s:
    s = s[:-1]
  return s
