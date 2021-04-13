

def recursive_function(i):
    if i == 100:
        return
    print("현재는: ", i," 입니다.")
    recursive_function(i+1)
    print(i, " 번째 재귀함수를 종료합니다.")

recursive_function(1)
def recursive_function_fibo(n):
    if n<=1:
        return 1
    return n * recursive_function_fibo(n-1)

print(recursive_function_fibo(5));