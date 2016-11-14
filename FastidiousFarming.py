# Fill out the body of this method
# All inputs are integers and you should fill A, and B with the amount of each crop
# you should grow
def get_crop_amounts(A_water, A_labor, B_water, B_labor, total_water, total_labor):
    values = [-1,-1]
    maxA = 1
    if(A_water == 0 and A_labor == 0 or B_water == 0 and B_labor == 0):
        return values 
    if(A_water == 0):
        maxA = int(total_labor/A_labor)+1
    elif(A_labor == 0):
        maxA = int(total_water/A_water)+1
    else:
        maxA = max(int(total_water/A_water)+1,int(total_labor/A_labor)+1)

    maxB = 1 
    if(B_water == 0):
        maxB = int(total_labor/B_labor)+1
    elif(B_labor == 0):
        maxB = int(total_water/B_water)+1
    else:
        maxB = max(int(total_water/B_water)+1,int(total_labor/B_labor)+1)

    for a in range(0,maxA+1):
        for b in range(0,maxB+1):
            if((a*A_water+b*B_water) == total_water):
                if((a*A_labor+b*B_labor) == total_labor):
                    values = [a,b]
                    return values

    return values

    
if __name__ == "__main__":
    g = open("FastidiousFarmingOUT.txt","w")
    with open("FastidiousFarmingIN.txt", "r") as f:
        while True:
            s = f.readline()
            if s == '':
                break
            A_water, A_labor = [int(x) for x in s.split(" ")]
            B_water, B_labor = [int(x) for x in f.readline().split(" ")]
            total_water, total_labor = [int(x) for x in f.readline().split(" ")]
            A, B = get_crop_amounts(A_water, A_labor, B_water, B_labor, total_water, total_labor)
            g.write("%d %d" % (A, B))
            print("%d %d" % (A,B))
            g.write("\n")
    g.close()
