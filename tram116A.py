n = int(input( ))
current = 0
count = []
for _ in range(n):
    k , b = list(map(int,input( ).split()))
    current = current - k + b
    a = current + a
    
    print(a)
    
    