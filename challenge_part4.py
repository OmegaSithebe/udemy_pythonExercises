#Challenge 1
# A company has a revenue of 45,897,513.
# Calculate its profit, assuming profit is 12.7% of the revenue.
# Display the result rounded to two decimal places.

revenue = 45897513
profit = 12.7
total_profit = revenue * (12.7/100)
total_profit2 = round(total_profit, 2)
print('Total profit for the company is R' + str(total_profit2))

# revenue = 45_897_513
# profit_percentage = 12.7 / 100
# profit = revenue * profit_percentage
# # Display profit with 2 decimal places
# print(f'Company\'s profit: ${profit:.2f}')


#Challenge 2
# Consider the following string declaration which is part of the output of a Linux command.
# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
# Try to solve the challenge in more than one way.
# [Stuck? Click here to see the solution.]

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
new_str = my_str.removeprefix('wlo1 Link encap:Ethernet HWaddr ')
print(new_str)

new_str2 = my_str.split(' ')
print(new_str2[4])

mac = my_str[len(my_str) - 17:]
print(mac)

mac2 = my_str[-1:-18:-1]
mac2 = mac2[::-1]        # reverse the string
print(mac2)               # => b4:6d:83:77:85:f3

# Split the string into a list and return the last list element which is the MAC address
mac3 = my_str.split() [-1]
print(mac3)



# Challenge 3
# Display the following strings literally:
# It displayed: "You've got an error!"
# \n means a new line.
# \ is known as the escape character.
# [Stuck? Click here to see the solution.]


message =  "It displayed: \"You've got an error!\""
print(message)

message2 = 'It displayed: "You\'ve got an error!"'
print(message2)

new_line = '\\n means a new line'
print(new_line)

print(r'\n means a new line')       #r'' means a new string where \ doesn't have a special meaning.

print('\\ is known as the escape character.')



#Challenge 4
# Write a Python script to convert feet (ft) to centimeters (cm).
# Conversion: 1 ft = 30.48 cm
# Prompt the user to enter a value in feet.
# Display the result in centimeters with two decimal places, formatted using an f-string.

valueFt = int(input('Please enter value in ft(foot):'))
totalCM = valueFt * 30.48
print(f'Total conversion from Foot to Centimeters is: {totalCM:.2f} cm')


# ft = float(input('Enter distance (in ft):'))
# cm = ft * 30.48
# print(f'{ft} ft = {cm:.2f} cm')


#Challenge 5
#Write a Python script to check if a string is a palindrome.


s1 = 'mom'
print(f'Is s1 palindrome? => {s1 == s1[::-1]}')

s2 = 'eve'
print(f'Is s2 a palidrome? {s2 == s2[::-1]}')

s3 = 'daddy'
print(f'Is s3 a palidrome? {s3 == s3[::-1]}')


#Challenge 6
#Change the solution of the previous challenge to ignore whitespace and letter case when checking if a string is a palindrome.

s1 = 'mom is not home'
s1 = s1.replace(' ', '')
s1 = s1.lower()
print(f'Is s1 palindrome? => {s1 == s1[::-1]}')


s2 = 'mom eve'
s2 = s2.replace(' ', '')
s2 = s2.lower()
print(f'Is s2 a palindrome? => {s2 == s2[::-1]}')

s3 = 'Able was I ere I saw Elba'
s3 = s3.replace(' ', '')
s3 = s3.lower()
print(f'Is s2 a palindrome? => {s3 == s3[::-1]}')



# Challenge 7
# Write a Python script that extracts the first and last two characters from a user-entered string.
# Example: Input: 'Hello!', Output: 'Heo!'

chara = input('Enter a character:')
new_char = chara[:2] + chara[-1:]
print(new_char)


my_str = input('Enter a string(min 2 chars):')
new_str = my_str[:2] + my_str[-3:]
print(new_str)

