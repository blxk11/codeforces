n , k = map(int, input( ).split())
scores = list(map(int, input( ).split()))
count = 0
threshold = scores[k-1]  
for i in range(n): 
     
    if scores[i] >= threshold and scores[i] > 0:
        count += 1
print(count)
            