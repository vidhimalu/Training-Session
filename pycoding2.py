#Program to take input from user for 2 numbers and then replacing first value with sencond value and second value with first value and then print the values of both the numbers after swapping.

val1 = input("Enter the First Value: ")
val2 = input("Enter the Second Value: ")

print("Before swapping:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")

# Swapping the values
val1, val2 = val2, val1

print("After swapping:")
print(f"First Value: {val1}")
# Swapping the values using temp variable
temp = val1
val1 = val2
val2 = temp

print("After swapping:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")


# Swapping without using a temporary variable
val1 = int(val1) + int(val2)
val2 = int(val1) - int(val2)
val1 = int(val1) - int(val2)

print("After swapping without temp variable:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")


#WAP to enter height of user in feet and convert it into inch and centimeter
height_feet = float(input("Enter height in feet: "))

height_inches = height_feet * 12
height_cm = height_feet * 30.48

print(f"Height in feet: {height_feet}")
print(f"Height in inches: {height_inches}")
print(f"Height in centimeters: {height_cm}")


#WAP to Reverse a 3 digit number with loop
num = int(input("eEnter a  number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(f"Reversed number with loop : {rev}")

#WAP to Reverse a 3 digit number without loop
num = 1234567
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
num = num // 10
f = num % 10
num = num // 10
g = num % 10
rev = a * 1000000 + b * 100000 + c * 10000 + d * 1000 + e * 100 + f * 10 + g
print(f"Reversed number using sir's logic (without loop): {rev}")

num =123
a=num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
rev = a * 100 + b * 10 + c
print(f"Reversed number: {rev}")
