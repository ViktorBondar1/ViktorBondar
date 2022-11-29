def zad3(*args):
    print(args)
    for a in args :
        print(a)
    print()
#zad3(3, 31.21, "lis",["pies", "kot"])
#zad3(1.2, 3, "małpa")
#zad3()

def max(*args):
    m = num1
    for i in args:
        if m < i:
            m = i
    return  m
print(max(1, -4, 6))
