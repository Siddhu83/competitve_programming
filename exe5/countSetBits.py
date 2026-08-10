# Enter your code here. Read input from STDIN. Print output to STDOUT
def countBits(n):
    c = 0
    while n != 0:
        n = n & (n - 1)
        c += 1
    return c
    
n = int(input())
print(countBits(n))
