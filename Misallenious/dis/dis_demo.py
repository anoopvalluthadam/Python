import dis
def my_function(a, b):
    value = a + b
    return value
dis.dis(my_function)
