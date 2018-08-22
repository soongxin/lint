d = {'d': 2, 'f': 2, 'c': 5, 'b': 6, 'a': 7}

def f(x):
    key = x[1]
    return key

s = sorted(d.items(), key=f)

print(s)