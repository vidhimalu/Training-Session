def count_special_and_spaces(message): # Function to count special characters and spaces in the message
     count = 0 # Initialize count to 0
     for ch in message:
# If character is NOT a letter or digit → count it
         if not ch.isalnum(): # Check if the character is not alphanumeric (i.e., not a letter or digit)
             count += 1 # Increment count for each special character or space 
    return count # Return the final count of special characters and spaces
## Input
 message = input() # Read a message from the user
## Output
 print(count_special_and_spaces(message)) # Call the function and print the result, which is the count of special characters and spaces in the input message

 import re
 var = 'gasgg54@#vscs!s'
 count=0
 for i in var:
     z= re.findall('[a-z,0-9]',i)
     z =ord(i)
     print(z)
     if z>=97 and z<=122:
           continue
     elif z>=48 and z<=57:
          continue
     else:
        count+=1
 print(count)

 import re
 var = 'gasgg54@#vscsd!s*'
 count=0
 for i in var:
     z =ord(i)
     if z>=97 and z<=122:
          continue
     elif z>=48 and z<=57:
          continue
     else:
        count+=1
 print(count)

#find the intersection of three arrays
 a = [1,2,3]
 b = [2,3,4]
 c = [3,4,5]
 result = []
 for i in a:
     if i in b and i in c:
         result.append(i)
 print(result)

 def moveZeroes(nums):
     j = 0  # position to place next non-zero
    for i in range(len(nums)):
         if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
     return nums
 print(moveZeroes([0,1,0,3,12])) # Output: [1, 3, 12, 0, 0]

# find second largest number in the array
 a = [4,2,6,1,5]
 a.sort()
 print(a)
 print(a[-2])

#finding the total distance between adjacent items in list of 5 numbers
a = [10,11,7,12,14]
total_distance = 0
for i in range(len(a) - 1):
    total_distance += abs(a[i+1] - a[i])
print(total_distance)
