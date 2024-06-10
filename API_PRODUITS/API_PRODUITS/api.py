from ninja import NinjaAPI, Schema, Form

api = NinjaAPI()


#Schema d'un produit
class productSchema(Schema):
    name: str = "Nom"
    desc: str = "Description"
    location: str = "Lieu d'importation"
    price: int = "Price"
    stock: int = "Stocks"


class HelloSchema(Schema):
    name: str = "world"

@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"


from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

class HelloSchema(Schema):
    name: str = "world"

@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"


@api.get("/path")
def get_operation(request):
    ...

@api.post("/path")
def post_operation(request):
    ...

@api.put("/path")
def put_operation(request):
    ...

@api.delete("/path")
def delete_operation(request):
    ...

@api.patch("/path")
def patch_operation(request):
    ...



#Chaque service devra fournir, via une API REST, des opérations de création/modification/suppression et
#recherche des objets liés (cf détails des endpoints à développer).

#Création du produit
@api.post("/create")
def createProduct(request,id,name,desc,location,price,stocks):
    ...

#Suppression du produit
@api.post("/delete")
def deleteProduct(request,id):
    ...

#Modification d'un produit
@api.post("/modify")
def modifyProduct(request,id,name,desc,location,price,stocks):
    ...

#Liste des produits
@api.post("/get")
def getProduct(request,id,name,desc,location,price,stocks):
    ...

#Recherche des produits par param, voir comment mettre dans le get.
@api.post("/search")
def searchBy(request,data: Form[productSchema]):
    return data
        

