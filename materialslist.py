from generallist import generalList

class materialsList(generalList):
 def getPriceForGramm(self,code):return self.findByCode(code).getPriceForGramm()
 def infoMaterials(self, code):
  return return self.findByCode(code).info()
 def info(self):
  s=''
  for code in self.getCodes():
   s+=self.infoMaterials(code) + '\n'
  if s:
    s = s[:-1]
  return s
