n1, n2 = 0, 0

res = 0.0

n1 = int(input("digite um número positivo"))

n2 = int(input("digite outro número positivo"))

if (n1 > n2):
  res = (n1-n2)
else:
  res = (n2-n1)
print(res)