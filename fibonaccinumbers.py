fibonacci = []

sum_num = 0

for i in range(20):
  if i == 0:
    fibonacci.append(0)
  elif i == 1 or i == 2:
    fibonacci.append(1)
  elif i > 2 and sum_num < 55:
    sum_num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(sum_num)

print(fibonacci)