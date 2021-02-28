customer = {
    "name": "John Smith",
    "age": 40,
    "is_verified": True
}

'''
For more dictionary methods
https://www.w3schools.com/python/python_dictionaries_methods.asp 
'''

print(customer["age"])
print(customer.get("birthdate"))
print(customer.keys())
print(customer.values())
customer.update({"marital_status":"single"})
print(customer.items())


customer["birthdate"] = "Jan 1 1980"

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

phone = input("Phone: ")

output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "
print(output)


def greet_user(first, last):
    print(f"Hi {first} {last}!")


greet_user(last="john", first="smith")


