n = int(input())
w = []
for _ in range(n):
  w.append(int(input()))

w.sort()

weight = min(w) * n

rw = [x * (n - i) for i, x in enumerate(w)]

print(max(rw))