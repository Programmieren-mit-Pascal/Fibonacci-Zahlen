from sys import setrecursionlimit

setrecursionlimit(20000)

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    fib_values = [0] * (n+1)
    fib_values[1] = 1
    fib_values[2] = 1
    for i in range(3, n+1):
        fib_values[i] = fib_values[i-1] + fib_values[i-2]
    return fib_values[n]


def fib_top_down(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_top_down(n-1) + fib_top_down(n-2)


def fib_memo_calc(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_memo_calc(n-1, memo) + fib_memo_calc(n-2, memo)
    memo[n] = result
    return result

def fib_top_down_memo(n):
    memo = [None] * (n+1)
    return fib_memo_calc(n, memo)


#result = fib_top_down(35)
#result = fib_top_down_memo(100)
result = fib_bottom_up(100)

print("Result: ", result)