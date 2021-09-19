#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst_products = [
                'Beans,Peas,Corn', 'Beverages and Drinks', 'Bread', 'Cakes', 'Cookies and Crackers',
                'Dairy products', 'Dried fruits', 'Fruits', 'Grain', 'Grain products', 
                'Herbs and Spices', 'Ice cream', 'Sauces', 'Sweets and chocolates', 'Vegetables'

products = {}
buyer = {}
for i in range(1, len(lst_products) + 1):
    products[i] = {"name": lst_products[i - 1], "Available_Quantity" : 10, "price" : 10, "discount" : 0 }   # int(input(f"Enter the {lst_products[i - 1] } price : "))
# print(products)

def purchase(products, buyer):
    while True:
        name = input("Enter the name of buyer: ")
        if name == "":
                break
        Buyer_purchased = int(input("Enter the Total product buyed by buyer : "))
        for i in range(Buyer_purchased):
            product_ID = int(input("Enter the product ID : "))
            buyer[name] = products[product_ID]["name"]

            Quantity = int(input("Enter the quantity want to buy : "))

            if Quantity > products[product_ID]["Available_Quantity"]:
                print("Qantity available is ", products[product_ID]["Available_Quantity"])
            else:
                buyer["purchased quantity"] = Quantity
                buyer["price"] =  Quantity * products[product_ID]["price"]
                products[product_ID]["Available_Quantity"] =  products[product_ID]["Available_Quantity"] - buyer["purchased quantity"]
        
purchase(products, buyer)
print(buyer)
print(products)

products_file = open("Inventory.json", "w+")
for i in range(15):
    products_file.write(json.dumps(products[i + 1], indent = 4) + "\n")
products_file.close()

