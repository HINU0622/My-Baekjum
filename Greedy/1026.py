def S(l1, l2):
  c = 0
  for a, b in zip(l1, l2):
    c += a * b
  return c

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

print(S(A, B))