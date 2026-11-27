l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)

print(l)

# Creating new list from existing list and copying the list element
l1=l.copy()
print(l)
print(l1)

#Print length of l,l1 list
print(len(l))
print(len(l1))

for i in l:
    print(i)

l1.append([1,2,3,'hi'])
print(l1)

# Removing the element from the list
l1.remove(40)
print(l1)

print(l1[3])

# Removing the element by index wise
# If we don't pass any argument by default it will take last
l1.pop()
print(l1)

l1.pop()
print(l1)

l1.pop()
print(l1)

l1.append(20)
l1.append(30)
print(l1)

l1.pop(-1)
print(l)
print(l1)

# Insert the element at particular index in the list
#l1.insert(30) # TypeError : insert expected 2 arguments, got 1
l1.insert(2,30)
print(l1)

l1.insert(1,15)
print(l1)

l2=[]
print(l2)

l2.extend(l1)
print(l2)

# Printing all the list 1,l1,l2
print(l)
print(l1)
print(l2)

# Printing length of all the list l,l1,l2
print(len(l))
print(len(l1))
print(len(l2))

# Printing the index of element in the list
print(l2.index(20))

l3=[]
l3.extend(l2)
print(l3)

l3.append(30)
print(l3)
print(l3.count(30))

l3.remove(30)
print(l3)
l3.clear()

print(l3)

l4=l2.copy()
l4.append(25)
print(l4)

# Sort the list in ascending order
l4.sort()
print(l4)

# Sort the list in descending order
l4.sort(reverse=True)
print(l4)

l5=[2,3,1,5,4]
print(l5)

# Reversing the list right to left
l5.reverse()
print(l5)

# Sorting the list in ascending order
l5.sort()
print(l5) 

# Sorting the list in descending order
l5.sort(reverse=True)
print(l5)