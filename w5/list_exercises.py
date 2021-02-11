# Exercise 6-a: Calling Elements of a Python List (Index 0)
# - Assign the first element of the list to answer_1 
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]
print(answer_1)
# I was able to complete this without help

# Exercise 6-b: Calling List Elements and Indexing
# - And let's print the second element directly inside print function.
# - This time print the second element of the list directly
lst = [11, 100, 101, 999, 1001]
print(lst[1])
# I was able to complete this without help

# Exercise 6-c: Calling List Elements(Negative Index)
# - Print the last element of the list through variable answer_1.
lst = [11, 100, 101, 999, 1001]
answer_1 = lst[-1]
print(answer_1)
# I was able to complete this without help

# Exercise 6-d: Append method to add items to the end of Python Lists
# - .append method will let you add items to your lists.
# - add the string "pajamas" to the list with .append() method.
gift_list = ['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append('pajamas')
print(gift_list)
#I was able to complete this without help

# Exercise 6-e: List inside List (Python Nested Data)
# - Lists can hold many type of data inside them. You can even add another list to a list as its element. This is called nested data in Python.
# - This time add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list.
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append(['socks', 'tshirt', 'pajamas'])
print(gift_list)
# I was able to complete this without help

# Exercise 6-f: Insert method to add to a specified index of a Python List
# - .insert() lets you specify the index you want to add your item, this time insert "slippers" to index 3 of gift_list.
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.insert(2, 'slippers')
print(gift_list)
# I was able to complete this without help

# Exercise 6-g: Index method to get the index of a List Item
# With .index() method you can learn the index number of an item inside your list. Assign the index no of 8679 to the variable answer_1.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer_1 = lst.index(8679)
print(answer_1)
# I was able to complete this without help

# Exercise 6-h: Adding a different type of element to a List using Append
# Using .append() method, add a new list to the end of the list which contains strings: "Navigator" and "Suburban".
lst = ['CRV', 'Outback', 'XC90', 'GL', 'Cherokee', 'Escalade']
# Type your code here.
lst.append(['Navigator', 'Suburban'])
print(lst)
# I was able to complete this without help

# Exercise 6-i: Removing the last item of a list (.remove() method)
# Using .remove() method, clear the last element of the list.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
# Type your code here.
lst.remove(99)
print(lst)
# I was able to complete this without help

# Exercise 6-j: Reversing a Python list (.reverse() method)
# Using .reverse() method, reverse the list.
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
# Type your code here.
lst.reverse()
print(lst)
# I was able to complete this without help

# Exercise 6-k: Count Method to get the amount of an item in a list
# .count() method tells how many times a value occur in a list. You need to type the value you’re checking inside .count()
# Using .count() method, count how many times 6 occur in the list.
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
# Type your code inside print() function.
answer_1 = lst.count(6)
print(answer_1)
# I was able to complete this without help

# Exercise 6-l: Adding up all the items in a List w/ Sum Function
# sum() function will calculate the total sum inside the numbers of your list.
# What is the sum of all the numbers in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
# Type your code on line 4:
answer_1 = sum(lst)
print(answer_1)
# I was able to complete this without help

# Exercise 6-m: Max Function to Get the Lowest Value in a List
# min() function will show the minimum value of the list.
# What is the minimum value in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
# Type your code on line 4:
answer_1 = min(lst)
print(answer_1)
# I was able to complete this without help

# Exercise 6-n: Max Function to Get the Highest Value in a List
# max() function will show the minimum value of the list.
# What is the maximum value in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
# Type your code on line 4:
answer_1 = max(lst)
print(answer_1)
# I was able to complete this without help



