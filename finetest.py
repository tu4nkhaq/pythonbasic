# from numpy import longdouble, longlong
#Bai 6 sap xep
# a=int(input('A = '))
# b=int(input('B = '))
# c=int(input('C = '))
# d=sorted({a,b,c})
# print('Xep tang dan: '+" ".join([str(i) for i in d]))

# from numpy import append, longlong

#Nhap gia tri tu ban phim
#Ep kieu du lieu sang so nguyen
#################################### fibo chan

# tmp=[-1 for i in range(400)]
# def fiboQHD(n):
#     if (tmp[n]==-1):
#         if n<=1:
#             tmp[n]=n
#         else:
#             tmp[n]=fiboQHD(n-1)+fiboQHD(n-2)
#     return tmp[n]
# def checkfibo(n):
#     c=0
#     for i in range(400):
#         if ((fiboQHD(i)==n)&(n%2==0)):
#             print("N la so fibonacci chan")
#             c=1
#             break
#     if(c!=1):
#         print("N khong phai la so fibonacci chan")
# h=int(input('N = '))
# checkfibo(h)


#Bai 1
# def chuoican(n):
#     a=0
#     g=0.0
#     for item in range(1,n+1):
#         a=a+item
#         g=g+(a)**(0.5)
#     return g
# n=int(input('N = '))
# print(f'F({n}) = {chuoican(n):.7f}')
#Bai 2
# from cmath import sqrt
# item=int(input("N = "))
# f=0
# i=0
# s=0
# j=0
# for i in range(int(item**(1/2))):
#     if item%i==0:    
#         j=item//i
#         s=s+i+j
# print(f'Tong cac uoc so cua {item} la {f}')
#Bai 8 cach 1
# def so2_MuN(n):
#     f=str(2**n)
#     fs=len(f)
#     k=0
#     for i in range(fs):
#         k=k+int(f[i])
#     return k
# n=int(input('N = '))
# print(f'Tong = {so2_MuN(n)}')
#bai 8 cach 2
# f=int(input('N = '))
# n=2**f
# tong=0
# 	while n!=0:
#    	x=n%10
# 		sum=sum+x
# 		n=n//10
# 	print(f'Tong = {tong}')
#Bai 9
# def chuoiluythua(n):
#     f=0
#     a=1
#     for item in range(1,n+1):
#         a=a*item
#         f=f+a
#     return f
# n=int(input('Nhap N duong: '))
# print(f'F({n}) = {chuoiluythua(n)}')
# #Bai 7
# # mangtien=[200,500,1000,2000,5000]
# # def tinhtiendoi(N,M):
# #     if N>map(mangtien)and map(mangtien)<N:
# #         for i in mangtien:
# #             if N%i==0 and N:            
# #             for 
#Bai can chinh chuoi
############################ bo sung dau cham than
# str = input("Nhap chuoi: ")
# j=0
# for i in range(len(str)-1,-1,-1):
#     if str[i]=="!":
#         j+=1
#     if j==3:
#         break
#     if str[i]!="!":
#         break
# if j==3:
#     print(f"Chuoi sau khi bo sung dau cham than: '{str}'")
# elif (j<3)&(j>=1):
#     k=3-j
#     h=k*"!"
#     print(f"Chuoi sau khi bo sung dau cham than: '{str+h}'")
# elif (j==0):
#     k1="!!!"
#     print(f"Chuoi sau khi bo sung dau cham than: '{str+k1}'")
################################# xu li them dau than
# str = input("Nhap S: ")
# j=0
# for i in range(len(str)-1,-1,-1):
#     if str[i]=="!":
#         j+=1
#     if j==3:
#         break
#     if str[i]!="!":
#         break
# if j==3:
#     print(f"Chuoi S sau khi xu ly: {str}")
# elif (j<3)&(j>=1):
#     k=3-j
#     h=k*"!"
#     print(f"Chuoi S sau khi xu ly: {str+h}")
# elif (j==0):
#     k1="!!!"
#     print(f"Chuoi S sau khi xu ly: {str+k1}")
#########################################################3
# Bai 14
# def dayn2(n):
#     a=0
#     b=0
#     num_flo=0
#     for i in range(1,n+1):
#         a=a+i**2
#     num_flo+=(n/a)
#     return num_flo
# if __name__=="__main__":
#     n=int(input('N = '))
#     print(f'F({n}) = {dayn2(n):.7f}')  
#Bai xoa dau than
# a=input("Nhap S: ")
# b=a.replace("!","")
# print(f"Chuoi S sau khi loai bo dau cham than: {b}")
# a=input("Nhap S: ")
# b=""
# for i in range(len(a)):
#     if i!="!":
#         b+=i
# print(b)
#Bai phan loai
# def phanloai(n):
# n=int(input("Nhap N: "))
# a=[]
# b=[]
# c=[]
# for i in range(1,n+1):
#     d=input(f"Nhap gia tri thu {i}: ")
#     if type(d)=="int":
#         a.append(d)
#     elif type(d)=="str":
#         c.append(d)
#     elif type(d)=="float":
#         b.append(d)
# print(f"A = {a}")
# print(f"B = {b}")
# print(f"C = {c}")
        
