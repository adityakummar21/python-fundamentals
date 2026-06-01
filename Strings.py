my_str1 = "Hello"
my_str2 = "Goodbye"



print('ell' in my_str1)
print('dont' in my_str2, 'ello' in my_str2, 'ello' in my_str1) # in checks to see if chars exist in the string

##Use parantheses to print the length 
print(len(my_str1))


##Index
#In a string, each character is represented by an index value staring at 0 For Example:

print(my_str1[2]) #This will print the first l found in hello

#Negative indexing also exists, which takes you from the right to left. 

print(my_str1[-2]) #Which prints the 2nd l found in hello


##String Concatenation is the joining of 2 string, Ex:

print(my_str1 + '', my_str2)   #This prints Hello, Goodbye


##String interpolation: We can also combine a string with and integer as as whole string

name = 'Aditya'
age = 20
name_and_age = name
name_and_age += str(age)

print(name_and_age)



## f strings knows as formated string literals is a built int
## allows you to handle interpolation with a compact and readable syntax

name = "Drake"
planet_type = 'Venus'


print(f'My name is {name} I come from {planet_type} I am the meanest')

#Slicing [start:stop] starts at current index, stops just before the stop index 1-

word = 'Computer'

print(word[0:3])    # Com
print(word[-3:])    # ter
print(word[:-1])    # Compute
print(word[::-1])   # retupmoC (reverse string)

# String Methods
text = " hello world "

print(text.upper())  #prints 'HELLO WORLD'
print(text.lower())  #prints 'hello world'
print(text.title())  #prints 'Hello World'
print(text.strip())  #Prints and removes white space
print(text.replace("world", "Python")) #Prints and replaces 'world' with 'Python'


#Split and Join
sentence = "Aditya is a Programmer'

words = sentence.split  #Splits sentence into a list

print(words) #Prints ['Aditya', 'is', 'a', 'Programmer']

new_sentence = " ".join(words)  #Will print words with a space between each string
print(new_sentence) #Prints Aditya is a Programmer

#Escape Characters

print("Say\n Goodbye") #Prints Say Goodbye with a new line
print("He said \"hello\"")  #Prints "He said "hello""
print("Line one\nLine two") #Print Line one Line two as a new line
print("Column1\tColumn2")  #Prints "Column 1  Column 2" with a tab space







