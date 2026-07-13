# Enter your code here. Read input from STDIN. Print output to STDOUT
s = int(input())
nums = list(map(int, input().split()))

def maxSubSum(s, nums):
    dp = [0] * s
    dp[0] = maxSum = nums[0]
    for i in range(1, s):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        maxSum = max(maxSum, dp[i])
    return maxSum
    
res = maxSubSum(s, nums)
print(res)
