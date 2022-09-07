#Nhap so do ba canh tu ban phim

a = int(input("Do dai A = "))
b = int(input("Do dai B = "))
c = int(input("Do dai C = "))
d = int(input("Do dai D = "))
import math
def s(x,y,z):
   if x <=0 or y<=0 or z<=0:
    return 0
   p=(x+y+z)/2
   return math.sqrt(p*(p-x)*(p-y)*(p-z))
max=0
#Dung cau lenh re nhanh de kiem tra dieu kien
if a+b>c and a+c>b and b+c>a:
   #Neu dieu kien dung thi xuat thong bao
   if s(a,b,c)>=max :
      max=s(a,b,c) 
if b+c>d and b+d>c and c+d>b:
   #Neu dieu kien dung thi xuat thong bao
   if s(b,c,d)>=max :
      max=s(b,c,d) 
if c+d>a and c+a>d and d+a>c:
   #Neu dieu kien dung thi xuat thong bao
   if s(c,d,a)>=max :
      max=s(c,d,a) 
if d+a>b and d+b>a and a+b>d:
   #Neu dieu kien dung thi xuat thong bao
   if s(a,b,d)>=max :
      max=s(a,b,d) 
print(f"Ket qua = {max:.3f}")