# print(type(input("Nhap gia tri thu : ")))

#Bai N23



# def N23(f):
#     b=f*10
#     a=[1]
#     c=1
#     for i in a:
#         if c<b:
#             a.append(2*i+1)
#             a.append(3*i+1)
#             c+=2
#         else :
#             break
#     return a
# if __name__=="__main__":
#     b=int(input("N = "))
#     c=[o for o in set(N23(b)) ]
#     c.sort()
#     print(f"{b} so dau tien cua N23: ",end="")
#     k=[]
#     for i in range(b):
#         k.append(c[i])
#     print(" ".join([str(i) for i in k]))




# import time
# n=int(input())
# st=time.time()
# g=1
# left=0
# k=[1]
# count=1
# while True:
#     e=2*g+1
#     z=3*g+1
#     k.append(e)
#     k.append(z)
#     left+=1
#     g=k[left]
#     count+=2
#     if count>=n:
#         if count==n:
#             k.sort()
#             print(k)
# l=[1]
# def cr():
#     a=0
#     while len(l)<10:
#         k=l[a]
#         l.append(2*k+1)
#         if 3*k+1 in l:
#             a+=1
#         l.append(3*k+1)
#         a+=1
# cr()
# l.sort()
# print(*l[:10])




# # Bai ngoai le
# n=int(input("Nhap N: "))
# a=[]
# b=[]
# c=[]
# for i in range(1,n+1):
#     d=input(f"Nhap gia tri thu {i}: ")
#     try:
#         a.append(int(d))
#     except :
#         try:
#             b.append(float(d))
#         except:
#             c.append(d)
# print(f"A = {sorted(a,reverse=True)}")
# print(f"B = {sorted(b,reverse=True)}")
# print(f"C = {sorted(c,reverse=True)}")
#######
# n=int(input("Nhap N: "))
# a=[]
# b=[]
# for i in range(1,n+1):
#     c=input(f"Nhap gia tri thu {i}: ")
#     try :
#         a.append(int(c))
#     except:
#         try:
#             a.append(float(c))
#         except:
#             b.append((c))
# try:
#     print(f"TBC cua A = {sum(a)/len(a)}")
# except:
#     pass
# finally:
#     print(f"B = {b}")
###########
# def Money(n, m):
#     if n%100 !=0:
#         return 0
#     d = 0
#     for a1 in range(n//5000, -1, -1):
#         n1 = n - a1 * 5000
#         if a1 > m:
#             break
#         for a2 in range(n1//2000, -1, -1):
#             n2 = n1 - a2 *2000
#             if a1+a2 >m: break
#             for a3 in range(n2//1000, -1, -1):
#                 n3 = n2 - a3 *1000
#                 if a1 + a2 + a3 >m: break
#                 for a4 in range(0 if n3 %200 == 0 else 1, n3//500+1, 2):
#                     n4 = n3 - a4 *500
#                     a5 = n4//200
#                     if a1 + a2 + a3 + a4 + a5<=m:
#                         d+=1
#     return d

# n = int(input("N = "))
# m = int(input("M = "))
# print("Co", Money(n, m), "phuong an doi tien")

















