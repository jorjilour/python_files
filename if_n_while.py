weight = float(input("Weight: "))

unit_system = input("(K)g or (L)g: ")
unit_system = unit_system.lower()
print(unit_system)
if 'k' in unit_system or 'l' in unit_system:
    if unit_system == 'k':
        weight /= 0.45
        print("Weight in Lbs: %.2f" % weight)

    elif unit_system == 'l':
        weight *= 0.45
        print("Weight in Kgs: %.2f" % weight)


else:
    unit_system = input("Please enter either k or l: ")


###WHILE###
i=1
while i <= 5:
    print(i)
    i += 1

i=1
while i <= 10:
    print(i * '*')
    i += 1