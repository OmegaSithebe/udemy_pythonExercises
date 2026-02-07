#Strings basics
#A string is an ordered sequence of characters.

print("AI says, I\'m here to assist you.")
print("AI says, I'm here to assist you.")

ai_reponse = """Hello there!
I'm an AI here to help.
Feel free to ask me anything."
"""

print(ai_reponse)


ai_prompt = 'Welcome to AI Bot\nYour virtual assistant\nHere to assist with all things tech!'
print(ai_prompt)

#backslash are special characters in Python, \t for tab & \n for new line, \\ to print \
print('\\ is essential for handling escape characters in Python')

gen_ai_message = 'Generative AI has revolutionized the way we create,\
from text generation to image synthesis. It is like having a creative partner!'
print(gen_ai_message)


#Python string are UTF eight encoded by default, so they support characters from various languages & even emojis. You can personalize reposnses or add some flair to your output.


#Getting user input

command = input('Ask your AI assistant a question: ')
print('Your question was: ', command)

#No matter what the user enters text, numbers, or symbols, the data is stored as a string. If you need to perfeorm calculations, you'll have to convert it.

training_hours = input('Enter hours spent training the model: ')
print('Data type of training_hours: ', type(training_hours))

iterations = input('Enter the number of model iterations: ')
iterations = int(iterations)
datasets = input('Enter the number of datasets: ')
datasets = int(datasets)
total = iterations * datasets
print('Total processing units: ', total)


#Another way to convert to int in a single line:
iterations = int(input('Enter the number of model iterations: '))
datasets = int(input('Enter the number of datasets: '))
total = iterations * datasets
print('Total processing units: ', total)

print("AI says, 'I’m here to assist you.'")


#Indexing Strings
#A string is an ordered sequence of UTF-8 encoded characters.

aText = 'GenAI is amazing!'
print(aText[0])
print(aText[5])
print(aText[-1])
print(aText[-7])
n = len(aText)
print(n)
print(aText[n-1])

#aText[0] = 'X'     #will give syntax error

#String Conctatination

gret = 'Hello, '
role = 'AI enthusiast'
print(gret + role + '!')


#Cannot conctatinate a string with a number
#print('Version ' + 5.7)    #Will throw an error

print('Version ' + str(5.7)) 


seperator = ':)'
print(seperator * 5)

#slicing - string[start:stop]
lens = 'Machine Learning'
print(lens[0:7])
print(lens[:7])
print(lens[9:])
print(lens[-4:])
print(lens[8:100])
print(lens[0:14:2])
print(lens[::-1])

print('Python 3!!!'[:7:2])


#Common String Methods
#A Method is like a function specifically tied to an object. All the variables seen so far are in fact objects or instances of a specific class.

#For example
x = 10  #I can say that x is a variable or an object of type int with a value 10
s = 'abc'  #Can say that s is an object of type string with the value ABC
print(type(x), type(s))   #This can be seen with a python function type to see the type of object


#These methods, as well as the ones covered are non-destructive. They don't modify the original string, but instead return a modified copy. 
model_output = 'ai IS the future of everything!'
print(model_output.upper())
print(model_output.lower())

response = ' !Hello, human! '
print(response.strip())
print(response.strip(' !'))

text = 'This is the ML, text of ML as it is'
updated_text = text.replace('ML', 'machine learning')
print(updated_text)

text3 = 'This future is the Future of ai future'
print(text3.count('future'))
print(text3.lower().count('future'))


statement = "This AI breakthrough at every step"
words = statement.split()
print(words)


terms = ['AI', 'ML', 'GenAI', 'LLM', 'NLP']
buzzwords = ''.join(terms)
print(buzzwords)
buzzwords = ', '.join(terms)
print(buzzwords)


url = 'https://example.com'
cleaned_url = url.removeprefix('https://')
print(cleaned_url)

filename = 'state_of_ai.pdf'
clean_filedname = filename.removesuffix('.pdf')
print(clean_filedname)

help(str)
help(str.strip)

'py' in 'Python'.lower()

text = 'Python is awesome'
print(text.split())


#Formatted string: using f-string for clean output
model_name = 'GPT'
version = 4
print('Hello from ' + model_name + ' - ' + str(version) + '!')
print(f'Hello from {model_name} - {version}!')

token_used = 123
cost_per_token = 0.001
total_cost = f'{token_used * cost_per_token:.4f}'
print(f'Total cost for this message: {total_cost}')


name, age = 'Alice', 30
print(f'Your name is {name} & your {age} years old')
print(f'Your name is {name=} & your {age=} years old') #include the = sign with the expression to the its value

r = 13.3
PI = 3.141592
print(f'The circle area with a radius of {r=} is {PI * r **2=}')
print(f'The circle area with a radius of {r=} is {PI * r **2:.4f}')