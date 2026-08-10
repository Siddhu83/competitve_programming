# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

def findThreeSum(n, x, nums):
    triplets = []
    nums.sort()
    
    for i in range(n - 2):
        j, k = i + 1, n - 1
        target = x - nums[i]
        while j < k:
            s = nums[j] + nums[k]
            if s == target:
                triplets.append([nums[i], nums[j], nums[k]])
                k -= 1
                j += 1
            elif s > target:
                k -= 1
            else:
                j += 1
                
    if not triplets:
        print('No Triplets Found.')
        return
        
    for t in triplets:
        print(t[0], t[1], t[2])
    return
    
findThreeSum(n, x, nums)
        
