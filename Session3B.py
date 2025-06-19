names = ["john", "jennie", "jim"]
followers = names

print('names:')
print(names, type(names), id(names))
print('followers:')
print(followers, type(followers), id(followers))

names[1] = 'george'
names = ['leo', 'george', 'ben']

print('names now:')
print(names, type(names), id(names))
print('followers now:')
print(followers, type(followers), id(followers))

print(names[1], type(names[1]), id(names[1]))
print(followers[1], type(followers[1]), id(followers[1]))