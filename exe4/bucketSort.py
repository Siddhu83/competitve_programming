# Enter your code here. Read input from STDIN. Print output to STDOUT

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr, n):
    if n <= 1:
        return arr
    buckets = [[] for _ in range(n)]
    
    for num in arr:
        bucket_index = min(int(n * num), n - 1) 
        buckets[bucket_index].append(num)
        
    for i in range(n):
        insertion_sort(buckets[i])
    
    sorted_arr = []    
    for bucket in buckets:
        sorted_arr.extend(bucket)
        
    return sorted_arr

s = int(input())
nums = list(map(float, input().split()))
res = sorted(nums)
for i in res:
    print(i, end=' ')
