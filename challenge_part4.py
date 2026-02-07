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
