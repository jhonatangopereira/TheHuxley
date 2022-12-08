N = int(input())

result = "Falso"
for i in range(1, int(N / 2)):
  if i * (i + 1) * (i + 2) == N:
    result = f"{i} * {i + 1} * {i + 2} = {N}\nVerdadeiro"
    break

print(result)
