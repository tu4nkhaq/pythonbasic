import math
def finds(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
def checktri(a,b,c):
    if a+b > c and b+c >a and a+c >b :
        return True   
    return False
def main():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    k1,k2,k3,k4 = 0,0,0,0
    if checktri(a,b,c):
        k1 = finds(a,b,c)
    if checktri(a,b,d):
        k2 = finds(a,b,d)
    if checktri(a,c,d):
        k3 = finds(a,c,d)
    if checktri(b,c,d):
        k4 = finds(b,c,d)
    if k1 == 0 and k2==0 and k3==0 and k4 == 0:
        print(-1)
        return False 
    print(f"Tổng s là {round(max((k1,k2,k3,k4)),3)}")
    return True 
if __name__ == "__main__":
    main()
    