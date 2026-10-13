def outer():
    def inner():
        print("this is inner ")

    return inner
result = outer()
result()
