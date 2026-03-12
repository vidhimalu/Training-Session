mylist=["prashant","sachin","rohit","virat",77,88,99,100,"sandeep",60.52]
print(mylist)
print(type(mylist)) 
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[5:])
print(mylist[::2])
print(mylist[::-1])
print(mylist[1:8:2])
print(mylist[1:8:3])


mylist = ["prashant", "sachin", "rohit", "virat", 77, 88, 99, 100, "sandeep", 60.52]

mylist.append('Vidhi')
mylist.append("Vidhi_malu")
print(mylist)
mylist.insert(2, "malu")
print(mylist)
mylist.remove("malu")
print(mylist)
newList = mylist.copy()
print(newList)    


crazylist =[['prashant', 'sachin', 'rohit'], [77, 88, 99], [100, 'sandeep', 60.52]]
print(crazylist)
print(crazylist[0][0])
print(crazylist[0][1])
print(crazylist[0][2])
print(crazylist[1][0])
print(crazylist[1][1])
print(crazylist[1][2])
print(crazylist[2][0])
print(crazylist[2][1])
print(crazylist[2][2])



list1=["Vidhi","Malu"]
print(list1*2)

list2=[50,25.50]
print(list1+list2)

list1.remove("Malu")
print(list1)

list1.clear()
print(list1)

name="prashant"
print(name)
myname=list(name)
print(myname)



#sorting example
mylist1=[5,2,9,1,5,6]
mylist1.sort()
print(mylist1)

mylist1.sort(reverse=True)
print(mylist1)



#id function is used to return the address of the variable.

math = 10
print(id(math))
math = 20
print(id(math))


#id comes out the same because of the concept of interning in Python, where small integers are cached and reused to 
# optimize memory usage. When you assign the value 10 to both `physics` and `physics1`, 
# they point to the same memory location, hence the same id is returned.
physics = 10
physics1=10
print(id(physics))
print(id(physics1))

#aliasing means assigning one variable reference to another variable 

mylist=[44,22,77,0,9,88]
mylist1=mylist
print(id(mylist))
print(id(mylist1))


name='Vidhi'
print('Z' in name)
print('I' in name)


print('Z' not in name)


for i in range(1,6):
   print(i)

for i in range(6):
   print(i)

 for i in range(1,10,3):{

    print(i)}

for i in range(10,0,-1):{
    print(i) }


for num in range(2, 11):
     for i in range(1, 11):
        print(f"{num}x{i}={num*i}", end="\t")
     print()

#WAP a program to accept any digit and check that positive ,negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
if num < 0:
    print("The number is negative.")
if num == 0:
    print("The number is zero.")


#WAP to accept days and check the working days and weekends
day = input("Enter a day of the week: ").lower()
if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print(f"{day.capitalize()} is a working day.")
else:
    print(f"{day.capitalize()} is a weekend day.")



#WAP to accept three paper marks and calculate total marks , percentage and if percentage is greater than eqaul to 60 then print pass otherwise print fail
marks1 = float(input("Enter marks for paper 1: "))
marks2 = float(input("Enter marks for paper 2: "))
marks3 = float(input("Enter marks for paper 3: "))

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

if percentage >= 60:
    print("The student has passed.")
else:
    print("The student has failed.")

print(f"Total marks: {total}")
print(f"Percentage: {percentage:.2f}%")


#WAP to accept five diffrent values in 5 diffrent variables and check maximum value and print by using "Simple if statement"
val1 = float(input("Enter value 1: "))
val2 = float(input("Enter value 2: "))
val3 = float(input("Enter value 3: "))
val4 = float(input("Enter value 4: "))
val5 = float(input("Enter value 5: "))

max_val = val1
if val2 > max_val:
    max_val = val2
if val3 > max_val:
    max_val = val3
if val4 > max_val:
    max_val = val4
if val5 > max_val:
    max_val = val5

print(f"The maximum value is: {max_val}")
