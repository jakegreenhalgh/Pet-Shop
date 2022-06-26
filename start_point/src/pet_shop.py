# WRITE YOUR FUNCTIONS HERE
from ast import Pass


def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, amount):
    shop["admin"]["pets_sold"] += amount

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    breed_list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list

def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].insert(0, new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet_name):
    customer["pets"].append(pet_name)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet, customer):
        print('pet')
        print(pet)
        if pet == None:
            return None
        elif customer_can_afford_pet(customer, pet) == True:
            indexno = shop["pets"].index(pet)
            customer["cash"] -= shop["pets"][indexno]["price"]
            shop["admin"]["pets_sold"] += 1
            shop["admin"]["total_cash"] += shop["pets"][indexno]["price"]
            shop["pets"].pop(indexno)
            customer["pets"].append(pet)
        else:
            return None


