order_hand = ['High Card','One Pair','Two Pairs','Three of a Kind','Straight','Flush','Full House','Four of a Kind','Straight Flush','Royal Flush']
order_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def get_hand(hand):
    result = ('None','None')
    face = sorted([(order_cards.index(c[0]),c[0]) for c in list(hand)])
    order = [c[0] for c in face]
    face_fig = [c[1] for c in face]
    naipe = [c[1] for c in list(hand)]
    count_cards = [face_fig.count(c) for c in face_fig]

    if range(face[0][0],face[-1][0]+1) == order:
        result = face[-1][0],'Straight'
        if len(set(naipe)) == 1:
            result = face[-1][0],'Straight Flush'
            if face[-1][1] == 'A':
                result = face[-1][0],'Royal Flush'
    else:
        if len(set(naipe)) == 1:
            result = (face[-1]),'Flush'
        else:
            if 4 in count_cards:
                result = face_fig[count_cards.index(4)],'Four of a Kind'
            elif 3 in count_cards:
                result = face_fig[count_cards.index(3)],'Three of a Kind'
                if 2 in count_cards:
                    result = (face_fig[count_cards.index(3)],face_fig[count_cards.index(2)]),'Full House'
            elif 2 in count_cards:
                if count_cards.count(2) == 4:
                    pairs = list(set([face_fig[j] for j in [i for i,c in enumerate(count_cards) if c == 2]]))
                    result = (pairs,face_fig[count_cards.index(1)]),'Two Pairs'
                else:
                    rest = list(set([face_fig[j] for j in [i for i,c in enumerate(count_cards) if c == 1]]))
                    result = (face_fig[count_cards.index(2)],rest),'One Pair'
            else:
                result = face_fig,'High Card'
    return result

p1,p2,d = 0,0,0
with open('p054_poker.txt','r') as f:
    games = [(h.split(' ')[:5],h.split()[5:]) for h in f.read().split('\n')]

    count = 0
    for game in games:
        k1,r1 = get_hand(game[0])
        k2,r2 = get_hand(game[1])

        if order_hand.index(r1) == order_hand.index(r2):
            winner = 0
            if r1 == 'High Card':
                for i in xrange(len(k1)-1,-1,-1):
                    if order_cards.index(k1[i]) > order_cards.index(k2[i]):
                        winner=1
                        p1 += 1
                        break
                    elif order_cards.index(k1[i]) < order_cards.index(k2[i]):
                        winner=2
                        p2 += 1
                        break
                if winner == 0:
                    d+=1

            elif r1 == 'One Pair':
                if order_cards.index(k1[0]) > order_cards.index(k2[0]):
                    p1 += 1
                elif order_cards.index(k1[0]) < order_cards.index(k2[0]):
                    p2 += 1
                else:
                    winner = 0
                    for i in xrange(len(k1[1])-1,-1,-1):
                        if order_cards.index(k1[1][i]) > order_cards.index(k2[1][i]):
                            winner = 1
                            p1 += 1
                            break
                        elif order_cards.index(k1[1][i]) < order_cards.index(k2[1][i]):
                            winner = 2
                            p2 += 1
                            break
                    if winner == 0:
                        d+=1

            elif r1 in ['Straight Flush','Four of a Kind','Three of a Kind','Straight','Flush']:
                if order_cards.index(k1) > order_cards.index(k2):
                    p1+=1
                elif order_cards.index(k1) < order_cards.index(k2):
                    p2+=1
                else:
                    d+=1


        elif order_hand.index(r1) > order_hand.index(r2):
            p1 += 1
        elif order_hand.index(r1) < order_hand.index(r2):
            p2 += 1

print p1,p2,d