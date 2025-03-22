# Assignment 1
#1
Num1 = 10
Num2 = 30
Add = Num1 + Num2

print(Add)

#2
BMI = int(input("Enter your BMI: "))
if BMI < 18.5:
  print("You are underweight")
elif BMI < 25:
  print("You are normal")
elif BMI < 30:
  print("You are overweight")
else:
  print("You are obese")

# Assignment 2
#1
InstituteName = input("Enter your Institute Name: ")
print(InstituteName)

#2
Name = input("Enter your name: ")
Age = input("Enter your age: ")
SchoolName = input("Enter your school name: ")
Degree = input("Enter your drgree: ")

#3
Num1 = 10
Num2 = 30
Add = Num1 + Num2

print(Add)

#4
Num1 = 10
Num2 = 30
Sub = Num1 - Num2

print(Sub)

#5
Num1 = 10
Num2 = 30
Mul = Num1 * Num2

print(Mul)

#6
Num1 = 76
Num2 = 31
Div = Num1 / Num2

print(Div)

#7
Num1 = 76
Num2 = 31
DivFloor = Num1 // Num2

print(DivFloor)

#8
Num1 = 76
Num2 = 31
Modulo = Num1 % Num2

print(Modulo)

#9
Num1 = 4
Num2 = 4
Pow = Num1**Num2
print(Pow)

# Assignments 3
#1
for num in range(0, 20):
  print(num)

#2
for num in range(10, 20):
  print(num)

#3
list = [10, 20, 14, 55, 43, 87, 76]
print("Number of item in the List: ", len(list))

#4
word = "Artificial Intelligence"
for chr in word:
  print(chr)

#5
Name = input("Enter your name: ")
Age = input("Enter your age: ")
Profession = input("Enter your Profession: ")
print("Your Name- ", Name)
print("Your Age- ", Age)
print("Your Profession- ", Profession)

#6
tup = (1, 'Welcome', 2, 'Hope')
print(tup)

#8
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'HOPE')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

#9
tuple = (20, 10, 16, 19, 25, 1, 276, 188)
for num in tuple:
  if num % 2 != 0:
    print(num, "is odd")

#10
tuple = (20, 10, 16, 19, 25, 1, 276, 188)
for num in tuple:
  if num % 2 == 0:
    print(num, "is even")

# Asignment 4

#1
value = 10
if value == 10:
  print("CORRECT")

#2
password = input("Enter the password: ")
passKey = "HOPE@123"
if (password == passKey):
  print("Your password is correct")
else:
  print("Your password is incorrect")

#3
age = int(input("Enter your age: "))
if age < 18:
  print("children")
elif age < 30:
  print("adult")
elif age < 60:
  print("citizen")
else:
  print("senior citizen")

#4
num = int(input("Enter a number: "))
if num >= 0:
  print("Positive")
else:
  print("Negative")

#5
num = int(input("Enter a number to check div by 5: "))
if num % 5 == 0:
  print("Divisible by 5")
else:
  print("Not divisible by 5")

# Asignment 5


class MulFunctions():
  #1
  def Subfields(self):
    subfields = [
        "Machine Learning", "Neural Networks", "Vision", "Robotics",
        "Speech Processing", "Natural Language Processing"
    ]
    print("Sub-fields in AI are:")
    for field in subfields:
      print(field)

#2

  def OddEven(self):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
      print(f"{num} is Even number")
    else:
      print(f"{num} is Odd number")

#3

  def Elegible(self):
    gender = input("Your Gender (Male/Female): ").strip().lower()
    age = int(input("Your Age: "))

    if (gender == "male" and age >= 21) or (gender == "female" and age >= 18):
      print("ELIGIBLE")
    else:
      print("NOT ELIGIBLE")

#4

  def percentage(self):
    marks = []
    for i in range(5):
      marks.append(int(input(f"Subject{i+1}: ")))
    total = sum(marks)
    percentage = (total / 500) * 100
    print(f"Total: {total}")
    print(f"Percentage: {percentage}")


#5

  def triangle(self):
    height = float(input("Height: "))
    breadth = float(input("Breadth: "))
    area = (height * breadth) / 2
    print("Area formula: (Height*Breadth)/2")
    print(f"Area of Triangle: {area}")

    height1 = float(input("Height1: "))
    height2 = float(input("Height2: "))
    breadth = float(input("Breadth: "))
    perimeter = height1 + height2 + breadth
    print("Perimeter formula: Height1 + Height2 + Breadth")
    print(f"Perimeter of Triangle: {perimeter}")

mul_functions = MulFunctions()
print(mul_functions.Subfields())
print(mul_functions.OddEven())
print(mul_functions.Elegible())
print(mul_functions.percentage())
print(mul_functions.triangle())
