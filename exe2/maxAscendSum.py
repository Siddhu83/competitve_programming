# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
nums = list(map(int, input().split()))

def maxAscendSum(n, nums):
    maxSum = curSum = nums[0]
    for i in range(1, n):
        curSum += nums[i]

        if nums[i] < nums[i - 1]:
            curSum = 0    
                
        if maxSum < curSum:
            maxSum = curSum
            
    print(maxSum)
    return maxSum
    
maxAscendSum(n, nums)
