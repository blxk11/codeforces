n = int(input( ))
current = 0
max_passengers = 0
for _ in range(n):
    k , b = list(map(int,input( ).split()))
    current = current - k + b
    max_passengers = max(max_passengers, current)
print(max_passengers)