
result = 0

def sum_fn(value):
    global result
    result = result + value
    return result

list1 = []
for i in range(10):
    list1.append(i)
for value in list1:
    res = sum_fn(value)
    print res
