
def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

def fibo_dp(n):
    cache = [0 for i in range(n+1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2,n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]



# result1 = fibo_recursive(35)
result2 = fibo_dp(55550)

print(result2)