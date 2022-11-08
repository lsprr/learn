name = 'Luis'  # global scope


def display_name():
    name = 'Test'  # local scope
    print(name)


display_name()
print(name)
