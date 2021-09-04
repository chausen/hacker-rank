def fib_ultimate(n):
    back2, back1, next = 1, 1, 0

    if n == 0: return 0
    
    for i in range(2, n):
        next = back1 + back2
        back2 = back1
        back1 = next

    return back1 + back2

print(fib_ultimate(4))
