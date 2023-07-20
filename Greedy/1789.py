S = int(input())

now = 0
this = 0
cnt = 0

while (S - now) >= this:
  cnt += 1
  now += this
  this += 1
  
print(cnt-1)