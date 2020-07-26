def feibonacci(n):
    a = 1
    b = 0
    while n >0:
        if a%2 == 0:
            print(a,end='  ')
        a, b = a+b, a
        n -= 1

feibonacci(100)
