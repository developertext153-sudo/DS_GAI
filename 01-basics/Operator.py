# Arithmetic Operations in Python
# Integers

print('Addition:', 2 + 3) # Addition: 5
print('Subtraction:', 3 - 2) # Subtraction: 1
print('Multiplication:', 2 * 3) # Multiplication: 6
print('Division:', 3 / 2) # Division: 1.5
print('Exponentiation:', 3 ** 2) # Exponentiation: 9
print('Modulus:', 3 % 2) # Modulus: 1
print('Floor Division:', 3 // 2) # Floor Division: 1    



# Floating Point Numbers
print('Floating Number, PI:',3.14) # Floating Number, PI: 3.14
print('Floating Number, gravity:',9.81) # Floating Number, gravity: 9.81    

# Complex Numbers
a1=10+20j
                                
a2=20+30j

print('Complex Number:',a1) # Complex Number: (10+20j)
print('Complex Number:',a2) # Complex Number: (20+30j)
print('Real Part of Complex Number:',a1.real) # Real Part of Complex Number: 10.0
print('Imaginary Part of Complex Number:',a1.imag) # Imaginary Part of Complex Number: 20.0

a3=a1+a2
print('Addition of Complex Numbers:',a3) # Addition of Complex Numbers: (30+50j)
a4=a1-a2
print('Subtraction of Complex Numbers:',a4) # Subtraction of Complex Numbers: (-10-10j)
print('Real part of Complex Number:',a4.real) # Real part of Complex Number: -10.0
print('Imaginary part of Complex Number:',a4.imag) # Imaginary part of Complex Number: -10.0

# Declaring the variables at the top first
a=3 # a is a variable name 3 is an integer data type
b=2 # b is a variable name 2 is an integer data type

# Arithmetic Operations and assigning the result to a variable
total=a+b # total is a variable name a+b is an arithmetic operation
diff=a-b # diff is a variable name a-b is an arithmetic operation
product=a*b # product is a variable name a*b is an arithmetic operation
division=a/b # division is a variable name a/b is an arithmetic operation
remainder=a%b # remainder is variable name a%b is arithmetic operation
floor_division=a//b # floor_division is variable name a//b is arithmetic operation
exponentiation=a**b # exponentiation is variable name a**b is arithmetic operation

# Printing the values with labels
print('Total:',total) # Total: 5
print('Difference:',diff) # Difference: 1
print('Product:',product) # Product: 6
print('Division:',division) # Division: 1.5
print('Remainder:',remainder) # Remainder: 1
print('Floor Division:',floor_division) # Floor Division: 1
print('Exponentiation:',exponentiation) # Exponentiation: 9

# I should have used sum instead of total, but I wanted to show you that you can use any variable name you want.
print(total) # 5 # If you don't label your print statement, it will just print the value of the variable.
print('a+b',total) # a+b 5 # If you label your print statement, it will print the label and the value of the variable.
print('a-b',diff) # a-b 1
print('a*b',product) # a*b 6
print('a/b',division) # a/b 1.5
print('a%b',remainder) # a%b 1
print('a//b',floor_division) # a//b 1
print('a**b',exponentiation) # a**b 9

# Declaring values and organizing them together
num_one=10
num_two=20


# Arithmetic Operations with Variables
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_one%num_two
floor_division=num_one//num_two
exponentiation=num_one**num_two

print('Total:',total) # Total: 30
print('Difference:',diff) # Difference: -10
print('Product:',product) # Product: 200
print('Division:',division) # Division: 0.5
print('Remainder:',remainder) # Remainder: 10
print('Floor Division:',floor_division) # Floor Division: 0
print('Exponentiation:',exponentiation) # Exponentiation: 10000000000   

# Calculating the area of a circle
radius=5
area=3.14*radius**2
print('Area of Circle:',area) # Area of Circle: 78.5

# Calculating the area of a rectangle
length=10
width=5     
area=length*width
print('Area of Rectangle:',area) # Area of Rectangle: 50

# Calculating the area of a triangle
base=10
height=5
area=0.5*base*height
print('Area of Triangle:',area) # Area of Triangle: 25.0

# Calculating the weight of an object
mass=10
gravity=9.81    
weight=mass*gravity
print('Weight of Object:',weight) # Weight of Object: 98.1

print(3>2) # True
print(3<2) # False          
print(3>=2) # True
print(3<=2) # False
print(3==2) # False
print(3!=2) # True  
print(len('Hello')==5) # True
print(len('Hello')==len('mango')) # False
print(len('Hello')!=len('mango')) # True
print(len('Hello')<len('mango')) # True
print(len('Hello')>len('mango')) # False