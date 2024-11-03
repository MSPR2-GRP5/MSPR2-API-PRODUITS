from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, ModelSchema  # ,Schema
import PRODUITS.DBFunctions as dbf
from typing import Any
from ninja_apikey.security import APIKeyAuth
# from datetime import datetime
from PRODUITS.models import Products
# Schema d'un produit


class ProdsOut(ModelSchema):
    # id: int
    # created_at: datetime
    # name: str
    # description: str
    # color: str
    # price: float
    # stock: int
    class Meta:
        model = Products
        fields = "__all__"


api = NinjaAPI(auth=APIKeyAuth())
# api = NinjaAPI()


@api.post("")
def create(
    request: Any,
    add_name: str,
    add_desc: str,
    add_color: str,
    add_price: float,
    add_stock: int,
) -> int:
    return dbf.addProduct(add_name, add_desc, add_color, add_price, add_stock)


@api.get("", response=list[ProdsOut])
def search(
    request: Any, search_name: str = "", search_desc: str = "", search_color: str = ""
) -> Any:
    return dbf.searchProduct(
        search_name=search_name, search_desc=search_desc, search_color=search_color
    )


# @api.get("/{id}", response = list[ProdsOut])
# def get(request: Any, name: str = "",desc: str = "",location: str= "", price: float = None, stocks: int = None) -> Any:
#     return(dbf.searchProduct(name,desc,location))


@api.get("{id}", response=list[ProdsOut])
def get(request: Any, id: int) -> Any:
    return dbf.searchProduct(id=id)


@api.patch("")
def update(
    request: Any,
    id: int,
    update_name: str = "",
    update_desc: str = "",
    update_color: str = "",
    update_price: float = -1,
    update_stock: int = -1,
) -> int:
    return dbf.updateProduct(
        id, update_name, update_desc, update_color, update_price, update_stock
    )


@api.delete("")
def delete(request: Any, id: int) -> int:
    return dbf.deleteProduct(id)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", api.urls),
]
