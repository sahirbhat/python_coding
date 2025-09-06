dummy_data = {
    "users": [
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "age": 25,
            "roles": ["admin", "editor"]
        },
        {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com",
            "age": 30,
            "roles": ["viewer"]
        },
        {
            "id": 3,
            "name": "Charlie",
            "email": "charlie@example.com",
            "age": 35,
            "roles": ["editor", "viewer"]
        }
    ],
    "products": {
        101: {"name": "Laptop", "price": 1000, "quantity": 10},
        102: {"name": "Keyboard", "price": 50, "quantity": 100},
        103: {"name": "Mouse", "price": 20, "quantity": 200},
        104: {"name": "Monitor", "price": 150, "quantity": 50}
    },
    "settings": {
        "theme": "light",
        "notifications": True,
        "version": "1.0.0",
        "permissions": {
            "read": True,
            "write": False,
            "execute": False
        }
    },
    "logs": [
        {"id": 1, "action": "login", "user": "Alice", "timestamp": "2024-06-25 10:00:00"},
        {"id": 2, "action": "logout", "user": "Bob", "timestamp": "2024-06-25 10:30:00"},
        {"id": 3, "action": "update_profile", "user": "Charlie", "timestamp": "2024-06-25 11:00:00"},
    ]
}
# Find all users whose age is greater than 30.

# 1.1 Find all users whose age is greater than 30.
# 1.2 Find all products with a quantity less than 50.
# 1.3 Search for logs where the action is "login".
# 1.4 Find all users who have the role "editor".
# 1.5 Search for a product with the name "Mouse".
for user in dummy_data["users"]:
    if user["age"]>25:
        print(user)
low_qty={ info:values for info,values in dummy_data["products"].items()  if values['quantity']>50
}
print(low_qty)

for info,values in dummy_data["products"].items():
    if values["quantity"]==100:
        print(info,values)
for k in dummy_data["logs"]:
    if k["action"]=='login':
        print(k)
      

for user in dummy_data["users"]:
    if user["roles"]=="editor":
        print(user)
# 1.2 Find all products with a quantity less than 50.
print("problem2")
for product_key,product_value in dummy_data["products"].items():
    if product_value['quantity'] < 50:
        print(product_key,product_value)
print("problem 3")        
product_less_than={product_key:product_value for product_key ,product_value in dummy_data["products"].items() if product_value['quantity']<50}       
print(product_less_than)
print("prpblem 4 ")


# 1.3 Search for logs where the action is "login".

for data in dummy_data["logs"]:
    if data["action"] =="login":
        print(data)
print("___________________________")        
data_user_login=[ data for data in dummy_data["logs"] if data["action"]=="login"]  
print(data_user_login)  


# 1.5 Search for a product with the name "Mouse"

for data_key,data_value in dummy_data["products"].items():
    if data_value["name"]=="Mouse":
        print(data_key,data_value)
print(".................................................................................")
data_mouse={ data_key:data_value for data_key,data_value in dummy_data["products"].items() if data_value["name"]=="Mouse"}
print(data_mouse)



