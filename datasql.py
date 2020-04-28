import os
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;

create table materials
(code integer primary key,
 name text,
 priceForGramm integer);

create table product
(code integer primary key,
 name text,
 type1 text,
 weight integer,
 price integer,
 material integer);

create table sell
(code integer primary key,
 date text,
 surname text,
 name text,
 secname text,
 product integer references product(code) on update cascade on delete set null);
"""

class datasql:
 def read(self,inp,lib):
  conn = db.connect(inp)
  curs = conn.cursor()
  curs.execute("select code,name,priceForGramm from materials")
  data=curs.fetchall()
  for r in data:lib.newMaterial(r[0],r[1],r[2])
  curs.execute("select code,name,type1,material,weight,price from product")
  data=curs.fetchall()
  for r in data:
      lib.newProduct(r[0],r[1],r[2],lib.findMaterialByCode(int(r[3])),r[4],r[5])
  curs.execute("select code,product,date,surname,name,secname from sell")
  data=curs.fetchall()
  for r in data:lib.newSell(r[0],lib.findProductByCode(int(r[1])),r[2],r[3],r[4],r[5])
  
 def write(self,out,lib):
  conn = db.connect(out)
  curs = conn.cursor()
  curs.executescript(emptydb)
  for c in lib.getMaterialCodes():
   curs.execute("insert into materials(code,name,priceForGramm) values('%s','%s','%s')"%(
     str(c),
     lib.getMaterialName(c),
     int(lib.getMaterialPriceForGramm(c))))
  for c in lib.getProductCodes():
    curs.execute("insert into product(code,name,type1,material,weight,price) values('%s','%s','%s','%s','%s','%s')"%(
      str(c),
      lib.getProductName(c),
      lib.getProductType(c),
      int(lib.getProductMaterialCode(c)),
      int(lib.getProductPrice(c)),
      int(lib.getProductWeight(c))))
  for c in lib.getSellCodes():
    curs.execute("insert into sell(code,product,date,surname,name,secname) values('%s','%s','%s','%s','%s','%s')"%(
      str(c),
      int(lib.getSellProductCode(c)),
      lib.getSellDate(c),
      lib.getSellSurname(c),
      lib.getSellName(c),
      lib.getSellSecname(c)))
    
  conn.commit()
  conn.close()
