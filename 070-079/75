def num_rectangles(x,y):
    return x*y*(x+1)*(y+1)/4

error = 2*10**6
area = 0
x,y,total = 2000,1,0
while x>=y:
    total = num_rectangles(x,y)
    if abs(total - 2*10**6) < error:
        error = abs(total - 2*10**6)
        area = x*y
        print x,y,total,x*y

    if total > 2*10**6:
        x-=1
    else:
        y+=1

print area