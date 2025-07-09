# Explore SET 
# Uniqueness

john_followers = {'fionna', 'sia', 'kim', 'harry', 'george', 'sia'}
print('john_followers:', john_followers)
print('type john_followers:', type(john_followers))
print('length john_followers:', len(john_followers))

numbers = list(range(10, 101, 10))
# convert list into set
data = set(numbers)
print('data:', data)

data.add(50)
data.add(500)

print('data:', data)
# data will be removed i.e. the first element based on hashing
# data.pop()

data.remove(100)
print('data:', data)

john_followers = {'fionna', 'joe', 'sia', 'kim', 'harry', 'george', 'sia'}
jack_followers = {'anna', 'sia', 'kia'}
fionna_followers = {'joe', 'sia'}

mutual_followers = john_followers.intersection(jack_followers)
print('mutual_followers:', mutual_followers)

# result = fionna_followers.issubset(john_followers)
result = john_followers.issuperset(fionna_followers)
print('result:', result)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Operators on Set
# Concatenation: error -> not supported on Set
# C = A + B
# print('C:', C)

print('A:', A)
print('B:', B)

D = A - B
print('D:', D)

E = A ^ B
print('E:', E)

F = A | B
print('F:', F)

A.clear()
print('A is: ', A)
