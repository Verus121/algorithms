def fib(n):
    if n == 0 or n == 1:
        return 1

    a = 1
    b = 1
    for i in range(2, n):
        temp = a 
        a = a + b 
        b = temp 
    
    return a


print(fib(20000))