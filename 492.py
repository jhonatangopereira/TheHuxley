TEACHERS = 7

coffee_capsules = 0
for i in range(TEACHERS):
  box_quantity = int(input())
  size = input().lower()

  if size == 'p':
    coffee_capsules += box_quantity * 10
  elif size == 'g':
    coffee_capsules += box_quantity * 16

cups_of_coffee = int((coffee_capsules * 2) / TEACHERS)
print(coffee_capsules)
print(cups_of_coffee)
