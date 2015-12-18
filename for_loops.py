from __future__ import print_function

#1
for row in range(10):
    print("*",end=" ")
    
print('\n')
print('2')

#2
for row in range(10):
    print("*",end=" ")
print()
for row in range(5):
    print("*",end=" ")
print()
for row in range(20):
    print("*",end=" ")
print()
print('\n')
print('3')

#3
for row in range(10):
    for column in range(10):
        print("*",end=" ")
 
    print()
print()
print('\n')
print('4')

#4
for i in range(10):
    for j in range(5):
        print("*", end=" ")
    print()
    
print('\n')
print('5')

#5
for i in range(5):
    for j in range(20):
        print("*", end=" ")
    print()

print('\n')
print('6')

#6
for row in range(10):
    for column in range(10):
        print(column,end=" ")
    print()
print('\n')
print('7')

#7
for row in range(10):
    for column in range(10):
        print(row,end=" ")
    print()
print('\n')
print('8')

#8
for row in range(10):
    for column in range(row+1):
        print (column,end=" ")
    print()
print('\n')
print('9')
#9
for row in range(10):
 
    for j in range(row):
        print (" ",end=" ")
 
    for j in range(10-row):
        print (j,end=" ")
 
    print()
print('\n')
print('10')

#10
for i in range(1,10):
    for j in range(1,10):
        if i*j < 10:
            print (" ",end="")
 
        print (i*j,end=" " )
    print()
print('\n')
print('11')
#11a
for i in range(10):
    for j in range(10-i):
        print (" ",end=" ")
    
    for j in range(1,i+1):
        print (j,end=" ")
    
    for j in range(i-1,0,-1):
        print (j,end=" ")
    
    print()
print('\n')
print('11_1')

for i in range(10):
    for j in range(10-i):
        print (" ",end=" ")
    for j in range(1,i+1):
        print (j,end=" ")
    for j in range(i-1,0,-1):
        print (j,end=" ")
    print()
 
for i in range(10):
    for j in range(i+2):
        print (" ",end=" ")
    for j in range(1,9-i):
        print (j,end=" ")
    for j in range(7-i,0,-1):
        print (j,end=" ")
    print()
