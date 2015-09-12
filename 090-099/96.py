import time

square1 = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
square2 = [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
square3 = [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]
square4 = [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]
square5 = [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]
square6 = [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]
square7 = [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]
square8 = [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]
square9 = [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]
squares = [square1,square2,square3,square4,square5,square6,square7,square8,square9]

def print_game(game):
    print '\n'
    for i,line in enumerate(game):
        if i in [3,6]:
            print '-'*6+'+'+'-'*7+'+'+'-'*6
        print line[0],line[1],line[2],'|',line[3],line[4],line[5],'|',line[6],line[7],line[8]

def read_games():
    games = []
    with open('p096_sudoku.txt') as f:
        while f.readline():
            games.append([[int(num) for num in f.readline().replace('\r','').replace('\n','')] for line in xrange(9)])
    return games

def is_completed(game):
    for line in game:
        if 0 in line:
            return False
    return True

def missing_values(game):
    return sum([line.count(0) for line in game])

def find_square(n):
    for square in squares:
        if n in square:
            return square

def get_line(game,n):
    return game[n]

def get_column(game,n):
    temp = []
    for line in game:
        temp.append(line[n])
    return temp

def get_square(game,n,line=-1,column=-1):
    temp = []
    for i,j in find_square(n):
        if line != -1 or column !=-1:
            if line == i or column == j:
                temp.append(game[i][j])
        else:
            temp.append(game[i][j])

    return temp

def update_line_poss(poss,num,n):
    for j,pos in enumerate(poss[n]):
        if num in pos and len(pos)>1:
            poss[n][j].remove(num)
    return poss

def update_line_other_squares(poss,d,n):

    own_square = find_square(n)

    for j,pos in enumerate(poss[n[0]]):
        if (n[0],j) not in own_square:
            if d in pos and len(pos)>1:
                poss[n[0]][j].remove(d)
    return poss


def update_column_poss(poss,num,n):
    for i,pos in enumerate(poss):
        if num in pos[n] and len(pos[n])>1:
            poss[i][n].remove(num)
    return poss

def update_column_other_squares(poss,d,n):
    own_square = find_square(n)
    for i,pos in enumerate(poss):
        if (i,n[1]) not in own_square:
            if d in pos[n[1]] and len(pos[n[1]])>1:
                poss[i][n[1]].remove(d)
    return poss


def update_square_poss(poss,num,n):
    for i,j in find_square(n):
        if num in poss[i][j] and len(poss[i][j])>1:
            poss[i][j].remove(num)
    return poss


def update_game(poss,game):

    for i,line in enumerate(poss):
        for j,pos in enumerate(line):
            if game[i][j]!=0 and len(pos)>1:
                poss[i][j] = [game[i][j]]
                num = game[i][j]
                poss = update_line_poss(poss,num,i)
                poss = update_column_poss(poss,num,j)
                poss = update_square_poss(poss,num,(i,j))
            if game[i][j] == 0 and len(pos) == 1:
                #print i,j,pos[0]
                game[i][j] = pos[0]
                num = game[i][j]
                # print i,j,game[i][j],pos
                poss = update_line_poss(poss,num,i)
                poss = update_column_poss(poss,num,j)
                poss = update_square_poss(poss,num,(i,j))

            for d in poss[i][j]:

                d_in_line = sum([l.count(d) for l in get_line(poss,i)])
                d_in_column = sum([l.count(d) for l in get_column(poss,j)])             
                d_in_square = sum([l.count(d) for l in get_square(poss,(i,j))])

                if game[i][j] ==0 and game[i][j]!=d and (d_in_line == 1 or d_in_column == 1 or d_in_square == 1):
                    game[i][j] = d
                    # print 'extra'
                    # print d_in_line,d_in_column,d_in_square
                    # print i,j,d

                if  game[i][j]==0 and sum([l.count(d) for l in  get_square(poss,(i,j),i)]) == d_in_square:
                    poss = update_line_other_squares(poss,d,(i,j))
                    # print 'guess1'
                    # print_game(game)
                    # print d_in_line,d_in_square
                    # print i,j,d
                if  game[i][j] ==0  and sum([l.count(d) for l in  get_square(poss,(i,j),-1,j)]) == d_in_square:
                    # print 'guess2'
                    # print_game(game)
                    # print d_in_column,d_in_square
                    # print i,j,d
                    poss = update_column_other_squares(poss,d,(i,j))


    return game,poss

def solve(game):
    ini = time.time()
    completed = False
    poss = [[range(1,10) for i in xrange(9)] for i in xrange(9)]
    while not completed:

        #print '{}/81'.format(missing_values(game))

        game,poss = update_game(poss,game)

        completed = is_completed(game)

    print_game(game)
    print time.time()-ini
    return game

import copy

games = read_games()
game = copy.deepcopy(games[5])
# solved_games = [solve(game) for game in games]

completed = False
poss = [[range(1,10) for i in xrange(9)] for i in xrange(9)]

while not completed:

    #print '{}/81'.format(missing_values(game))
    ini = time.time()
    game,poss = update_game(poss,game)

    completed = is_completed(game)

print_game(game)
print time.time()-ini