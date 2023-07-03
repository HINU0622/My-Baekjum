from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for edges in graph:
  edges.sort()

visited = [False] * (n+1)
visited_bfs = [False] * (n+1)

def DFS(s):
  visited[s] = True
  print(s, end=' ')
  for i in graph[s]:
    if not visited[i]:
      DFS(i)

def BFS(start):
  queue = deque([start])
  
  visited_bfs[start] = True
  
  while queue:
    s = queue.popleft()
    print(s, end=' ')
    for i in graph[s]:
      if not visited_bfs[i]:
        queue.append(i)
        visited_bfs[i] = True

DFS(v)
print()
BFS(v)