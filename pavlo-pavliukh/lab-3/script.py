# Умови

x = 2
print(x == 2)
print(x == 3)

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


name, age = "Pavlo", 19

if name == "Pavlo" and age == 19:
    print("My name is Pavlo, and my age also 19 years old.")
if name == "Pavlo" or name == "Pablo":
    print("My name is either Pavlo or Pablo.")


# == і is
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)


print(not False)
print(not False == False)


# Цикли
primes = [2, 3, 5, 7]
# цикл for
for prime in primes:
    print(prime)

# функція range
for x in range(3):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)


# цикл while
count = 0
while count < 5:
    print(count)
    count += 1

# break і continue
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(5):
    if x % 2 == 0:
        continue
    print(x)
