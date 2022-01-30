number = str(input("Please write a number: "))
sum = 0
if int(number), < 0:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
  for i in range(len(number)):
    sum += int(number[i])**len(number)
  if sum == int(number):
    print(number, "is an Armstrong number")
  else:
    print(number, "is not an Armstrong number")