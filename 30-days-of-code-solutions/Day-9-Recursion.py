# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

print factorial(n)
