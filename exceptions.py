try:
    age = int(input('Age: '))
    print(age)

    risk = 2000 / age
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print("age cannot be 0.")

