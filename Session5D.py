# List         0         1         2       3      4
usernames = ['john', 'jennie', 'fionna', 'kia', 'leo']
search = input('Enter username to search: ')

"""
if usernames[0] == search:
    print('User Found', search)
elif usernames[1] == search:
    print('User Found', search)
elif usernames[2] == search:
    print('User Found', search)
elif usernames[3] == search:
    print('User Found', search)
elif usernames[4] == search:
    print('User Found', search)
else:
    print('User Not Found', search)

"""
# We are repeating the same logic again and again
# Loops: If we have to run the same logic again and again

# Linear Search Algorithm
# while loop
index = 0
flag = False
while index < 5:
    
    if usernames[index] == search:
        print('User Found', search, 'at', index)
        flag = True
        break
    else:
        print('user not found at ', index)
    
    # Update Statement
    index += 1

if flag == False:
    print('user not found')

# continue: HW