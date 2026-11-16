# Single line comment
letter='P'
print(letter)
print(len(letter)) # 1
greeting='Hello, World!'
print(greeting)
print(len(greeting)) # 13
sentence="This is a string"
print(sentence)
print(len(sentence)) # 16

# Multiline String
multiline_string='''This is a multiline string.
It can span multiple lines.'''
print(multiline_string)

# Another way of doing multiline string
multiline_string2="""This is another way of doing multiline string.     
It can also span multiple lines."""
print(multiline_string2)

# String Concatenation
first_name='Prashant'
last_name='Pandey'
space=' '
full_name=first_name+space+last_name
print(full_name)

# Checking the length o a string using len() function
print(len(first_name)) # 8
print(len(last_name)) # 6
print(len(full_name)) # 15
print(len(first_name)>len(last_name)) # True

### Unpacking the characters of a string
language='Python'
a,b,c,d,e,f=language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing the characters in string by index
language='Python'
first_letter=language[0]
print(first_letter)
second_letter=language[1]
print(second_letter)
last_index=len(language)-1
last_letter=language[last_index]
print(last_letter)

# If we want ot start from right end we can use negative indexing. -1 is the last index
language='Python'
last_letter=language[-1]
print(last_letter)

# Slicing
language='Python'
first_three=language[0:3]
print(first_three)
last_three=language[-3:]
print(last_three)

# Skipping character while splitting Python strings
language='Python'
pto=language[0:6:2]
print(pto)

# Escape sequence
print('I hope every on enjoying python challenge?\tDo you?')
print('Day 1\t3\t5')
print('Day 1\t2\t5')
print('Day 1\t3\t5')
print('Day 1\t4\t5')
print('This is a back slash symbol(\\)') # To write back slash.

# String methods
# capitalize(): converts the first character of the string to capital letter.

challenge='thirty days of python'
print(challenge.capitalize()) # Thirty days of Python

# count() : returns occurence of substring in string, count(substring,start=...,end=...)
challenge='thirty days of python'
print(challenge.count('y'))
print(challenge.count('y',7,14))
print(challenge.count('th'))

# endsWith() : checks if a string ends with a specified ending
challenge='thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith("tion"))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes size argument
challenge='thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): Returns the index of first occurrence of substring
challenge='thirty days of python'
print(challenge.find('o'))
print(challenge.find('y'))
print(challenge.find('th'))

#format(): formats string into nicer output
first_name='Prashant'
last_name='Pandey'
desg='AI Engineer'
country='India'

employee_details='Hi, I am {} {}, I am from {}, My Designation is {}'.format(first_name,last_name,country,desg)
print(employee_details)

# area of circle
radius=10
pi=3.14
area=pi*radius*radius
area_of_circle='The area of circle with radius : {} is {}'.format(radius,area)
print(area_of_circle)

# index(): Returns the index of substring
challenge='thiry days of python'
print(challenge.index('o'))
print(challenge.index('th'))

# isalnum(): Checks alphanumeric character
challenge='thirty days of python'
print(challenge.isalnum())
print('30daysofPython'.isalnum())
print("30 days of python".isalnum())
print("ThirtyDaysOfPython".isalnum())

# isalpha(): Checks if all characters are alphabetic
print("thirty days of python".isalpha())
print('30daysofpython'.isalpha())
print('thirtydaysofpython'.isalpha())
