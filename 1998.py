N = int(input())
M = int(input())

for i in range(N, M + 1):
  for j in range(1, 10):
    print(f"{i} x {j} = {i * j}")
  print("")