class User:
    def __init__(self, id = "", name = "", username = "", email = "", phone = "", website = "") -> None:
        self.__id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website

    def get_id(self):
        return self.__id
    
    def set_from_json(self, djson):
        self.__id = djson["id"]
        self.name = djson["name"]
        self.username = djson["username"]
        self.email = djson["email"]
        self.phone = djson["phone"]
        self.website = djson["website"]
    
    def __str__(self) -> str:
        return f"Usuario {self.name} {self.email}"