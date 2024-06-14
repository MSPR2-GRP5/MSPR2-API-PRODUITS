from PRODUITS import DBFunctions as dbf
from django.contrib import admin
from django.urls import path
# from .api import api
from ninja import NinjaAPI, Schema
from ninja_apikey.security import APIKeyAuth

#Schema d'un produit

api = NinjaAPI()
class ProdsOut(Schema):
    id : int
    product_name: str
    description: str
    import_location: str




# api = NinjaAPI(auth=APIKeyAuth())


@api.post("/create")
def createProduct(request,name,desc,location,price,stocks):
    return(dbf.addProduct(name,desc,location,price,stocks))

@api.post("/search", response = list[ProdsOut])
def search(request, name = "",desc = "",location= "") :
    return(dbf.searchProduct(name,desc,location))

# #Suppression du produit
# @api.post("/delete")
# def deleteProduct(request,id):
#     ...

# #Modification d'un produit
# @api.post("/modify")
# def modifyProduct(request,id,name,desc,location,price,stocks):
#     ...

# #Liste des produits
# @api.post("/get")
# def getProduct(request,id,name,desc,location,price,stocks):
#     ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]