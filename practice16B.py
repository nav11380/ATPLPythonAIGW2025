john_followers ={'fionna', 'sia', 'kim', 'harry'}
print('john_followers', john_followers)
print('type john_followers', type(john_followers))
print('length john_followers', len(john_followers))

numbers = list(range(10,101,10))

data = set(numbers)
print('data:', data)

data.add(50)
data.add(500)

print('data:', data)


data.remove(100)
print('data:', data)

john_followers ={'fionna', 'sia', 'kim', 'harry'}
jacK_followers = {'anna', 'sia', 'kia'}
fioana_followers = {'joe',"sia"}

mutual_followers = john_followers.intersection(jacK_followers)


A = {1,2,3,4,5}
B = {4,5,6,7,8}

#C = A + B
#print('C:', C)

D =A - B
print('D:', D)

E = A ^ B
print('E:', E)

F = A | B
print('F:', F)

A.clear()
print('A is:', A)


