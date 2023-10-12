class Product:
    def __init__(self, id: int) -> None:
        self.__id = id
        self.name = ''
        self.__stock = 0
        self.__value = 0
        
    def get_id(self) -> int:
        return self.__id
    
    def get_value(self) -> int:
        return self.__value
    
    def set_value(self, value: int):
        if value <= 0:
            raise "Error: El valor no puede ser menor o igual que cero."
        self.__value = value

    def show(self):
        print(f"{self.__id} {self.name} {self.__value}")

    def add_stock(self, value: int):
        self.__stock = self.__stock + value

    def remove_stock(self, value: int):
        self.__stock = self.__stock - value

    def get_stock(self):
        return self.__stock