#Explanatino:
#[:] means “slice” - :2 means “from the start up to index 2 (not including 2)” - chara[:2] = "He"
#chara[-1:] — take the LAST character - Negative indexes count from the end - (-1 = last character) - chara[-1:] = "o"
#"He" + "o" = "Heo"
#string[start:end] - string[start:end] - (start → where to begin (included)) - (end → where to stop (NOT included))
# Slice Meaning
# s[:3]from start → index 2
# s[3:]from index 3 → end
# s[:]entire string


#***NB***
# 3. Slicing (Manual Manipulation)
# Slicing allows you to "add" or "remove" by rebuilding the string from parts. 
# Syntax: string[start:stop:step].
# Remove last 2: str[:-2].
# Remove first 2: str[2:].
# Insert at index i: str[:i] + "new" + str[i:]

# 2. Adding / Combining Content
# Concatenation (+): Joins two strings together: "a" + "b" → "ab".
# .join(iterable): Concatenates elements of an iterable (like a list) using the string as a separator: "-".join(["a", "b"]) → "a-b".
# .center(width[, fillchar]): Pads the string with a specified character to reach a certain width.
# .ljust() / .rjust() / .zfill(): Adds padding to the left or right to align text or pad numbers with zeros

# 1. Removing Content
# .replace(old, new[, count]): Replaces occurrences of a substring. To "remove," replace with an empty string: "hello".replace("l", "") → "heo".
# .strip([chars]): Removes leading and trailing characters (defaults to whitespace).
# .lstrip() / .rstrip(): Removes characters only from the left or right side.
# .removeprefix(prefix) / .removesuffix(suffix): Removes a specific exact sequence from the start or end (added in Python 3.9).
# .translate(table): Highly efficient for removing multiple specific characters at once using a mapping table


# Challenge 8
# Write a Python script that replaces all occurrences of the first character in a string with '$', except for the first occurrence itself.
# Example:
# Input: 'mama'
# Output: 'ma$a'

string = input('Enter a string')
char = string[0]
new_string = string[1:].replace(char, '$')
print(char+new_string)


# Challenge 9
# Write a Python program to remove the character at the nth index from a non-empty string.
# The nth index is provided by the user.

n = int(input('Enter the index of of the char:')) #2
str22 = input('Enter the string:') #omega
firstS = str22[:n] #om          o - m) - e - (g - a
lastS = str22[n+1:] #ga         0 - 1) - 2 - (3 - 4
comb = firstS + lastS
comb1 = firstS
comb2 = lastS
print(comb1 + ' - ' + comb2)
print(comb)


#Solution:
# n = int(input('Enter the nth index char to remove:'))
# my_str = input('Enter the string to change:')
# first_part = my_str[0:n]
# last_part = my_str[n+1:]
# new_str = first_part + last_part
# print(new_str)


# Challenge 10
# Write a Python script that removes characters at odd index positions from a given string.

strGv = input('Enter a string:')
newGv = strGv[::2]
print(newGv)

#Explanation
#string[start : end : step], start → where to begin - end → where to stop - step → how many characters to skip each time
#start → empty → Python starts at index 0 - end → empty → Python goes to the end - step = 2 → take every second character


#Challenge 11
# Write a Python script that prompts the user for a circle's radius and calculates its area.
# Formula: Area = π * r² (π = 3.1415)
# Display the area with four decimal places using an f-string.

radius = float(input('Enter a circle\'s raduis: '))
pie = 3.1415
area = pie * (radius**2)
print(f'The total area of the circle is: {area:.4f}cm')


#Challenge 12
# Write a Python script that counts the number of occurrences of a substring in a given string, ignoring letter case.

gvStr = "Welcome to Romania. romania is an awesome country, isn't it? Hello roMania!"
subStr = "Romania"

new_str = gvStr.lower()
count = new_str.count(subStr.lower())
print(f'The number of substring: {subStr} in the given string is: {count}')


# Challenge 13
# Write a Python script to format a number using:
# US/UK format: A comma , as the thousands separator
# EU format: A period . as the thousands separator
# Example:
# Input: 1234567
# Output: 1,234,567 (US/UK) and 1.234.567 (EU)

num = 123456789
n_comma = f'{num:,}'
print(n_comma)

print(n_comma.replace(',', '.'))

