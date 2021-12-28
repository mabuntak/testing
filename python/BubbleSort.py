def BubbleSort(NumberList):
    for i in range (len(NumberList)-1):
        for j in range ((len(NumberList)-1)-i):
            if NumberList[j] > NumberList[j+1]:
                NumberList[j], NumberList[j+1]=NumberList[j+1], NumberList[j]
    print ('Sorted:', NumberList)

NumberList=[]
n=int(input('How many numbers do you want to enter?'))
for x in range (n):
    a=int(input('Enter number:'))
    NumberList.append(a)    

BubbleSort(NumberList)
