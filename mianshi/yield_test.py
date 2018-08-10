def test1():
    for i in range(2):
        print('+' + str(i))
        yield str(i)


for a in test1():
    print("-" + a)


for a in list(test1()):
    print('-' + a)