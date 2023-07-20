n = int(input())

cnts = []

for i in range(n//5+1):
  # print(f'i : {i}')
  temp = 5*i
  # print(f'temp : {temp}')
  if (n - temp) % 2 == 0:
    # print(f'temp // 2 : {(n - temp) // 2}')
    # print(f'(n - temp) % 2 {i+(n-temp)//2}')
    cnts.append(i + (n-temp)//2)
  elif n - temp == 0:
    # print(f'n - temp {temp}')
    cnts.append(temp)

if not cnts:
  print(-1)
else:
  # print(cnts)
  print(min(cnts))