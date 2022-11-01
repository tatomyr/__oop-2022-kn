# Conditions
print("---------- Conditions ----------")

x = 2
print(x == 2)  # prints True
print(x == 3)  # prints False

if x == 2:
    print("x equals 2.")
else:
    print("x does not equal to 2.")


first_statement, second_statement = False, True
if first_statement is True:
    print("First statement is True.")
elif second_statement is True:
    print("Second statement is True.")
else:
    print("Each statements is not True.")


name, age = "Andrii", 19

if name == "Andrii" and age == 19:
    print("My name is Andrii, and my age also 19 years old.")
if name == "Andrii" or name == "Andrew":
    print("My name is either Andrii or Andrew.")


# '==' and 'is' are not the same
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # prints True
print(x is y)  # prints False


# 'not' inverts boolean expression
print(not False)  # prints True
print(not False == False)  # prints False


# Loops
print("\n---------- Loops ----------")

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# range function arguments: first - start, second - end, third - step
for x in range(3):  # prints 0, 1, 2
    print(x)

for x in range(3, 6):  # prints 3, 4, 5
    print(x)

for x in range(3, 8, 2):  # prints 3, 5, 7
    print(x)


# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break and continue
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # stops the program if count is bigger or equal to 5

for x in range(5):
    if x % 2 == 0:  # prints only odd numbers - 1, 3
        continue
    print(x)