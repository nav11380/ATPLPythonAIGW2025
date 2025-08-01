message = 'hello, how are you? i hope are you doing good'
new_message = message.replace(',',' ')
another_new_message = new_message.replace('.',' ')
words = message.split(' ')
print(words,type(words))
print('words in message',len(words))

file = open('Session21.py')
data_in_file = file.read()
print(data_in_file)