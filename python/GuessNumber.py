from random import*
print('Try to guess the number (1 to 100)')
n=randint(1,100)
userTry=0
attempts=0
while userTry!=n:
    userTry=int(input('Your guess:'))
    attempts=attempts+1
    if userTry<n:
        print('No, number is bigger!')
    if userTry>n:
        print('No, number is smaller!')

print('Congratulations, you needed',attempts,'attempts!')
