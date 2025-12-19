from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    #URL
    URL = "https://www.saucedemo.com/"

    #selectores

    _INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")  
    _ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_COUNTER = (By.CLASS_NAME, "shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
  
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)       

    def obtener_todos_los_productos(self):
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEM))
        products = self.driver.find_elements(*self._INVENTORY_ITEM)
        return products
    
    def obtener_nombres_productos(self):
       productos = self.driver.find_elements(*self._ITEM_NAME)
       return [producto_nombre.text for producto_nombre in productos] 
    
    def agregar_primer_producto_al_carrito(self):
       productos = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEM))

       primer_boton_producto = productos[0].find_element(*self._ADD_TO_CART_BUTTON)
       primer_boton_producto.click()

    
    def agregar_producto_al_nombre(self, nombre_producto):
        producto = self.obtener_todos_los_productos()

        for producto in producto:
            nombre = producto.find_element(*self._ITEM_NAME).text
            if nombre.strip().lower () == nombre_producto:
                boton_agregar = producto.find_element(*self._ADD_TO_CART_BUTTON)
                boton_agregar.click()
                return self
            else: 
                raise Exception(f"Producto con nombre {nombre_producto} no encontrado")

    def abrir_carrito(self) :
        carrito = self.wait.until(EC.element_to_be_clickable(self._CART_LINK))
        carrito.click()
    

    def obtener_conteo_carrito(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._CART_COUNTER))
            contador = self.driver.find_element(*self._CART_COUNTER)
            return int(contador.text)
        except:
            return 0