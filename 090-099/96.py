
def read_games():
    games = []
    with open('p096_sudoku.txt') as f:
        while f.readline():
            games.append([f.readline().replace('\r','').replace('\n','') for line in xrange(9)])
    return games

def solve(game):
    pass

games = read_games()
