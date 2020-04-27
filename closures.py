# A closure is a record storing a function together wiht an environment: a mapping associateing each free variable of the function with the value or staorage location to which the name was bound when the closure was created. A closure, unlike a plain function, allows the function to access those captured variables throught eh closure's reference to them, even when the function is invoked outside their scope.


def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func()


outer_func()

# ok so the outter function is created which sets the message variable to hi. then we see the inner function prints that message. it returns itself invoked. let's now use this same code but not return that inner function invoked.


def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func()
