import math
n,m,a = map(int, input().split())
c = math.ceil(n/a) * math.ceil(m/a)
print(c)
