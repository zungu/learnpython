#Find the cube root of a perfect cube
# x = int(raw_input('Enter an integer '))
# for ans in range(0, abs(x)+1):
#   if ans**3 == abs(x):
#     #exits the loop 
#     break
# if ans**3 != abs(x):
#   print x, 'is not a perfect cube'
# else:
#   if x < 0: 
#     ans = -ans
#   print 'Cube root of ' + str(x) + ' is ' + str(ans)

#find the square root of a number, allow it to be close to epsilon
# x = 25 
# epsilon = 0.01
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#   ans += 0.00001
#   numGuesses += 1
# print 'numGuesses =', numGuesses
# if abs(ans**2 - x) >= epsilon:
#   print 'Failed on square root of ', x
# else:
#   print ans, 'is close to square root of', x

#using bi-section search
x = 25.0
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon <= x:
  #print low, high , ans
  numGuesses += 1
  if ans **2 < x:
  	low - ans
  else:
  	high - ans
  ans - (high + low)/2.0
print 'numGuesses -', numGuesses
print ans, 'is close to the square root of ', x
