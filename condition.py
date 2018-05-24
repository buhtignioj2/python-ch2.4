# if ~ else
a = 10
if a > 5:
    print('big')
else:
    pass

# if ~ elif ~ else
n = -2
if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0')

order = 'spam'
if order == 'spam':
    price = 1000
elif order == 'egg':
    price = 500
elif order == 'spagetti':
    price = 2000

print(price)

# Condition Expression(tenary operator, 삼항연산자)
# in Java, s = a > 5 ? 'big' : 'small'
print('big' if a > 5 else 'small')
