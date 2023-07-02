n = int(input())

timeline = []

for i in range(n):
  s, e = map(int, input().split())
  timeline.append([s, e])

timeline.sort(key=lambda x : x[0])
timeline.sort(key=lambda x : x[1])

cnt = 1
end = timeline[0][1]

for i in range(1, n):
  if timeline[i][0] >= end:
    end = timeline[i][1]
    cnt += 1

print(cnt)  