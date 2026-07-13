# Enter your code here. Read input from STDIN. Print output to STDOUT

sizes = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def findMedian(n, arr1, m, arr2):
    i = j = med = aux = 0
    for _ in range((n + m) // 2 + 1):
        aux = med    
        if i < n and j < m:
            if arr1[i] < arr2[j]:
                med = arr1[i]
                i += 1
            else:
                med = arr2[j]
                j += 1
        elif i < n:
            med = arr1[i]
            i += 1
        else:
            med = arr2[j]
            j += 1
        
    if (n + m) & 1:
        res = float(med)
            
    else:
        res = (med + aux) / 2

    return res
    
median = findMedian(sizes[0], arr1, sizes[1], arr2)
print(median)


