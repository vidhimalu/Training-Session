##function
def msg(): #function definition
print("Hello, World!") #function body
msg() #function call

def add(a,b):
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a + b
print("Sum is:", c)

def add():
     n1 = int(input("Enter first number: "))
     n2 = int(input("Enter second number: "))
     sum = n1 + n2
     sub = n1 - n2
     mul = n1 * n2
     div = n1 / n2
     return sum, sub, mul, div
 result = add()
 print(result)


## 1.positional argument
 def personal_info(fname, lname):
     print("Firstname:", fname)
     print("Lastname:", lname)
 personal_info("Vidhi", "Malu") #positional argument

## 2.keyword argument
 def personal_info(fname, lname):
     print("Firstname:", fname)
     print("Lastname:", lname)
 fname = "Vidhi"
 lname = "Malu"
 personal_info(fname, lname) #keyword argument

 def cityname(city="Banglore"):
     print(city)
 cityname("Nagpur") #positional argument
 cityname("Pune")
 cityname()

#variable length argument
 def studentnames(*name):
     print(name)
studentnames("Virat","Rohit","Bumrah")

mylist=[5,2,9,7,5,6]
def searchelement(target):
    for i in range(len(mylist)):
        print(mylist[i])
searchelement(7)

 mylist=[5,2,9,7,5,6]
 def searchelement(target):
     for i in range(len(mylist)):
         if(target==mylist[i]):
             print("Element found at index:", i)
             break
        print(mylist[i])
searchelement(7)

mylist=[5,2,9,7,5,6]
def searchelement(target):
    for i in range(len(mylist)):
        if(target==mylist[i]):
             return i
result=searchelement(10)
if result !=-1:
  print("Element found at index:", result)
else:  
    print("Element not found")
