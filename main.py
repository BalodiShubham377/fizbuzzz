for num in range(1, 101):
  if num % 3 == 0 and num % 7 == 0:
      print("FizzBuzz")
  elif num % 3 == 0:
      print("Buzz")
  elif num % 7 == 0:
      print("Fizz")
  else:
      print(num)
