l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)

l1=l.copy()

l2=[]
l2.extend(l1)

print(l)
print(l1)
print(l2)

# String List slicing (datatype)
name='prashant'
print(name)

print(name[0])
print(name[1])
print(name[2])

for i in name:
 print(i)

# List Slicing 
# : entire element
# 2:10 --> Print the element from 2nd index to n-1 (10-1) 9th index
# always right index should be n-1 formula is applicable
# :10 --> Print the element from starting index to n-1
# 3: --> Print the element from 3rd index to last index

# Advanced Slicing 1:100:10
# 1:100:10 --> Print start index(1st) & last index(n-1) & step index(10)
# every 10th step count


# Printing the element from starting index to the last index
print(l[0:len(l)-1])

# Printing the element from 3rd index to the last index
# Last index(n-1)
print(l[3:])

# Print the element from from start index to the 2nd index 
print(l[:3])

l=[10,20,30,40,50,60,70,80,90,100]
print(l[0:20:5])

print(l[3:10:3])

print(l[::-1])

print(l[::-2])

print(l[::-3])

l[-1]='prashant'
print(l)

# Print the nested slicing
print(l[-1][0])
print(l[-1][1])
print(l[-1][2])
print(l[-1][3])
print(l[-1][4])
print(l[-1][5])
print(l[-1][6])
print(l[-1][7])

# Concat the List
l1=[10,20,30]
l2=[40,50,60]
l3=l1+l2

print(f'L1 element = {l1} and the size L1 is {len(l1)}')
print(f'L2 element ={l2} and the size L2 is {len(l2)}')
print(f'L3 element ={l3} and size {len(l3)}')

# List im mutable
l4=[]
l4=l3.copy()
print(l4)

print(20 in l4)

# Enumerate
print(l4)

for i in l4:
 print(i)

# with index
for i in enumerate(l4):
 print(i)

l5=[0,2,3,4,5]

# all(list) it returns True if all elements are True else false
print(all(l5))

# any(list)  it returns True if atleast one element is True else false
print(any(l5))

l6=[0,0,0]
print(all(l6))
print(any(l6))

# List data structure is completed
