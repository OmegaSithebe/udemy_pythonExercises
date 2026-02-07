#Static vs Dynamic
#Static compile at run time (meaning a variable must be declared before used)
    #Advantages: errors are caught easily during the complilation process
    #Programs often perform better at run-time as no need for interpreter to figure out the types
#Dynamic you do not need to declare a type of the variable. Instead, the type is tied to the value assigned to the variable at runtime
    #Flexibility allows you to develop faster, you can focus on writing the logic without worrying about its declarations
    #Disadvantages - runtime bugs, since types are determined at runtime, errors like assignment, the wrong type can slip through & only show up when the program runs. Debugging challenges. 

#Static
#Java
# int score;
# score = 10;

#Dynamic
score = 10 #int
print(type(score))

score = 'Python'
print(type(score))


#Python notations - they are a way to combine Python's flexibility with additional safeguards.

#Static typing - common in languages like Java & C, catches types errors early & can booast run-time performance but slows down development.
#Dynamic typing - makes Python more flexibile & intuitive, but it can lead to run-time bugs & harder-to-diagnose issues.
#Type annotations - provides a middle ground, helping you catch potential issues earlier without sacrificing Python's dynamix nature.




#Numbers AND Math Operators
#Python Operators
#An operator is a symbol that tells Python to perform a specific operation on values
# - Arithmwtic Operators: + - * / // ** %
# - Assignment Operators: = += -= *= /=
# - Comparison Operators: == != > >= < <=
# - Identity Operators: "is" "is not"
# - Logical Operators: "and" "or" "not"

#Numbers & Math Operators
#Addition (+) and Subcraction (-) are straighforward

#Multiplication (*)

#Division (/) returns a float results no matter the calculation
print(8 / 2)

#Float Division (//) returns a whole discard any remainder
print(11 // 5)

#If you mix interger with float, the results will be float
print(5 * 3.0)

# Exponentiation (**)
print(2 ** 3)

#Order of operations (operator precedence)
#Exponentiation(**), Multiplication(*) & Division(/), Addition(+) & substration(-)
#E.g
print(2 + 4 * 2 ** 3)
print((2 + 4) * 2 ** 3)

#Python allows underscores as visual seperators, which can help make values easier to read
#10000001000
#10_000_001_000
print(10_000_001_000)

print(18 % 3, 15 / 3, 16 // 3, 2 ** 3)



#Assignment Operators
#Equals (=)
#Plus equals (+=)
#Minus equals (-=)
#Star equals (*=)
#Slash equals (/=)
#Double stars equals (**=)
#Percentage equals (%=)


a = 6

a += 2 #same as a = a + 2
print(a)

a -= 3
print(a)

# *=, /*, **=, %=, //=

a *= 10
print(a) 



#Comparison Operators
#Equal to (==)
#Not equal to (!=)
#Greater than (>)
#Greater than or equal to (>=)
#Less than (<)
#Less than or equal to (<=)


a, b = 10, 5
print(a == b)
print(a > b)


#Identity operators is, is not
a is b


#Mutability vs Immutability
#Mutable objects like lists, can be changed after they are created while immutable objects like integers or strings cannot be changed.
#Python creates a new memory address if you try to change an immutable variable 
#Since integers are immutable with mutable types like lists. However, the memory address remains the same. 

a = 4
print(id(a))
a += 16
print(id(a))


numbers = [3, 6, 9]
print(id(numbers))
numbers.append(12)
print(id(numbers))


x = 8
x **= 3
x /= 4
print(x)