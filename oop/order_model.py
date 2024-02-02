class Order:
    username:str
    cake_type:str
    quantity:int
    def __init__(self, username, cake_type, quantity):
        self.username = username
        self.cake_type = cake_type
        self.quantity = quantity