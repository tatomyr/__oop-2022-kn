# Conditions
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#Else
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#And
  a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#Or
  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  

#Loops
#"for" loop
  primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
#"while" loops
        # Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
#"break" and "continue"
        # Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

        # Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
        # Check if x is even
    if x % 2 == 0:
        continue
    print(x)