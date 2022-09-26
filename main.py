L = True

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  try:
    return x / y
  except ZeroDivisionError:
    print("Undefined: Division by 0")

print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Division")
print ("5. 🖕")
value = input("Enter number for operation (1,2,3,4,5): ")

try:
  value = float(value)
  if value == 1:
    firstValueAdd = float(input("Enter first number: "))
    secondValueAdd = float(input("Enter second number: "))
    print (firstValueAdd, "+", secondValueAdd, "=",     add(firstValueAdd, secondValueAdd))

  if value == 2:
    firstValueSub = float(input("Enter first number: "))
    secondValueSub = float(input("Enter second number: "))
    print (firstValueSub, "-", secondValueSub, "=", subtract(firstValueSub, secondValueSub))

  if value == 3:
    firstValueMul = float(input("Enter first number: "))
    secondValueMul = float(input("Enter second number: "))
    print (firstValueMul, "x", secondValueMul, "=", multiply(firstValueMul, secondValueMul))
  
  if value == 4:
      firstValueDiv = float(input("Enter first number: "))
      secondValueDiv = float(input("Enter second number: "))
      print (firstValueDiv, "/", secondValueDiv, "=", divide(firstValueDiv, secondValueDiv))
    
  
  if value == 5:
    while L == True:
      print("L")
except ValueError:
  print("Please input a number 1-5")


