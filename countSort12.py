n = int(input())
nums = list(map(int, input().split()))

def countingSort(n, nums):
    maxi = max(nums)
    freq = [0] * (maxi + 1)
    res = [0] * n
    
    for i in nums:
        freq[i] += 1
        
    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]
        
    for i in nums[::-1]:
        res[freq[i] - 1] = i
        freq[i] -= 1
    
    return res
        
sortedArr = countingSort(n, nums)
for i in sortedArr:
    print(i, end=' ')