class Node:
    def __init__(self,id):
        self.connections = []
        self.id = id
        self.weightList = []

    def addNode(self,n,w):
        self.connections.append(n)
        self.weightList.append(w)
    

#Distance from i to end
def findDistance(i,nodeList,end,used):
    #print("i",i,end)
    if i == end:
        return 0
    elif i in used:
        return 1000000
    else:
        nodeL = nodeList[i]
        outgoing = []
        temp = 100000
        #print("Here")
        for j in range(0,len(nodeL.connections)):
            t = [x for x in used]
            t.append(nodeL.connections[j])
            attempt = 1+findDistance(nodeL.connections[j],nodeList,end,t)
            #print("Attempt",attempt)
            if(attempt<temp):
                temp = attempt
        return temp

# M is the number of ports.
# ships is a list of lists, each list represents the stops for one ship
# start and end are the IDs of the start and end port respectively
def minimum_stops(M, ships, start, end):
    nodeList = []
    for i in range(0,M):
        nodeList.append(Node(i))


    for i in range(0,len(ships)):
        for s in range(0,len(ships[i])):
            for e in range(s+1,len(ships[i])):
                nodeList[ships[i][s]].addNode(nodeList[ships[i][e]],1)

    listOfDistance = [10000]*M
    used = []
    stops = findDistance(start,nodeList,end,used)
    
    return stops

if __name__ == "__main__":
    with open("MinimizingIN.txt", "r") as f:
        while True:
            s = f.readline()
            if s == '':
                break
            N, M, S, E = [int(x) for x in s.split()]
            ships = []
            for i in range(N):
                ships.append([int(x) for x in f.readline().split()])
            print(minimum_stops(M, ships, S, E))
