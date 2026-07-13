# Enter your code here. Read input from STDIN. Print output to STDOUT

s = int(input())
nums = list(map(int, input().split()))

def findMajor(n, nums):
    nums.sort()
    mid = n // 2
    candidate = nums[mid]
    res = candidate if nums.count(candidate) > mid else -1
    print(res)
    return res
    
findMajor(s, nums)
