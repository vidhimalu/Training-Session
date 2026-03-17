fruit_list1 =["apple", "Berry","cherry", "papaya"]
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = "Guava"
fruit_list3[1] = "Kiwi"
sum =0
for ls in (fruit_list1, fruit_list2, fruit_list3):
     print(ls)
     if ls[0] == "Guava":
         sum += 1
     if ls[1] == "Kiwi":
       sum += 20
print("Total sum:", sum)

 def f(i,values=[]):
     values.append(i)
     print (values)
 f(1)
 f(2)
 f(3)


def func(value,values):
     var =1
     values[0]=44
 t=3
 v =[1,2,3]
 func(t,v)
 print(t,v[0])
 dict ={'c':97,'a':96,'b':98}
 for _ in sorted(dict):
     print(dict[_])

 fruit ={}
 def addone(index):
     if index in fruit:
         fruit[index] += 1
     else:
         fruit[index] = 1
 addone("apple")
 addone("banana")
 addone("apple")
 print(len(fruit))

def productExceptSelf(nums):
    n = len(nums) # Get the length of the input array
    answer = [1] * n # Initialize the answer array with 1s
    # Step 1: Left product
    left = 1 # Initialize left product to 1
    for i in range(n): # Iterate through the input array
        answer[i] = left # Update the answer array with the left product
        left *= nums[i] # Update the left product by multiplying with the current element
    # Step 2: Right product
    right = 1 # Initialize right product to 1
    for i in range(n - 1, -1, -1): # Iterate through the input array in reverse
        answer[i] *= right # Update the answer array by multiplying with the right product
        right *= nums[i] # Update the right product by multiplying with the current element
    return answer
print(productExceptSelf([1,2,3,4])) # Output: [24, 12, 8, 6]
