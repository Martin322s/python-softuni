divisor = int(input())
boundary = int(input())

N = (boundary // divisor) * divisor

# boundary // divisor - finds the biggest inger below boundary
# result * divisor - finds the biggest number between them

print(N)
