def sumN (n):
    if n==1:
        return 1
    else:
        return n+sumN(n-1)

n=int(input('Enter number (n):'))
print('The sum of first ',n, 'numbers is:', sumN(n))

