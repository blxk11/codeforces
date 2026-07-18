n = int(input())
for _ in range(n):
    w = int(input())
    for _ in range(w): 
        s, k  = map(int, input().split())
        if s == k :
            print("YES")
        else:
            print("NO")
            
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if s % 4 == 0:
        print("YES")
    else:
        print("NO")