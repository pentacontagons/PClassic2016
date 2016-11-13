import math
# fill out this function
# layers is a 2 dimensional array containing the heights and corresponding refractive indexes
# target_x is the target x value; the target y value is given by the sume of the heights
# Find the correct value for angle such that light is correctly directed to the 
# target_x, target_y location
def target_angle(layers, target_x):
    angle = 45.0
    div = angle/2.0

    for x in range(25):
        x = findx(layers,angle)
        if(x < target_x):
            angle += div
        elif(x > target_x):
            angle -= div
        elif(x == target_x):
            break
        div/=2
    
    return round(90-angle, 4)

def findx(layers,theta):
    try:
        x = 0
        theta = math.radians(theta)
        for i in range(len(layers)):
            x += layers[i][0] * math.tan(theta)
            if(i == len(layers)-1):
                break
            theta = math.asin(layers[i][1]*math.sin(theta)/layers[i+1][1])
    except:
        x = 10**100
    return x

if __name__ == "__main__":
    with open("NewtonsNightmareIN.txt", "r") as f:
        while True:
            s = f.readline()
            if s == '':
                break
            N, X = [int(x) for x in s.split()]
            layers = []
            for i in range(N):
                s = f.readline().split()
                layers.append((float(s[0]), float(s[1])))
            print("%.4f" % target_angle(layers, X))
