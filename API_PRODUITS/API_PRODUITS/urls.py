from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema
import PRODUITS.DBFunctions as dbf
from ninja_apikey.security import APIKeyAuth
from typing import Any
# Schema d'un produit


class ProdsOut(Schema):
    id: int
    product_name: str
    description: str
    import_location: str
    price: float
    stocks: int


api = NinjaAPI(auth=APIKeyAuth())
# api = NinjaAPI()


@api.post("")
def create(
    request: Any, name: str, desc: str, location: str, price: float, stocks: int
) -> int:
    return dbf.addProduct(name, desc, location, price, stocks)


@api.get("", response=list[ProdsOut])
def search(request: Any, name: str = "", desc: str = "", location: str = "") -> Any:
    return dbf.searchProduct(Name=name, Desc=desc, Location=location)


# @api.get("/{id}", response = list[ProdsOut])
# def get(request: Any, name: str = "",desc: str = "",location: str= "", price: float = None, stocks: int = None) -> Any:
#     return(dbf.searchProduct(name,desc,location))


@api.get("{id}", response=list[ProdsOut])
def get(request: Any, id: int) -> Any:
    return dbf.searchProduct(id=id)


@api.patch("")
def update(
    request: Any, id: int, name: str = "", desc: str = "", location: str = ""
) -> int:
    return dbf.updateProduct(id, name, desc, location)


@api.delete("")
def delete(request: Any, id: int) -> int:
    return dbf.deleteProduct(id)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", api.urls),
]
