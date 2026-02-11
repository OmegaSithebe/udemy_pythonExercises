#Data structure - represents a specialised format for organising, processing, retrieving and storing data.
#Lists allow us to store, access & modify multiple items in a single variable. 
#Python Lists is an ordered collection of items, which can include almost anything. Numbers, Strings even other lists (a container that can hold multiple pieces of information at once)
#Python lists are flexible, which makes them perfect for storing diverse data types.
#Lists in python are mutable - You can change, add, or remove elements without creating a new list. Different from strings as they are immutable
#In Python, lists can hold other lists as elements, creating what we call nested lists or 2D lists. This structure is helpful when dealing with complex data like matrix or grouped data.


#Creating a list with different data types
sample_list = [42, 3.1415, 'GPT-4', True]

empty_list1 = []
empty_list2 = list()    #Calling the list constructor


print(sample_list[0])
print(sample_list[-1])

# print(sample_list[100])     #This will give an error

sample_list[2] = 'This is Python language'
print(sample_list)

sample_list.append('PSL')
print(sample_list)
print(len(sample_list))

matrix = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]                   #This is a nested list or a 2D list

print(matrix[1][2])



#Lists Operations: Concatenation, Slicing, Iteration
#1. Lists Concatenation - (combining 2 lists into 1)

l1 = [3, 4]
print(l1, id(l1))

l1 = l1 + [5, 6]
print(l1, id(l1))

l1 += [7, 8]
print(l1, id(l1))

l1.extend([11, 12])         #Iterable in Python is an object capable of returning its elements one at a time, allowing it to be used in loops or converted into other data structures like lists.
print(l1, id(l1))           #Becareful between append & extend - (append adds a single item), (extend add all elements from an iterable)

l1.append(['a', 'b'])
l1.extend(['x', 'y'])
print(l1)

#2. Lists Slicing - is a powerful feature that allows you to retrieve parts of a of a list. Think of it as zooming in on specific elements without altering the original list
numbers = [1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums: {nums}')
print(f'numbers: {numbers}')

print(numbers[:3])
print(numbers[2:])
print(numbers[1:5:2])
print(numbers[::-1])

#Quiz Lists:
# q3:
l1 = ['go', '[5,6,7]', 'swift3', 55, [8, 9, 10]]
print(l1[0][1])  #o

#q4 - what will the result of my_list[4][-1] be?
my_list = [[3, 4, 5], 7, 8.9, 'x', ['p', 'q', 9.9]]  #99

#q7
my_list = [[7, 8, 9], 2, 3.5, 'b', ['r', 's', 4.4]]
print(my_list[2:100])  #[3.5, 'b', ['r', 's', 4.4]]
#The syntax for slicing is: list[start:end] - It returns a sublist from the start index up to, but not including, the end index. - Important: The index specified as the end is not included in the resulting sublist.
#Difference between "index taken" and "index not taken": "Index of the slicing is taken" (inclusive): This is not how Python slicing works. However, sometimes people think the end index is included, but in Python, it's exclusive. "Index of the slicing is not taken" (exclusive): This is the correct behavior in Python. The end index is not included in the slice. How to remember: When you write list[start:end], the slice includes elements from start up to but not including end.
#If you want to include index end, you need to set the slice to list[start:end+1].


#q8
my_list = [[7, 8, 9], 2, 3.5, 'b', ['r', 's', 4.4]]
print(my_list[2:][-1])  #['r', 's', 4.4]

#q9
nums1 = [3, 4.9, 12]
nums2 = nums1
nums2.append('w')
nums2.extend(['z'])
print(nums1) 
#answer [3, 4.9, 12, 'w', 'z'] because when you append 'w' and extend the list with ['z'] using nums2, which refers to the same list as nums1, both lists are updated to include those new elements.

#q10
l1 = list('opq')
l2 = l1
l1[1] = 88
print(l2)
#q10 - answer ['o', 88, 'q'] because when you set l1[1] = 88, it modifies the list l1, which l2 refers to, reflecting the change in l2

#q11
l1 = [25, 35, 45, 55]
l2 = l1.copy()
l1.append(95)
print(l2)
# q11 - answer [25, 35, 45, 55] because when you use l1.copy(), it creates a new list l2 with the same elements as l1, and any subsequent changes made to l1, such as appending 95, do not affect l2.
# (In Python, when you use the copy() method on a list (like l1.copy()), it creates a shallow copy of the list. This new list (l2) is a separate object in memory, with its own storage for the elements.
# Because it is a distinct list, any modifications to l1 after copying—such as appending a new element with append()—do not affect l2. They are independent lists, and changes made to one do not reflect in the other.)

#q12
l1 = list('mno')
l2 = l1
l1 = []
print(l2)
# q12 - In Python, when you do l2 = l1, both l1 and l2 refer to the same list object in memory. However, when you later assign l1 = [], you are reassigning the variable l1 to point to a new, separate list (an empty one). This does not change l2, which still points to the original list containing 'm', 'n', and 'o'.
# (l2 still points to the original list with its elements 'm', 'n', 'o' because its reference was not changed; only l1's reference was updated.)




#3. Iteration and Membership Testing
ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']

for ip in ip_list:
    print(f'Connecting to {ip} ....')
    
    
target_ip = '10.0.0.1'
if target_ip in ip_list:
    print(f'{target_ip} is in the list')


prefix = '192'
if prefix not in ip_list:
    print(f'No addresses with the prefix {prefix} found in the list')
#The not operator returned true and the entire testing condition return true
# prefix in ip_list checks whether the exact string '192' is an element of the list.
# But your list elements are full IP addresses like '192.168.0.1', not '192'.
# So '192' is not equal to any item in the list → the condition is False.


l1 = [1, 2, 3]
l2 = l1 #this doesn't create a copy, just references the same list
l2[0] = 'xx'    #if you change l2, l1 also changes because they point to the same memory location
l2.append(10)
print(l2, l1)


l3 = l1.copy()  #this is creating the exact copy of the list, l3 is a copy of l1
l3.append('ABC')  #this will only affect l3
print(l3, l1) 
#Avoid modifying lists while iterating. This is another gotcha and involves modifying a list while iterating over it. This can lead to unexpected results. 

nums = [1, 2, 3, 4, 5, 6, 7]
for n in nums:
    if n < 5:
        nums.remove(n)  #attempting to modify the list, while iterating and outside the for loop. 
print(nums)  

#A correct approach is to create a new list for elements you want to keep. 

new_list = []
for n in nums:
    if n >= 5:
        new_list.append(n)  #Not changing the nums list while iterating over it.
        
print(new_list)