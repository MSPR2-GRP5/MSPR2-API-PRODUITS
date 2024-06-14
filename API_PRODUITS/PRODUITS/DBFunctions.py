from PRODUITS.models import *

def addProduct(name,desc,location,price,stock):
    try:
        Products(product_name = name,description = desc, import_location = location, price = price, stocks = stock).save()
        return 1
    except:
        return 0        

def searchProduct(Name = None,Desc = None,Location =None) :
    try:
        products_out = Products.objects.all()
        if(Name) :
            products_out = products_out.filter(Name = Name)
        if(Desc):
            products_out = products_out.filter(Desc = Desc)
        if(Location):
            products_out = products_out.filter(Location = Location)
        return products_out
        
    except:
        return 0
