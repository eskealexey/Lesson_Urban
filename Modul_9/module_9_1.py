def quadr(n: list):
    res = []
    for x in n:
        y = x * x
        res.append(y)
    return res

def apply_full_func(int_list: list, *functions):
    results = {}
    for func in functions:
        func(int_list)
        results[func.__name__] = func(int_list)
    return results


print(apply_full_func([6, 20, 15, 9], max, min))
print(apply_full_func([6, 20, 15, 9], len, sum, sorted))
print(apply_full_func([6, 20, 15, 9], quadr, max, min, len, sum, sorted))


