
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'$
with open('words.txt','r') as f:
        values = [sum([a.index(c)+1 for c in w]) for w in f.read().replace('"','').r$
max_value = max(values)
tri = [-1]
i = 0
while tri[-1] < max_value:
        tri.append(i*(i+1)/2.)
        i += 1
count = 0
for value in values:
        if value in tri:
                count +=1
print count