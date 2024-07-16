"""
Python Code Challenges: Loops

"""

"""
1. Divisible By Ten
Coding question
Questions
Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.
"""

#Write your function here
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count


print(" 1. Divisible by ten")
print(divisible_by_ten([20, 25, 30, 35, 40]))


"""
  2. Greetings

  Create a function named add_greetings() which takes a list of strings 
  named names as a parameter.

  In the function, create an empty list that will contain each greeting. 
  Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

  Return the new list containing the greetings.
"""

def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

print(" 2. Greetings")
print(add_greetings(["Owen", "Max", "Sophie"]))

"""
  3. Delete Starting Even Numbers

  1.Define our function to accept a single input parameter my_list which is a list of numbers
  2.Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
  3.Within the loop, if the first number in the list is even, then remove the first number of the list
  4.Once we hit an odd number or we run out of numbers, return the modified list


  Write a function called delete_starting_evens() that has a parameter named my_list.

  The function should remove elements from the front of my_list until the front 
  of the list is not even. The function should then return my_list.

  For example if my_list started as [4, 8, 10, 11, 12, 15], 
  then delete_starting_evens(my_list) should return [11, 12, 15].

  Make sure your function works even if every element in the list is even!
"""

#Write your function here
def delete_starting_evens(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0:
    my_list.pop(0)
  return my_list
    


print("3. Delete Starting Even Numbers")
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

"""
  4. Odd Indices

  Create a function named odd_indices() that has one parameter named my_list.

  The function should create a new empty list and add every element from my_list 
  that has an odd index. The function should then return this new list.

  For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

  Hint
  There are a few ways to do this. range(1, len(my_list), 2) 
  will create a list of the indices you're interested in. So you could loop through that list like this:

"""

#Write your function here
def odd_indices(my_list):
  new_list = []
  for index in range(1,len(my_list),2):
    new_list.append(my_list[index])
  return new_list

print(" 4. Odd Indices")
print(odd_indices([4, 3, 7, 10, 11, -2]))

"""
  5. Exponents

  Create a function named exponents() that takes two lists as parameters named bases and powers. 
  Return a new list containing every number in bases raised to every number in powers.

  Hint
  Use nested for loops. The outer for loop should loop through all of the bases and the inner for loop should loop through all of the powers.
  Remember a ** b is a to the power of b
"""

#Write your function here
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list



print(" 5. Exponents")
print(exponents([2, 3, 4], [1, 2, 3]))

"""
        Python Code Challenges: Loops (Advanced)
"""

"""
  1. Larger Sum

  Create a function named larger_sum() that takes two lists of numbers 
  as parameters named lst1 and lst2.

  The function should return the list whose elements sum to the greater number. 
  If the sum of the elements of each list are equal, return lst1.
"""

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num1 in lst1:
    sum1 += num1

  for num2 in lst2:
    sum2 += num2

  if sum1 >= sum2:
    return lst1
  else:
    return lst2
  

# Solution #2 using sum()
def larger_sum_2(lst1, lst2):
  sum1 = 0
  sum2 = 0

  sum1 = sum(lst1)
  sum2 = sum(lst2)

  if sum1 >= sum2:
    return lst1
  else:
    return lst2
  

print(" 1. Larger Sum")
print(larger_sum([1, 9, 5], [2, 3, 7]))
print(larger_sum_2([1, 9, 5], [2, 3, 7]))

"""
  2. Over 9000

  Create a function named over_nine_thousand() that takes a list 
  of numbers named lst as a parameter.

  The function should sum the elements of the list until 
  the sum is greater than 9000. When this happens, the function should return the sum. 
  If the sum of all of the elements is never greater than 9000, 
  the function should return total sum of all the elements. If the list is empty, 
  the function should return 0.

  For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
"""

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if sum > 9000:
      break
  return sum
    


print(" 2. Over 9000")
print(over_nine_thousand([8000, 900, 120, 5000]))

"""
  3. Max Num

  Create a function named max_num() that takes a list of numbers named nums as a parameter.

  The function should return the largest number in nums
"""

#Write your function here
def max_num(nums):
  max = nums[0]
  for number in nums:
    if number> max:
      max = number
  return max 


#Solution #2 using max()
def max_num_2(nums):
  maximus = max(nums)
  return maximus



#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
print(max_num_2([50, -10, 0, 75, 20]))


"""
  4. Same Values

  Write a function named same_values() that takes two lists of numbers of equal size as parameters.

  The function should return a list of the indices where the values were equal in lst1 and lst2.

  For example, the following code should return [0, 2, 3]
"""

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)

  return new_lst


print(" 4. Same Values")
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


"""
  5. Reversed List

  Create a function named reversed_list() 
  that takes two lists of the same size as parameters named lst1 and lst2.

  The function should return True if lst1 is the same as lst2 reversed. 
  The function should return False otherwise.

  For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
"""

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True



print(" 5. Reversed List")
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))