# List supports duplicates
followers = ['john', 'jennie', 'jim', 'jack', 'joe', 'jennie']
print('followers:')
print(followers, type(followers), id(followers))

for name in followers:
    print(name)


print("~~~~~~~~~~~~~~~~~~~~~~~~~")

# Set
# Supports Uniqueness
# It wont work on indexing technique. Its uses hashing
# Hence, the output will be unordered because of hashing
followers = {'john', 'jennie', 'jim', 'jack', 'joe', 'jennie'}
print('followers now:')
print(followers, type(followers), id(followers))

fionna_followers = {'sia', 'kim', 'joe', 'jennie'}

print('fionna_followers now:')
print(fionna_followers, type(fionna_followers), id(fionna_followers))

# mutual_followers = followers.intersection(fionna_followers)
mutual_followers = followers & fionna_followers
print('mutual_followers now:')
print(mutual_followers, type(mutual_followers), id(mutual_followers))

# You can always read all the elements, but cannot capture single element from set
# As indexing is not allowed
# print(fionna_followers[0]) # error

# for Loop : Enhanced Version of For Loop, for each loop
for name in fionna_followers:
    print(name)
