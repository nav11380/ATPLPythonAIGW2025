"""
    Another Brick in the Wall
    john
    jack

    harry: 11 bricks
                total
    john: 1     1
    jack: 2     3
    john: 2     5
    jack: 4     9
    
  > john: 3     12 <
    
    john: 2     11

    Goal: Find who placed the last brick. john or jack ?
          and how many bricks in the end ?
          
          Ans
          john: 2     11

"""

bricks_by_customer = int(input('Enter Number of Bricks: '))
print('Wall must be constructed with',bricks_by_customer, 'bricks' )

total_bricks = 0

for brick in range(1, bricks_by_customer+1):
    
    john = brick # Assumption, where brick index starting from 1 is brick placed by john
    total_bricks += john

    if total_bricks > bricks_by_customer:
        extra_bricks = total_bricks - bricks_by_customer
        last_bricks = john - extra_bricks
        print('john placed last brick(s)', last_bricks)
        # print('john placed extra brick(s)', extra_bricks)
        break

    jack = john * 2
    total_bricks += jack

    if total_bricks > bricks_by_customer:
        extra_bricks = total_bricks - bricks_by_customer
        last_bricks = jack - extra_bricks
        print('jack placed last brick(s)', last_bricks)
        # print('jack placed extra brick(s)', extra_bricks)
        break
