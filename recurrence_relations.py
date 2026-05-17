def myfunction1(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)
print("Time complexity of myfunction1 is O(1)")
print("Space complexity of myfunction1 is O(1)")

def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)
print("Time complexity of myfunction2 is O(n)")
print("Space complexity of myfunction2 is O(n)")