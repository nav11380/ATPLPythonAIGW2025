# Create Statement
# Multi Value Container
johns_followers = ('fionna', 'kia', 'jim', 'joe', 'jack')
ipl_player_scores = 90, 50, 30, 20, 65, 37
menu = 'dal', 300, 'paneer', 400, 'noodles', 350

print('johns_followers')
print('~~~~~~~~~~~~~~~')
print(johns_followers)
print('johns_followers hashcode', id(johns_followers))
print('johns_followers type', type(johns_followers))
print('~~~~~~~~~~~~~~~')

print()

print('ipl_player_scores')
print('~~~~~~~~~~~~~~~')
print(ipl_player_scores)
print('ipl_player_scores hashcode', id(ipl_player_scores))
print('ipl_player_scores type', type(ipl_player_scores))
print('~~~~~~~~~~~~~~~')

print()

print('menu')
print('~~~~~~~~~~~~~~~')
print(menu)
print('menu hashcode', id(menu))
print('menu type', type(menu))
print('~~~~~~~~~~~~~~~')

print('menu[0]:', menu[0], id(menu[0]), type(menu[0]))
print('menu[1]:', menu[1], id(menu[1]), type(menu[1]))
print('menu[2]:', menu[2], id(menu[2]), type(menu[2]))
print('menu[3]:', menu[3], id(menu[3]), type(menu[3]))
print('menu[4]:', menu[4], id(menu[4]), type(menu[4]))
print('menu[5]:', menu[5], id(menu[5]), type(menu[5]))