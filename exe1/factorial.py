# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = int(input())
def fact(a):
    if a == 0 or a == 1:
        return 1
    return a * fact(a - 1)
print(fact(inp))
