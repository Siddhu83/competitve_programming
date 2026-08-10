# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
k = int(input())

isSet = n & (1 << (k))
print(1 if isSet else 0)
