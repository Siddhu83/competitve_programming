# Enter your code here. Read input from STDIN. Print output to STDOUT

s = int(input())
nums = list(map(int, input().split()))

def interchangeMinMax(s, nums):
    mini = maxi = 0
    for i in range(s):
        if nums[i] < nums[mini]:
            mini = i
        if nums[i] > nums[maxi]:
            maxi = i
            
    nums[maxi], nums[mini] = nums[mini], nums[maxi]
    return nums
    
res = interchangeMinMax(s, nums)
for i in res:
    print(i, end=' ')
