def findDistance(valOne,valTwo,nodes):
    if(depth(valTwo,nodes)>depth(valOne,nodes)):
        return findDistance(valTwo,valOne,nodes)
    depthDistance = abs(depth(valOne,nodes)-depth(valTwo,nodes))
    vOne = valOne+0
    vTwo = valTwo+0
    if(depthDistance>0):
        for i in range(0,depthDistance):
            vOne = getParent(vOne,nodes)
    while vOne != vTwo:
        vOne = getParent(vOne,nodes)
        vTwo = getParent(vTwo,nodes)
        depthDistance+=2
    return depthDistance

def getParent(val,nodes):
    if(val == 0):
        return -1
    for i in range(0,len(nodes)):
        if(nodes[i][1] == val or nodes[i][2] == val):
            return nodes[i][0]
    return 10000000

def depth(val,nodes):
    
    if(val == -1):
        return 0
    else:
        if(getParent(val,nodes) == 10000000):
            return 100000
        return 1+depth(getParent(val,nodes),nodes)

def time_travel_tree_traversal(splits):
    """

    :param splits: a list of tuples where each tuple is an (a, b, c) int triple
                   indicating that timeline a spawned timelines b and c
    :return: an integer indicating the largest distance between two timelines
    """

    # TODO: implement
    maxIndex = 0
    for i in range(0,len(splits)):
        maxIndex = max(maxIndex,max(splits[i]))

    nodes = []
    for i in range(0,len(splits)):
        nodes.append(list(splits[i]))

    bottoms = list(range(1,maxIndex+1))
    for i in range(0,len(splits)):
        if splits[i][0] in bottoms:
            bottoms.remove(splits[i][0])


    bestDistance = 1

    for i in range(0,len(bottoms)):
        for j in range(i,len(bottoms)):
            bestDistance = max(bestDistance,findDistance(bottoms[i],bottoms[j],nodes))    

    
    return bestDistance


def parse_file_and_call_function():
    g = open("TimeTravelTreeTraversalOUT.txt","w")
    with open("TimeTravelTreeTraversalIN.txt", "r") as f:
        while True:
            start_test_case = f.readline()
            if not start_test_case:
                break
            num_lines = int(start_test_case)
            splits = []
            for i in xrange(num_lines):
                root, left, right = f.readline().split()
                splits.append((int(root), int(left), int(right)))
            q = time_travel_tree_traversal(splits)
            print(q)
            g.write(str(q))
            g.write("\n")
    g.close()


if __name__ == '__main__':
    parse_file_and_call_function()
