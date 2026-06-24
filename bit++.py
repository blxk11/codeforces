n = int(input( ))
count = 0
for i in range(n):
    c = input( )
    if c[1] == "+":
        count += 1
    elif c[1] == "-":
        count -= 1
print(count)
    