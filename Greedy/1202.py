# n : 보석, k : 가방
n, k = map(int, input().split())

# m : 보석 무게, v : 보석 가격, c : 가방 수용 무게
m = []
v = []
c = []

for _ in range(n):
  mi, vi = map(int, input().split())
  m.append(mi)
  v.append(vi)

for _ in range(k):
  c.append(int(input()))

c.sort(reverse=True)

# for ci in c:
#   for mi in m:
    