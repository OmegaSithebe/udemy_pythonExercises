#Challenge 1
a = 16
t = 55.9
g = True
s = 'Love'
bits = [16, 8, 32, 64]

print(type(a))
print(type(t))
print(type(g))
print(type(s))
print(type(bits))


#Challenge 2
var_One = 10
var_Two = 20

"""
This is 
an example of a multiline
comment in Python.
"""

my_str = 'Hello'
print(my_str)


#Challenge 3
# This script contains some syntax errors.
# Modify the script so that it runs without any errors.

best_friend = 'Anne'
print('My best friend is ', best_friend)

my_value = 15

age = 18
print(age == 10)

a, b = '10', '20'
print(a + b)

print('To comment a line of code you # at the beginning of the line.')


#Challenge 4
# Using different Python operators

x = 10
y = 3

result1 = x == y  # Equality
result2 = x >= y  # Greater than or equal
result3 = x * y  # Multiplication
result4 = x ** y  # Exponentiation
result5 = x / y  # Division (float)
result6 = x // y  # Floor division
result7 = x % y  # Modulus

x += 5  # Increment x by 5
y *= 2  # Multiply y by 2

print(result1, result2, result3, result4, result5, result6, result7)
print(x, y)


#Challenge 5
a = ((16 / 2) + (6 / (2 ** 2)))
print(a)
a = 16 / ((2 + 6) / 2)**2
print(a)


"""
Your version:

Treats the expression as two separate parts added together: (16/2) plus 6/(2**2).
There is no shared denominator and no squaring of a grouped term besides the 2**2 in the second part.

The solution:

Enforces a specific grouping with parentheses: compute (2 + 6) / 2 first, then square the whole result, and use that as the single denominator of 16.

Even though both lines contain 2**2 in spirit (because the solution ends up squaring 4), the placement of parentheses changes the structure drastically:

Your denominator for the second term is only 2**2.
The solution’s denominator is ((2 + 6) / 2) ** 2.


🔍 Side-by-side comparison


Yours:
a=162+622=8+64=8+1.5=9.5a = \frac{16}{2} + \frac{6}{2^2} = 8 + \frac{6}{4} = 8 + 1.5 = 9.5a=216​+226​=8+46​=8+1.5=9.5


Solution:
a=16(2+62)2=1642=1616=1a = \frac{16}{\left(\frac{2 + 6}{2}\right)^2} = \frac{16}{4^2} = \frac{16}{16} = 1a=(22+6​)216​=4216​=1616​=1

"""

#Challenge 6
# Calculate total IPv6 addresses (2^128)

total_ipv6_addresses = 2 ** 128
print(total_ipv6_addresses)