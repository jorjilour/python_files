print(10**2)

x=10

#same same
x=x+3
x+=3

#follows PEMDAS unless parentheses is used
x = 10 + 3 * 2
y = (10 + 3) * 2

''''> , >=, <, <='''

price=5
print(price > 10 and price < 30)
print(price > 10 or price < 30)
print(not price < 30)

###IF STATEMENTS
temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: #20-30
    print("It's a nice day")
elif temperature > 10: #10-20
    print("It's a bit cold")
else:
    print("It's cold")




