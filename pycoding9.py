# WAP to perfor arithmetic operation using functional programming approach
# Function helps us to achieve modularity approach 
 import sys 
 def addition(num1, num2):
      print("Addition=", num1+num2)
 def substraction(num1, num2):
      print("Substraction=", num1-num2)
 def multiplication(num1, num2):
      print("Multiplication=", num1*num2)
 def division(num1, num2):
     print("Division=", num1 / num2)

 while True:
     print("1. Addition")
    print("2. Substraction")
     print("3. Multipliction")
     print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice from above options:"))
     if choice == 5:
          sys.exit()
     val1   = int(input("Enter First Value :"))
     val2   = int(input("Enter Second Value :"))
    if choice == 1:
          addition(val1, val2)
     elif choice ==2:
          substraction(val1, val2)
     elif choice ==3:
         multiplication(val1, val2)
     elif choice ==4:
          division(val1, val2)
     else:
          sys.exit()

#nested function

 def outerFunction():
     print("this is my outer function:")
     def innerFunction():
         print("inner Function")
    innerFunction()
 outerFunction()


## WAP to count the word
 name ="Vidhi is a good programer"
 count =1
 for i in name:
      if i == " ":
           count +=1
      else:
           continue 
 print("Total word count =", count)

#tuple questions

#Q1. 
 init_tuple =()
 print(init_tuple.__len__())

# #Q2
 init_tuple_a = 'a', 'b'
 init_tuple_b=('a','b')# bracket not mandatory
 print(init_tuple_a == init_tuple_b)

# Q3
 init_tuple_a='1','2'
 init_tuple_b=('3','4')
 print(init_tuple_a + init_tuple_b)

# Q4

 lst = [1,2,3]
 init_tuple = ('Python',) * (len(lst) - lst[::-1][0])
 print(init_tuple)

# Q5
 init_tuple =('Python') * 3
 print(type(init_tuple))

# Q6
 init_t =(1,) * 3 
 init_t [1] = 2
 print(init_t)

# #Q7
 init_tuple =((1,2)) * 7
 print(len(init_tuple[3:8]))


#string questions
# #Q1
 s=""
 s1=s.replace("difficult", "easy")
 print(s1)
 s="abababababababab"
 s1=s.replace("a","b")
 print(s1)

# Q2
 city=input("Enter your city name:")
 scity=city.strip()
 if scity=='Hyderabad':
    print("Hello Hyderabadi..Adab")
 elif scity=='Chennai':
     print("Hello Madrasi...Vanakkam")
 elif scity=="Bangalore":
     print("Hello Kannadiga...Shubhodaya")
 else:
     print("your entered city is invalid")


# list comprehension

s=[i*i for i in range(1,11)]
print(s)

val=[2**i for i in range(1,6)]
print(val)

val2=[i for i in s if i%2==0]
print(val2)

#Dictionary Comprehension
squares={x:x*x for x in range(1,6)}
print(squares)

doubles={x:2*x for x in range(1,6)}
print(doubles)
