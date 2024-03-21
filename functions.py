def greet(name):
    """
    Simple greet function, prints hello
    :param name: string
    :return: None
    """
    print(f"hello, {name}")

    #greet("bogdan")

def special_op(x=10,y=10,z=10):
    """
    some special operation
    :param x: int or float
    :param y: int or float
    :param z: int or float
    :return: the result of the operation
    """
    return x * y + z
result = special_op(2,3,4)
print(result)
print(special_op(2,3,))