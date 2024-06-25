from django.test import TestCase
from PRODUITS.models import Products
import PRODUITS.DBFunctions as dbf

# Create your tests here.
class DBTestCase(TestCase) :
    def setUp(self) -> None :   #Création de quelques entrées pour le search plus tard.
        self.product1 = Products.objects.create(
            product_name = "Product test", description = "Desc test 1", import_location = "Vietnam", price = 10 , stocks = 1
        )
        self.product1 = Products.objects.create(
            product_name = "Product test", description = "Desc test 2", import_location = "Vietnam", price = 20 , stocks = 2
        )

    def testCreateProduct_GoodInput(self) -> None : #Créer un produit avec des inputs corrects.
        dbf.addProduct("Product test 3","Desc test 3","Third world country",3,30)
        self.assertEqual(Products.objects.all().count(),3,"Should return 3.")

    def testDeleteProduct(self) -> None :   #Supprime un produit. ASSUME QUE l'ID DU PRODUIT CREER PRECEDEMMENT EST 3.
        dbf.deleteProduct(3)
        self.assertEqual(Products.objects.all().count(), 2, "Should return 2.")
    
    def testCreateProduct_WrongNameInput(self) -> None :    
        dbf.addProduct(None,"Out of this world.","Britain",3,30), 0, "Should return 0." # type: ignore  #Création érronée sur le nom.

    def testCreateProduct_WrongDescInput(self) -> None :
        dbf.addProduct("Fancy grainTM",None,"France",3,30), 0, "Should return 0." # type: ignore  #Création érronée sur la description.

    def testCreateProduct_WrongLocationInput(self) -> None :
        dbf.addProduct("Fancier grainTM","Out of this world.",None,3,30), 0, "Should return 0." # type: ignore  #Création érronée sur la location.

    def testCreateProduct_WrongStockInput(self) -> None :
        dbf.addProduct("Fanciest grainTM","Out of this world.","The local shady garden",None,30), 0, "Should return 0." # type: ignore  #Création érronée sur le stock.

    def testCreateProduct_WrongPriceInput(self) -> None :
        dbf.addProduct("Definitly not fancy grainTM","Out of this world.","Carrefour",5,None), 0, "Should return 0." # type: ignore #Création érronée sur le prix.

    def testSearchProduct(self) -> None :   #Recherche des produits selon des critères .
        self.assertEqual(   #Selon le nom.
            dbf.searchProduct(Name = "Product test").count(),
            2,
            "The number of products with the name 'Product test', should be 2."
        )
        self.assertEqual(   #Selon la description.
            dbf.searchProduct(Desc = "Desc test 1").count(),
            1,
            "The number of products with the desc 'Desc test 1', should be 1."
        )
        self.assertEqual(   #Selon la location.
            dbf.searchProduct(Location = "Vietnam").count(),
            2,
            "The number of products with the import_location 'Vietnam', should be 2."
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

    def testSearchProduct_WrongInput(self) -> None :   #Recherche un produit inexistant
        self.assertEqual(dbf.searchProduct(Name="Inexistant name").count(), 0, "Should return 0")

    def testUpdateProducts(self) -> None : #Update le nom du produit ID 1 et recherche le.
        dbf.updateProduct(id = 1, name = "The coffee god's finest")
        self.assertEqual(dbf.searchProduct(Name="The coffee god's finest").count(), 1, "Should return 1")
