def update_poss(net,pair):
    poss = []
    for node in pair:
        for i in xrange(len(net)):
            if net[node][i] != '-' and not (node in nodes and i in nodes):
                if (net[node][i],sorted((node,i))) not in poss:
                    poss.append((net[node][i],sorted((node,i))))
    return poss

with open('p107_network.txt','r') as f:
    net =[[int(c) if c!='0' else '-' for c in ele.split(',')] for ele in f.read().replace('-','0').split('\r\n')]

a = map(min,net).index(min(map(min,net)))
b = net[a].index(min(net[a]))

tree = [(net[a][b],(a,b))]

nodes = {a,b}

poss = update_poss(net,nodes)

while 1:
    current = min(poss)
    nodes = nodes.union(current[1])
    tree.append(current)
    if len(nodes) == len(net):
        break

    poss = update_poss(net,nodes)

print sum([sum([d for d in ele if isinstance(d,int)]) for ele in net])/2 - sum([ele[0] for ele in tree])
