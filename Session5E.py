# List         0         1         2       3      4
usernames = ['john', 'jennie', 'fionna', 'kia', 'leo']
search = input('Enter username to search: ')

# for loop
# for index in range(0, 5, 1):

flag = False

for index in range(0, 5): #Loop runs from 0 till less than 5 i.e. 4
    if usernames[index] == search:
        print('User Found', search, 'at', index)
        flag = True
        break
    else:
        print('user not found at ', index)

if flag == False:
    print('user not found')


# can write infinifte loops
# while True:
#     pass

# HW: Explore how to make for as infinite ? Is this possible ?
