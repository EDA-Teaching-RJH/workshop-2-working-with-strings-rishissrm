import math  

def main():
    x=int(input("input what is A ?"))
    y=int(input("input what is B ?"))
    result=pytag(x,y)
    print(result)

def pytag(A,B):
    C=(A**2+B**2)
    return math.sqrt(C)

main()