import requests
from datetime import datetime

class Customer:
    def __init__(self, url = "https://localhost:5000", selected_customer = None):
        self.url = url
        self.selected_customer = selected_customer

    def add_customer(self, name = "Default Name", phone = None, postal_code = None, registered_at = None):
#adds a customer with query_params collected from MAIN
        query_params = {
            "name" : name,
            "phone" : phone,
            "postal_code" : postal_code
        }
        response = requests.post(self.url+"/customers", json = query_params)
        return response.json()
    
    def update_customer(self, name, phone, postal_code):
#updates customer with query_params collected from MAIN
        if not name:
            title = self.selected_video["title"]
        if not phone:
            release_date = self.selected_video["release_date"]
        if not postal_code:
            total_inventory = self.selected_video["total_inventory"]
        query_params = {
            "name" : name,
            "phone" : phone,
            "postal_code" : postal_code
        }
        response = requests.put(self.url+f"/customers/{self.selected_customer['id']}", json=query_params)
        self.selected_customer = response.json()["customer"]
        return response.json()
    
    def list_customers(self):
#lists customers
        response = requests.get(self.url+"/customers")
        return response.json()
    
    def get_customer(self, name=None, id=None, phone=None, postal_code=None):
#gets customer by name, phone, or id
        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    self.selected_customer = customer
                    id = customer["id"]
            elif phone:
                if customer["phone"]==phone:
                    self.selected_customer = customer
                    id = customer["id"]
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "I'm sorry, I couldn't find that customer."
        
        response = requests.get(self.url+f"/customers/{id}")

        return response.json()

    def delete_customer(self):
#deletes one customer by id
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
        
    def print_selected(self):
#prints customer selected with name
        if self.selected_customer:
            print(f"Customer {self.selected_customer['name']} is currently selected.")
        else:
            print("Sorry, I couldn't find that customer.")