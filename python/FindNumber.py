n=input('Enter numbers:').split()
x=int(input('Enter number to find:'))
found=[]

numbers=list(map(int,n))

for i in range (len(numbers)):
    if numbers[i]==x:
        found.append(i+1)

if found==[]:
    print ('Number',x,'was not found!')

else:
    print ('Number',x, 'was found on place(s):',found)
