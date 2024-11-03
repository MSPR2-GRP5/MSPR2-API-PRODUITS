from django.test import TestCase
from PRODUITS.models import Products
import PRODUITS.DBFunctions as dbf


# Create your tests here.
class DBTestCase(TestCase):
    def setUp(self) -> None:  # Création de quelques entrées pour le search plus tard.
        self.product1 = Products.objects.create(
            name="Product test",
            description="Desc test 1",
            color="Brown",
            price=10,
            stock=1,
        )
        self.product1 = Products.objects.create(
            name="Product test",
            description="Desc test 2",
            color="Brown",
            price=20,
            stock=2,
        )

    def testCreateProduct_GoodInput(
        self,
    ) -> None:  # Créer un produit avec des inputs corrects.
        dbf.addProduct("Product test 3", "Desc test 3", "Black", 3, 30)
        self.assertEqual(Products.objects.all().count(), 3, "Should return 3.")

    def testDeleteProduct(
        self,
    ) -> None:
        dbf.deleteProduct(3)
        self.assertEqual(
            Products.objects.all().count(), 2, "Should return 2."
        )  # Supprime un produit. ASSUME QUE l'ID DU PRODUIT CREER PRECEDEMMENT EST 3.

    def testCreateProduct_WrongNameInput(self) -> None:
        (
            dbf.addProduct(None, "Out of this world.", "White", 3, 30),  # type: ignore  #Création érronée sur le nom.
            0,
            "Should return 0.",
        )

    def testCreateProduct_WrongDescInput(self) -> None:
        dbf.addProduct("Fancy grainTM", None, "Pink", 3, 30), 0, "Should return 0."  # type: ignore  #Création érronée sur la description.

    def testCreateProduct_WrongColorInput(self) -> None:
        (
            dbf.addProduct("Fancier grainTM", "Out of this world.", None, 3, 30),  # type: ignore  #Création érronée sur color.
            0,
            "Should return 0.",
        )

    def testCreateProduct_WrongStockInput(self) -> None:
        (
            dbf.addProduct(
                "Fanciest grainTM", "Out of this world.", "Rainbow", None, 30   # type: ignore  #Création érronée sur le stock.
            ),  
            0,
            "Should return 0.",
        )

    def testCreateProduct_WrongPriceInput(self) -> None:
        (
            dbf.addProduct(
                "Definitly not fancy grainTM",
                "Out of this world.",
                "RGB",
                5,
                None,  # type: ignore #Création érronée sur le prix.
            ),
            0,
            "Should return 0.",
        )

    def testSearchProduct(self) -> None:  # Recherche des produits selon des critères .
        self.assertEqual(  # Selon le nom.
            dbf.searchProduct(search_name="Product test").count(),
            2,
            "The number of products with the name 'Product test', should be 2.",
        )
        self.assertEqual(  # Selon la description.
            dbf.searchProduct(search_desc="Desc test 1").count(),
            1,
            "The number of products with the desc 'Desc test 1', should be 1.",
        )
        self.assertEqual(  # Selon color.
            dbf.searchProduct(search_color="Brown").count(),
            2,
            "The number of products with the color 'Brown', should be 2.",
        )
        # ==================================================== On ne peut pas chercher selon le stock et le prix.
        # self.assertEqual(   #Selon le stock.
        #     dbf.searchProduct(stocks = 1).count(),
        #     1,
        #     "The number of products with the stock '1', should be 1."
        # )
        # self.assertEqual(   #Selon le prix.
        #     dbf.searchProduct(price = 10).count(),
        #     1,
        #     "The number of products with the price '10', should be 1."
        # )
        # ====================================================

    def testSearchProduct_WrongInput(self) -> None:  # Recherche un produit inexistant
        self.assertEqual(
            dbf.searchProduct(search_name="Inexistant name").count(),
            0,
            "Should return 0",
        )

    def testUpdateProducts(
        self,
    ) -> None:  # Update le nom du produit ID 1 et recherche le.
        dbf.updateProduct(id=1, update_name="The coffee god's finest")
        self.assertEqual(
            dbf.searchProduct(search_name="The coffee god's finest").count(),
            1,
            "Should return 1",
        )
