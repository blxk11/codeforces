s = int(input())
n = input()
n = n.lower()
if len(set(n)) == 26:
    print("YES")
else:
    print("NO")  
# s = "TheQuickBrownFoxJumpsOverTheLazyDog"
# s = s.lower()
# print(set(s))