# Aquí programa una función que resuelva el problema 1 FizzBuzz
def fizzbuzz():
  for i in range(1, 101):
    #print(i)
    if i%3 == 0:
      if i%5 == 0:
        print("FizzBuzz")
      else:
        print("Fizz")
    elif i%5 ==0:
      print("Buzz")
    else:
      pass

fizzbuzz()