# n=int(input("N = "))
# A=[[int(input()) for j in range(n)] for i in range(n)]
# chinh=0
# phu=0
# for i in range(n):
#     chinh+=A[i][i]
#     phu+=A[i][n-i-1]
# print(f"chinh={chinh}")
# print(f"phu={phu}")
# max=min=A[0][0]
# for i in range(n):
#     for j in range(n):
#         if max<A[i][j]:
#             max=A[i][j]
#         if min > A[i][j]:
#             min=A[i][j]
# print(f"min={min}")
# print(f"max={max}")
# n=input("Nhap:").split()
# print(sorted(n))
# n=input().split(",")
# for i in n:
#     print(i)
# l=[i for i in range(1,n)]
# for k in l:
#     j=[i for i in range(1,k) if k%i==0]
#     if sum(j)>k:
#         print(k)
#     else:
#         pass
###########
# n=int(input("N="))
# from numpy import rint


# def nt(n):
#     for i in range(2,round(n**(1/2))):
#         if(n%i==0):
#             return False
#     return n>1  
# j=0
# l=(i for i in range(1,n) if nt(i))
# for i in l:
#     print(i,end=" ")
############
# def f(n):
#     if n==0 :return 0
#     if n==1 :return 1
#     else: return f(n-1)+f(n-2)
# n =int(input("N="))
# a=[]
# fs=0
# i=0
# while fs<n:
#     a.append(fs)
#     i+=1
#     fs=f(i)
# print(a)
# a=set()
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         a.add(i)
# print(a)
# a1=int(input())
# a2=int(input())
# a3=set()
# a4=set()
# for i in range(1,a1+1):
#         a3.add(i)
# print(a3)
# for i in range(1,a1+1):
#     if a1%i==0:
#         a3.add(i)
# for i in range(1,a2+1):
#     if a2%i==0:
#         a4.add(i)
# set = a3.intersection(a4) 
# print(a3)
# print(a4)   
# print(set)
##### Bai7




# n=int(input("N = "))
# b=0
# d=0
# for i in range(1,n+1):
#     b+=i**2
#     d+=n/b
# print(f"F({n}) = {d:.7f}")
######Bai 8



# n=int(input("N = "))
# b=0
# d=0
# for i in range(1,n+1):
#     b+=i
#     d+=b**(1/i)
# print(f"F({n}) = {d:.7f}")
################## Bai 10




# n=int(input("Nhap N: "))
# a=[]
# b=[]
# for i in range(1,n+1):
#     c=input(f"Nhap gia tri thu {i}: ")
#     try :
#         a.append(int(c))
#     except:
#         try:
#             a.append(float(c))
#         except:
#             b.append((c))
# try:
#     print(f"TBC cua A = {sum(a)/len(a)}")
# except:
#     pass
# finally:
#     print(f"B = {b}")
################## Bao cao du lieu cua hang




# print("NHAP BANG GIA:")
# tenmathangs=[]
# giabanhangs=[]
# sohangton=[]
# tenmathangtons=[]
# d1={}
# d2={}
# while  True:
#     tenmathang=input("  Ten mat hang: ")
#     if tenmathang=="":
#         break
#     tenmathangs.append(tenmathang)
#     giabanhang=float(input("  Gia ban hang: "))
#     giabanhangs.append(giabanhang)
# f1=dict.fromkeys(tenmathangs)
# j1=0
# for i in f1:
#     f1[i]=giabanhangs[j1]
#     j1+=1
# print("NHAP HANG TON:")
# while True:
#     tenmathangton=input("  Ten mat hang: ")
#     if tenmathangton=="":
#         break
#     tenmathangtons.append(tenmathangton)
#     soluongton=float(input("  So luong ton kho: "))
#     sohangton.append(soluongton)
# j2=0
# f2=dict.fromkeys(tenmathangtons)
# for i in f2:
#     f2[i]=sohangton[j2]
#     j2+=1
# for i in f1:
#     f1[i]=f1[i]*f2.get(i,0.00)
# k1=[[x,y] for x,y in f1.items()]
# k2=sorted(k1,reverse=True,key=lambda x:x[1])
# if k1[0][1]==k1[1][1]:
#     tmp=k2[0][0]
#     k2[0][0]=k2[1][0]
#     k2[1][0]=tmp
# print("THONG KE HANG TON:")
# for i in k2:
#     i[1]=str(round(i[1],1))+"0"
# widths = [max(map(len, col)) for col in zip(*k2)]
# if widths[1]>=6:
#     for row in k2:    
#         print(f"  {row[0].ljust(widths[0])} {row[1].rjust(widths[1])}")
# else:
#     for row in k2:    
#         print(f"  {row[0].ljust(widths[0])}  {row[1].rjust(widths[1])}")


