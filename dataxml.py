import os,xml.dom.minidom
class dataxml:
  def read(self,inp,lib):
    dom=xml.dom.minidom.parse(inp)
    dom.normalize()
    for node in dom.childNodes[0].childNodes:
      if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='material'):
        code,name,PriceForGramm=0,"",0
        for t in node.attributes.items():
          if t[0]=="code":code=int(t[1])
          if t[0]=="name":name=t[1]
          if t[0]=="PriceForGramm":PriceForGramm=t[1]
        lib.newMaterial(code,name,PriceForGramm)
      if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='product'):
        code,name,type1,material,weight,price=0,"","",None,0,0
        for t in node.attributes.items():
          if t[0]=="code":code=int(t[1])
          if t[0]=="name":name=t[1]
          if t[0]=="type":type1=t[1]
          if t[0]=="material":
              #print(t[1])
              material=lib.findMaterialByCode(int(t[1]))
          if t[0]=="weight":weight=t[1]
          if t[0]=="price":price=t[1]
        lib.newProduct(code,name,type1,material,weight,price)
      if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='sell'):
        code,product,date,surname,name,secname=0,None,"","","",""
        for t in node.attributes.items():
          if t[0]=="code":code=int(t[1])
          if t[0]=="product":
              #print(t[1])
              product=lib.findProductByCode(int(t[1]))
              #print(product.info())
          if t[0]=="date":date=t[1]
          if t[0]=="surname":surname=t[1]
          if t[0]=="name":name=t[1]
          if t[0]=="secname":secname=t[1]
        lib.newSell(code,product,date,surname,name,secname)

  def write(self,out,lib):
   dom=xml.dom.minidom.Document()
   root=dom.createElement("store")
   dom.appendChild(root)
   for c in lib.getMaterialCodes():
     bk=dom.createElement("material")
     bk.setAttribute('code',str(c))
     bk.setAttribute('name',lib.getMaterialName(c))
     bk.setAttribute('PriceForGramm',str(lib.getMaterialPriceForGramm(c)))
     root.appendChild(bk)
   for c in lib.getProductCodes():
     pub=dom.createElement("product")
     pub.setAttribute('code',str(c))
     pub.setAttribute('name',lib.getProductName(c))
     pub.setAttribute('type',lib.getProductType(c))
     pub.setAttribute('material',str(lib.getProductMaterialCode(c)))
     pub.setAttribute('weight',str(lib.getProductWeight(c)))
     pub.setAttribute('price',str(lib.getProductPrice(c)))
     root.appendChild(pub)
   for c in lib.getSellCodes():
     aut=dom.createElement("sell")
     aut.setAttribute('code',str(c))
     aut.setAttribute('product',str(lib.getSellProductCode(c)))
     aut.setAttribute('date',lib.getSellDate(c))
     aut.setAttribute('surname',lib.getSellSurname(c))
     aut.setAttribute('name',lib.getSellName(c))
     aut.setAttribute('secname',lib.getSellSecname(c))
     root.appendChild(aut)
   f = open(out,"w")
   f.write(dom.toprettyxml())#encoding='utf-8'))
