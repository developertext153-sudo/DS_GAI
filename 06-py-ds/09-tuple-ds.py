# tuple always start with ()
t=()

print(t)
print(type(t))

# Creating tuple datastructure t1
t1=(10,20,30,40,50)
print(t1)

print(len(t1))

# Printing the occurance of 10 in t1 datastructure
print(t1.count(10))

# Printing the occurance of 10 in t1 datastructure
print(t1.count(40))

# Printing the index of 10 in t1 datastructure
print(t1.index(10))

l5=['a','b','c','d']
print(l5)

print(l5)

l5[1]=10
print(l5)

t2=(100,3.4,'nit',True,1+2j,[1,2,3],[5,6,7])
print(t)
print(t1)
print(t2)

# Printing the t element individually
print(t1[0])

# Replacing the element in tuple
# t1[0]=1000 # Tuple does not allow modification
# tuple datastructure is immutable

icici=(12345,'xyz345',332000,98765)
print(icici)

t3=t2*3
print(t3)

# Slicing in tuple
# Printing all the element of tuple
print(t2[:])
# Printing start from first index to (7-1) i.e 6 index
print(t2[:7])
# Printing start from 2nd index to last index
print(t2[2:])
# Printing start from 0th index to (10-1) index and jump to 2 step
print(t2[0:10:2])

# Remove the element from tuple
# t2.remove(100) # tuple has no attribute 'remove'

# Adding the element in tuple
# t2.add(30) # tuple has no attribute 'add'
# print(t2)

t4=(10,20,30,40,40)
print(t4)
# Printing the index of 40
print(t4.index(40))
# Printing the index of nit in t3
print(t3.index('nit'))

# Looping in tuple
for i in t4:
    print(i)
# enumerate in tuple
for i in enumerate(t4):
    print(i)