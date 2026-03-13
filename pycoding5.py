i=1
while i<=5:
    print(i)
    i=i+1

username =''
password=''
while username != "admin" and password != "hello":
      username = input("Enter username:")
      password = input("Enter password:")

#sum of first n numbers

n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i

    i=i+1
print("the sum of first",n,"number is:",sum)

name ="Vidhi"
newname =" "
for i in name:
    if i not in newname:
    newname +=i
print(name)
print(newname)
print(name[::-1])

mycart=[10,20,200,300,800,60,700]
for i in mycart:
 if i>400:
  print("This is my purchased cart item")
  continue
 print(i) 

name ="Vidhi"
print(name[::-1])
if name == name[::-1]:
    print("palindrome string")
else:
   print("not palindrome")


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range (1,n+1):
        print(n+1-i,end=" ")
    print()
  
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range (1,n+2-i):
        print("*",end=" ")
    print()


for i in range(1,5):
  i=3
    if i==3:
        continue
    print(i)


for i,j in zip(range(1,6), range(5,0,-1)):
       if i == 3 and j==3:
          continue
       print(i, " ", j)


 for i in range(1,5):
     if i==3:
         break
     print(i)


 for i in range(1,5):
     if i==3:
         continue
    print(i)


 for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
         continue
     print(i," ",j)

#palindrome
 name=input("enter a name:")
 newname=name[::-1]
 if name==newname:
     print("palindrome")
 else:
    print("not a palindrome")


# #anagram - check if both words have same and equal letters like listen=silent
 a=input("enter word 1:")
 b=input("enter word 2:")
# #do by sorting


#adding key value pair to a dictionary
 my_dict = {}
 my_dict['name'] = 'Vidhi'
 my_dict['age'] = 20
 print("After adding key-value pairs:", my_dict)


#remove a key value pair 

 my_dict = {}
my_dict['name'] = 'Vidhi'
 my_dict['age'] = 20
 print("After adding key-value pairs:", my_dict)

 for i in range(1, 4):
     for j in range(1, 4):
         print(i, end=" ")
     print()
