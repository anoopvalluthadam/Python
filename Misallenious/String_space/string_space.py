
def space_generation(var):
    space = ' '
    for ch in range(var):
        space += space
    return space
print space_generation(1), 'hi'
