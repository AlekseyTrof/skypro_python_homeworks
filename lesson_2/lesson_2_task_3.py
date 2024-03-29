def square(x):
    if x % 1 != 0:
        x = int(x) +1
    
    mul = x*x
    print(mul)


square(2.2)