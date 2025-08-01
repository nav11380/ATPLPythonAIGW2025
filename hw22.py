
# 1. Count the number of words in a plain text file
#words = 'Artificial Intelligence is transforming the way we live and work. From virtual assistants to self-driving cars, AI is becoming an integral part of modern technology. With continuous advancements, it promises to bring efficiency, automation, and smarter solutions to everyday problems.'
def count(text):
    words = text.split()
    return len(words)

paragrah = 'Artificial Intelligence is transforming the way we live and work. From virtual assistants to self-driving cars, AI is becoming an integral part of modern technology. With continuous advancements, it promises to bring efficiency, automation, and smarter solutions to everyday problems.'
words_count = count(paragrah)
print("Total number of words in the string:", words_count)

#2. Locate, how many unique functions you used or created in a python file
#strip,lstrip,rstrip,float,str,replace,center,ljust,rjust,find,lfind,rfind

# 3. Create a dictionary, where key is function name and value is number of times, it has been used

