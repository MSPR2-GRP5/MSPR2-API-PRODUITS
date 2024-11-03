from PRODUITS.models import Products
from typing import Any


def addProduct(
    add_name: str, add_desc: str, add_color: str, add_price: float, add_stock: int
) -> int:
    try:
        Products(
            name=add_name,
            description=add_desc,
            color=add_color,
            price=add_price,
            stock=add_stock,
        ).save()
        return 1
    except Exception:
        return 0


def updateProduct(
    id: int,
    update_name: str = "",
    update_desc: str = "",
    update_color: str = "",
    update_price: float = -1,
    update_stock: int = -1,
) -> int:
    try:
        product = Products.objects.filter(id=id)[0]
        if update_name:
            product.name = update_name
        if update_desc:
            product.description = update_desc
        if update_color:
            product.color = update_color
        if update_price >= 0:
            product.price = update_price
        if update_stock >= 0:
            product.stock = update_stock

        product.save()
        return 1
    except Exception:
        return 0


def searchProduct(  # On ne recherche pas par le prix et le stock?
    id: int = 0, search_name: str = "", search_desc: str = "", search_color: str = ""
) -> Any:
    try:
        products_out = Products.objects.all()
        if id != 0:
            products_out = products_out.filter(id=id)
        else:
            if search_name:
                products_out = products_out.filter(name=search_name)
            if search_desc:
                products_out = products_out.filter(description=search_desc)
            if search_color:
                products_out = products_out.filter(color=search_color)

        return products_out

    except Exception:
        return 0


def deleteProduct(id: int) -> int:
    try:
        Products.objects.filter(id=id).delete()
        return 1
    except Exception:
        return 0
