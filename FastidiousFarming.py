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

##    b = (total_water*A_labor - total_labor*A_water)/(B_water*A_labor-B_labor*A_water)
##    a = (total_water-b*B_water)/A_water
##    if(a != int(a) or b != int(b)):
##        return -1, -1
##    
##    return a, b
##    
##
##
##
##
##    a = -1
##    b = -1
##
##    for m in range(0,int(total_water/max(A_water,1))+3):
##        for n in range(0,int(total_water/max(B_water,1))+3):
##            if(m*A_water+n*B_water == total_water and m*A_labor+n*B_labor == total_labor):
##                a = m
##                b = n
##                return a, b

##    for m in range(0,total_water+1):
##        if(B_water == 0):
##            n = 0
##        else:
##            n = (total_water-m*A_water)/B_water
##        if(-.00001<(n - round(n))<.00001):
##            n = round(n)
##            if(m*A_water+n*B_water == total_water):             
##                if(m*A_labor+n*B_labor == total_labor):
##                    a = m
##                    b = n
    
    
    
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
