def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid +1
        print('mid: ',mid, 'array[mid]: ',array[mid])
    return None

n, target = list(map(int,input().split()))
array = list(map(int, input().split()))
array.sort()    # binary search의 핵심. 정렬된 데이터.

print('n:',n)
print('target:',target)
result = binary_search(array,target,0,n-1)

if result == None:
    print("찾는 숫자가 없다.")
else:
    print(result+1)