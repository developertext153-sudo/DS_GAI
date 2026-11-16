# Complex Data Type is used to represent complex numbers, which consist of real and an imaginary part
# BuiltIn function in python

# Creating a complex Number
# Syntax : var=real+ imaginary*1j
c1=10+20j
print(c1)

# Printing the real part
print(c1.real) # 10

# Printing the imaginary part
print(c1.imag) # 20

# Operation with complex numbers
c1=10+20j
c2=20+30j

# Addition
print(c1+c2) # 30+50j

# Subtractions
print(c1-c2) # (-10-10j)

# Multiplication
print(c1*c2) # (-400+700j)

# Division
print(c1/c2) #(0.6153846153846154+0.0769230769230769j)

# abs(c1): Returns the magnitude(absolute value) of the complex number.
# conj(c1): Returns the complex conjugate of the number
print(abs(c1))
print(c1.conjugate())