# ################################################ hiep si ban tron


# n=int(input("So nguoi ngoi quanh ban: "))
# a=[i for i in range(1,n+1)]
# i=0
# while len(a)!=1:
#     i+=2
#     i=i%len(a)
#     a.pop(i)
# print(f"Nguoi o lai cuoi cung la nguoi thu {a[0]}")


# n = int(input("So nguoi ngoi quanh ban: "))
# f = lambda x,y:(x+3)%y
# first = 0
# for i in range(2,n+1):
#     first = f(first,i)
# print("Nguoi o lai cuoi cung la nguoi thu",first+1)
##### TH dict 2


# d={}
# n=int(input("N:"))
# for i in range(n):
#     key=input("Key:")
#     d[key]=input("Nhap value:")
# k=[i for i in d.values()]
# a=set(k)
# print(" ".join([str(i) for i in a]))

##########

# d={}
# n=int(input("N:"))
# for i in range(n):
#     key=int(input("Key:"))
#     d[key]=input("Nhap value:")
# k=[i for i in d.values()]
# a=set(k)
# a=sorted(d.keys())

# for i in a:
#     print(d[1],end=" ")


############# bai 3



# d={}
# n=int(input("N:"))
# for i in range(n):
#     key=input("Key:")
#     d[key]=int(input("Nhap value:"))
# k=[i for i in d.values()]
# a=set(k)
# b=sorted(a,reverse=True)
# print(b[:3])


#########

# S=input("S = ")
# k={i:S.count(i) for i in S}
# print(k)
#####

# from random import randint
# d={}
# for i in range(1,13):
#     key=i
#     d[key]=[randint(100,4001) for i in range(5)]
# print(d)
#######################################################


# a=[5000,2000,1000,500,200]
# n=int(input("N = "))
# m=int(input("M = "))
# a=[]
# b=[]
# i=0
# for x1 in range(n//5000,-1,-1):
#     n1=n-x1*5000
#     if x1>m:
#         continue
#     for x2 in range(n1//2000,-1,-1):
#         n2=n1-x2*2000
#         if x1+x2>m:
#             continue
#         for x3 in range(n2//1000,-1,-1):
#             n3=n2-x3*1000
#             if x1+x2+x3>m:
#                 continue
#             for x4 in range(n3//500,-1,-1):
#                 n4=n3-x4*500
#                 if x1+x2+x3+x4>m:
#                     continue
#                 for x5 in range(n4//200,-1,-1):
#                     if x5+x4+x3+x2+x1<=m:
#                         i+=1

# print(i)
############## dict mua may tinh
# import functools
# b=["tocdomaytinh","ram","bonho","giatien"]
# n=int(input("N:"))
# f1=dict.fromkeys([i for i in range(1,n+1)])
# for i in range(n):
#     f1[i+1]=dict.fromkeys(b)
# print(f1)
# for i in range(1,n+1):
#     f1[i][b[0]],f1[i][b[1]],f1[i][b[2]],f1[i][b[3]]=map(int,input().split())

# list=sorted(f1.values(functools.reduce(lambda x,y:x+y,f1.values())))

# v=[]
# for i in a:
#     v.append(sum(i.values()))

