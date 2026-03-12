# Take input of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# # Find the greatest number
greatest = max(num1, num2, num3)

# # Print the result
print(f"The greatest number is: {greatest}")


# # Find the greatest number using if-else
if num1 >= num2 and num1 >= num3:
     greatest = num1
 elif num2 >= num1 and num2 >= num3:
     greatest = num2
 else:
     greatest = num3

# # Print the result
 print(f"The greatest number is: {greatest}")


 percentage = float(input("Enter percentage: "))

 if percentage >= 90:
     print("Grade: A")
 elif percentage >= 80:
     print("Grade: B")
 elif percentage >= 60:
     print("Grade: C")
 else:
     print("Grade: Fail")


mydict = {
    "name":"Vidhi",
    "profession":"Student",
    "age":20
   
}
print(mydict)
print(type(mydict))


mydict1 = {
    101:"Vidhi",
    102:"Rahul",
    103:"Suresh",
    "104":"Ramesh",
    "105":"Priya",
    101:"Rohit",
    102:"Amit"
}
print(mydict1)
mydict1[102]="peter"
print(mydict1)

for x in mydict:
    print(x)

 for x in mydict.values():
    print(x)

for x, y in mydict.items():
    print(x, y)

mydict1["mobile_no"]= 9511233302
print(mydict1)

mydict1.pop("104")
print(mydict1)

name = "VidhiMalu"
print(name[0])
print(name[1])
print(name[-1])
print(name[0:6])
print(name[6:])
print(name[:6])
print(name[::2])
print(name[1:8:2])

s="help4code is a best platform for practicing python programming"
print(s.find("help4code"))
print(s.find("python"))
print(s.find("programming"))
print(s.find("Vidhi"))


ss="Python is a high level programming language"
print(ss.lower())
print(ss.upper())
print(ss.capitalize())
print(ss.swapcase())
print(ss.title())

print('Subject marks')
phy=50
chem=60
math=70
print(f"Physics: {phy}")
print(f"Chemistry: {chem}")
print(f"Mathematics: {math}")
print(f"Total Marks: {phy + chem + math}")
print("Roll No=", "15".zfill(4))


print('VidhiMalu'.isalnum())
print('VidhiMalu'.isalpha())
print('12345'.isdigit())
print('Hello World'.isupper())
print('Hello World'.islower())
print('Hello World'.istitle())
print(' '.isspace())
print(''.istitle())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))

#BODMAS
a=50
b=30 
c=30
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)

x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x !=z)

name = "vidhi"
for i in name:
    print(i)

name="Vidhi"
data=['a','e','i','o','u']
vowels=0
con=0
for i in name:
    if i in data:
        vowels+=1
    else:
        con+=1
print("vowels=",vowels)
print("consonent=",con)
