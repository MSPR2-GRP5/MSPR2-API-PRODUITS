from typing import Any

from ninja import NinjaAPI, Schema, Form

api = NinjaAPI()


#Schema d'un produit
class productSchema(Schema):
    name: str = "Nom"
    desc: str = "Description"
    location: str = "Lieu d'importation"
    price: int = 0
    stock: int = 0


class HelloSchema(Schema):
    name: str = "world"

@api.post("/hello")
def hello(request: Any, data: HelloSchema) -> str:
    return f"Hello {data.name}"


@api.get("/math/{a}and{b}")
def math(request: Any, a: int, b: int) -> dict[str, int]:
    return {"add": a + b, "multiply": a * b}


# @api.get("/path")
# def get_operation(request):
#     ...
#
# @api.post("/path")
# def post_operation(request):
#     ...
#
# @api.put("/path")
# def put_operation(request):
#     ...
#
# @api.delete("/path")
# def delete_operation(request):
#     ...
#
# @api.patch("/path")
# def patch_operation(request):
#     ...



#Chaque service devra fournir, via une API REST, des opérations de création/modification/suppression et
#recherche des objets liés (cf détails des endpoints à développer).

#Création du produit
# @api.post("/create")
# def createProduct(request,id,name,desc,location,price,stocks):
#     ...
#
# #Suppression du produit
# @api.post("/delete")
# def deleteProduct(request,id):
#     ...
#
# #Modification d'un produit
# @api.post("/modify")
# def modifyProduct(request,id,name,desc,location,price,stocks):
#     ...
#
# #Liste des produits
# @api.post("/get")
# def getProduct(request,id,name,desc,location,price,stocks):
#     ...

#Recherche des produits par param, voir comment mettre dans le get.
@api.post("/search")
def searchBy(request: Any, data: Form[productSchema]) -> Form[productSchema]:
    return data