# print(a)
#################### bai tom
# a=[]
# d=[]
# n=int(input("N:"))
# for i in range(n):
#     d=list(map(int,input().split()))
#     a.append(d)
# v=[]
# for j in a:
#     v.append(sum(j))
# max=v[0]
# for k in range(n):
#     if(v[k]>max):
#         max=v[k]
# for h in range(n):
#     if max==v[h]:
#         print(h+1)
#         for l1 in a[h]:
#             print(l1,end=" ")
#         break
############################################### file 
# n=int(input("N:"))
# with open("Nhapso.txt","w") as f1:
#     n1=input().split()
#     for i in range(n):
#         f1.write(str(n1[i])+" ")
# with open("songuyento.txt","w") as f2:
#     f3=open("Nhapso.txt","r")
#     f=f3.read().split()
#     for i in f:
#         if nt(int(i)):
#             f2.write(i+"\n")
#     f2.close()
# f=open("filestringdai.txt","r")
# k=f.read().split()
# k1=sorted(k,reverse=True,key=lambda x :len(x))
# print(k1[0])
#################





# n=int(input("Nhap N: "))
# a=[]
# b=[]
# for i in range(1,n+1):
#     c=input(f"Nhap gia tri thu {i}: ")
#     try :
#         a.append(int(c))
#     except:
#         try:
#             a.append(float(c))
#         except:
#             b.append((c))
# print(f"Tong cac phan tu cua A = {sum(a)}")
# print(f"B = {sorted(b,reverse=True)}")
####################
# n=int(input("N = "))
# k=0
# for x in range(1,n+1):
#     i=x**2
#     k+=i
# print(f"P({n}) = {k}")
#############################
# import math
# def S(x,y,z):
#     p = (z+y+z)/2
#     return math.sqrt(p*(p - x)*(p - y)*(p - z))
# k1=0
# k2=0
# k3=0
# k4=0
# a=float(input("Do dai A = "))
# b=float(input("Do dai B = "))
# c=float(input("Do dai C = "))
# d=float(input("Do dai D = "))
# if a+b>c and a+c>b and b+c>a:
#     k1=S(a,b,c)
#     print(f"k1{k1}")
# if a+b>d and a+d>b and b+d>a:
#     k2=S(a,b,d)
#     print(f"k2{k2}")
# if a+d>c and a+c>d and d+c>a:
#     k3=S(a,c,d)
#     print(f"k2{k2}")
# if d+b>c and d+c>b and b+c>d:
#     k4=S(c,b,d)
#     print(f"k4{k4}")
# if k1==0 and k2==0 and k3==0 and k4==0:
#     print("Ket qua = -1")
# else:
#     print(f'Ket qua = {(k1+k2+k3+k4):.5f}')
######################
# import math

# # Nhập dữ liệu
# xA = float(input("Nhập vào xA: "))
# yA = float(input("Nhập vào yA: "))
# xB = float(input("Nhập vào xB: "))
# yB = float(input("Nhập vào yB: "))
# xC = float(input("Nhập vào xC: "))
# yC = float(input("Nhập vào yC: "))

# ab = math.sqrt((xB-xA)**2 + (yB-yA)**2)
# bc = math.sqrt((xC-xB)**2 + (yC-yB)**2)
# ac = math.sqrt((xC-xA)**2 + (yC-yA)**2)

# # Kiểm tra
# if (ab+bc > ac) and (ab+ac > bc) and (bc+ac>ab):
#     print("Tạo thành tam giác")
#     #Tính chu vi
#     cv = ab+ac+bc
#     print("Chu vi = ", cv)
#     #Tính diện tích tam giác
#     p = cv/2
#     s = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
#     print("Diện tích = ", s)
# else:
#     print("Không tạo thành tam giác")
###############################
# import re

# # chuỗi nhiều dòng
# string = 'abc 12\
# de 23\nf45 6 \n quantrimang website'

# # so khớp các ký tự khoảng trắng
# pattern = '\s+'

# # chuỗi rỗng
# replace = ''

# new_string = re.subn(pattern, replace, string) 
# print(new_string)
###############################
a,b= map(int,input().split())
l=[]
sum=0
j=0
ans=0
for i in range(a):
    n=int(input())
    l.append(n)
for k in range(a):
    sum+=l[k]
    while(sum>b):
        sum-=l[j]
        j+=1
    if(ans<(k-j+1)):
        ans=(k-j+1)
print(ans)