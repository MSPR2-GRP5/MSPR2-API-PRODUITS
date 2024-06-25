from PRODUITS.models import Products
from typing import Any


def addProduct(name: str, desc: str, location: str,price: float, stock: int) -> int:
    try:
        Products(product_name = name,description = desc, import_location = location, price = price, stocks = stock).save()
        return 1
    except:
        return 0        
    
def updateProduct(id : int, name :str ="",desc : str ="", location : str ="", price: float = -1, stocks: int = -1) -> int:
    try :
        product = Products.objects.filter(id = id)[0]
        if(name) :
            product.product_name = name
        if(desc):
            product.desc = desc
        if(location):
            product.import_location = location
        if(price >= 0):
            product.price = price
        if (stocks >=0):
            product.stocks = stocks
        product.save()
        return 1
    except Exception:
        return 0

def searchProduct(id : int = "", Name: str = "", Desc: str = "", Location: str = "") -> Any:
    try:
        products_out = Products.objects.all()
        if id != 0 :
            products_out = products_out.filter(id = id)
        else:
            if(Name) :
                products_out = products_out.filter(product_name = Name)
            if(Desc):
                products_out = products_out.filter(description = Desc)
            if(Location):
                products_out = products_out.filter(import_location = Location)

        return products_out
        
    except:
        return 0
    
def deleteProduct(id: int) -> int:
    try:
        Products.objects.filter(id = id).delete()
        return 1
    except Exception:
        return 0
