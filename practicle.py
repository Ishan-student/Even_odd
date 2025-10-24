#Details
print('Ishan Maurya')
print('PU02325EUGBTAR026')

#Even Odd
print('Even Odd')
n=int(input('Enter the number'))

for i in range(2,n//2):
    if n%2==0:
        print('Even Number')
        break
else:
    print('Odd number')
    
        
#Reverse number
print('Reverse number')
n=int(input('Enter the number'))
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print(s)

#List and tuple operation
print('List and Tuple operation')
l=[3,6,5,1,5]
print(l)
l1=eval(input('Enter the list'))
print(l1)
l2=l1+l
print(l2)
for i in range(len(l1)):
    a=l2.pop(0)
print(l2)
i=int(input('Enter index to access'))
print(l2[i])

t=(3,1,2)
print(t)
try:
    t[1]=4
except TypeError:
    print('Tuple is immutable')

print(t[1])

#Numpy Array operations
print('Numpy Array operations')
import numpy as np
arr=np.array([5,4,2])

arr2=np.array([[5,2,1]
              [4,5,3]])
arr3=arr[3]
arr4=arr2[1,2]

arr5=arr+arr2[1]
arr6=arr*arr2[0]

#Dictionary Functionality
print('Dictionary Functionality')
d={'Sujal':11,'Hrideysh':17,'Ishan':15}
print(d)

d['Aaditya']=10
d['Aadharsh']=12
print(d)

d['Aaditya']=11
print(d)

for i in d:
    print(i,':',d[i])
