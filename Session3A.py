# Multi Value Container: List -> Mutable
names = ["john", "jennie", "jim"]
print('names:')
print(names, type(names), id(names))

# Reference Copy Operation
followers = names

print('followers:')
print(followers, type(followers), id(followers))
print(names[1], type(names[1]), id(names[1]))

followers[1] = "george"

print('names now:')
print(names, type(names), id(names))
print('followers now:')
print(followers, type(followers), id(followers))

print(names[1], type(names[1]), id(names[1]))
