message = "hello, how are you. i hope you are doing good"
new_message = message.replace(',', '') # remove ,
another_new_message = new_message.replace('.', '') # remove .
words = another_new_message.split(" ")
print(words, type(words))
print('words in message:', len(words))

# HW: Reference File: Session22A.py
# 1. Count the number of words in a plain text file
# 2. Locate, how many unique functions you used or created in a python file
# 3. Create a dictionary, where key is function name and value is number of times, it has been used

# 4. Ask the user, object name and attributes of the object using input function
#.   And create a python file for the object, which should have __init__, input_data, show

file = open('Session22A.py')
data_in_file = file.read()
print(data_in_file)