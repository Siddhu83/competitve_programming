# Enter your code here. Read input from STDIN. Print output to STDOUT

def divison(dividend, divisor):
    shift = 0
    quo = 1
    while divisor << shift <= dividend:
        shift += 1
    for s in range(shift, -1, -1):
        if divisor << s <= dividend:
            dividend -= divisor << s
            quo |= 1 << s
    print(quo)
    return quo
    
divi = int(input())
dsor = int(input())
divison(divi, dsor)
