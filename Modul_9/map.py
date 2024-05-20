list1 = [1,2,5,7,12,11,35,4,89,10]

def my_sq(x: int) -> int:
    return x ** 2


list_sq = list(map(my_sq, list1))
list_fl = list(filter(lambda x: (x % 2 != 0), list_sq))

print(list_sq)
print(list_fl)