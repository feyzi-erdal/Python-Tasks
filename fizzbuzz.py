number = int(input("Please enter a number: "))
if 1 <= number <= 100:
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("Buzz")
  elif number % 3 == 0:
    print("Fizz")
else:
  print(number)