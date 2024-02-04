import json
from order_model import Order
from user_model import User





class CakeManagementSystem:
    users_file = 'users.json'
    orders_file = 'orders.json'
    users:User
    orders:Order
    def __init__(self,name):
        self.name=name
        self.users = self.load_data(self.users_file)
        self.orders = self.load_data(self.orders_file)




    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def create_user(self, username, password):
        
        for user in self.users:
            if user['username'] == username:
                print("User already exists.")
                return
        self.users.append({'username': username, 'password': password})
        self.save_data(self.users_file, self.users)
        print("User created successfully.")

    def place_order(self, username, cake_type, quantity):
        order_id = len(self.orders) + 1
        self.orders.append({'order_id': order_id, 'username': username, 'cake_type': cake_type, 'quantity': quantity})
        self.save_data(self.orders_file, self.orders)
        print(f"Order placed successfully. Order ID: {order_id}")

    def view_orders(self, username):
        user_orders = [order for order in self.orders if order['username'] == username]
        if user_orders:
            for order in user_orders:
                print(f"Order ID: {order['order_id']}, Cake Type: {order['cake_type']}, Quantity: {order['quantity']}")
        else:
            print("No orders found for this user.")


cms1 = CakeManagementSystem(name='nishancms')
cms2 = CakeManagementSystem(name="bibekcms")


cms.create_user(username='ram',password='123')
cms.place_order(username="ram",cake_type="Choclate",quantity=2)
