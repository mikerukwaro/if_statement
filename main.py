
name = input("name: ")

if name == 'James':
    age == 12
    print(f'hello {name}, am {age} years old.')
    print('hello {}, am {} years old.'.format(name, age))

    age = input("age: ")
    if age >= '18':
        print("Access allowed ")
    else:
        print("Access denied")

elif name == 'Peter':
    print(f"Welcome back {name}")
    age = input("age: ")
    if age >= '18':
        print(f"Congrats {name}")
    else:
        print("Fail")

else:
    print("Not permitted!!!")
