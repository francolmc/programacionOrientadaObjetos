from product import Product

class ShoppingCart:
    def __init__(self, id: int) -> None:
        self.__id = id
        self.shoppingcart_client = None
        self.__products = list
        self.__creation_date = ""

    def get_id(self) -> int:
        return self.__id
    
    def get_creation_date(self) -> str:
        return self.__creation_date
    
    def set_creation_date(self, value: str):
        self.__creation_date = value

    def add_product(self, value: Product, quantity: int):
        value.remove_stock(quantity)
        self.__products.append(value)
    
