res = 0
def sum_fn(value):
    global res
    res = res + value
    print res

tuple1 = (1,2,3,4,5,6,7,8,9,0)
for i in tuple1:
    sum_fn(i)

