math = 40
pi = 3.14
name = 'Vidhi Malu'
print(type(math))
print(type(pi))
print(type(name))


print(2+2)
print("2"+"2")

#try:
val1 = int(input("Enter the First Value:"))
val2 = int(input("Enter the Second Value:"))
print(val1+val2)

except ValueError:
print("Error: Please enter valid integers")

#typcasting values for int 
print("typcasting values for int")
print(int(3.14))
print(int(True))
print(int(False))
print(int("4"))


#typcasting values for float
print("typcasting values for float")
print(float(3))
print(float(True))
print(float(False))
print(float(3.14))
print(float("3"))

#typcasting values for complex
print("typcasting values for complex")
print(complex(3))
print(complex(3.14))
print(complex("3"))
print(complex("3+4j"))
print(complex(True))
print(complex(False))
print(complex(True,False))
print(complex(5,-3))


#typcasting values for bool
print("typcasting values for bool")
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(0.0))
print(bool(0.1))
print(bool(""))
print(bool("Hello"))
print(bool(1+2j))


#WAP for simple interest 
print("WAP for simple interest")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Simple Interest: {simple_interest}")
print(f"Total Amount: {total_amount}")


#WAP a program to maintain temperature in centigrade and fahrenheit
print("\n#WAP a program to maintain temperature in centigrade and fahrenheit")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
  
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")
temp_f = float(input("Enter temperature in Fahrenheit: "))
temp_c = fahrenheit_to_celsius(temp_f)

print(f"{temp_f}°F is equal to {temp_c}°C")
