n = int(input())
money = 1000 - n

ml = [500, 100, 50, 10, 5, 1]
count = 0

for m in ml:
  count += money // m
  money %= m
  
print(count)