# Enter your code here. Read input from STDIN. Print output to STDOUT

s1 = int(input())
arr1 = list(map(int, input().split()))

s2 = int(input())
arr2 = list(map(int, input().split()))

def mergeArrays(s1, arr1, s2, arr2):
    res = []
    i = j = 0
    while i < s1 and j < s2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
            
    if i < s1:
        res = res + arr1[i:]
    else:
        res = res + arr2[j:]
        
    return res
    
mergedRes = mergeArrays(s1, arr1, s2, arr2)

for i in mergedRes:
    print(i, end = ' ')