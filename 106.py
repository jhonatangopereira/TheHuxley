N = int(input())

anterior = 0
atual = 1
if N == 1:
  print(f"{anterior}", end="")
else:
  print(f"{anterior} {atual}", end="")
  for i in range(2, N):
    proximo = anterior + atual
    print(f" {proximo}", end="")
    anterior = atual
    atual = proximo
print()