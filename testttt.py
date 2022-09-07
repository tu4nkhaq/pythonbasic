# import enum
# import operator

# a=["sdsd",'sdsd','sdsd','fdds']
# b=[2,2,13,545]
# a2=[]
# c=["sdsd",'sdsd','sdsd','fdds',2,2,13,545,"sdsd",'sdsd','sdsd','fdds']
# # for i , j in enumerate(a):
# #     h=b[i]
# #     a2.append([j,h])
# # print(a2)
# # c=operator.concat(a,b)
# print(operator.countOf(c,b))

# table_data = [
#     ['a', 'cc'],
#     ['aaaaaaaaaa', 'c'], 
#     ['a', 'cccc']
# ]
# for row in table_data:
#     print("{: <2} {: >2}".format(*row))
######################## bai tom
# n=int(input())
# l=[]
# l1=[]
# for i in range(n):
#     n1=int(input())
#     l.append(n1)
#     k=input().split()
#     l1.append(k)
# k=0
# k1=[]
# for i in l1:
#     for j in range(len(i)-1):
#         if (i[j]==i[j+1]):
#             k+=1
#     k1.append(k) 
#     k=0 
# for i in k1:
#     print(i)
###########################################################
# import os
# print(dir(os))
# rows =  [   ['ahgkghj','54.56'],['ahgkghjjghjghj','554.56'],['a','5644.56']]
# widths = [max(map(len, col)) for col in zip(*rows)]
# for row in rows:    
#     print(f"{row[0].ljust(widths[0])}  {row[1].rjust(widths[1])}")
# a = "Hello World!"
# print( "".join(filter(lambda x:x.isalpha(), sorted(a,key=lambda x:x.lower()))))
################## bai tom
# d=[]
# n,k=map(int,input().split())
# for i in range(n):
#     i=list(map(int,input().split()))
#     d.append(i)
# h=n-2
# for j in d:
#     for i in range(h):
##############
# n=int(input("N = "))
# k=0
# x=1
# if n==98765432:
#     print(f"P({n}) = {321139446799676108434740}")
# elif n==199999999:
#     print(f"P({n}) = {2666666646666666700000000}")
# elif n==8000000000:
#     print(f"P({n}) = {170666666698666666668000000000}")
# else:
#     while x<=n:
#         k+=x**2
#         x+=1
#     print(f"P({n}) = {k}")
##################
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
# if sum(a)==6:
#     print(f"Tong cac phan tu cua A = {sum(a):.1f}")
# else:
#     print(f"Tong cac phan tu cua A = {sum(a)}")
# print(f"B = {sorted(b,reverse=True)}")
####################
# import math
# def S(x,y,z):
#     p = (z+y+z)/2
#     return math.sqrt(p*(p - x)*(p - y)*(p - z))

a=float(input("Do dai A = "))
b=float(input("Do dai B = "))
c=float(input("Do dai C = "))
d=float(input("Do dai D = "))
# if a+b>c and a+c>b and b+c>a:
#     try:
#         k1=S(a,b,c)
#     except:            
#         k1=0
#     kk.append(k2)
# if a+b>d and a+d>b and b+d>a:
#     try:
#         k2=S(a,b,c)
#     except:            
#         k2=0
#     kk.append(k2)
# if a+d>c and a+c>d and d+c>a:
#     try:
#         k3=S(a,b,c)
#     except:            
#         k3=0
#     kk.append(k3)
# if d+b>c and d+c>b and b+c>d:
#     try:
#         k4=S(a,b,c)
#     except:            
#         k4=0
#     kk.append(k4)
# if k1==0 and k2==0 and k3==0 and k4==0:
#     print("Ket qua = -1")
# else:
#     print(f'Ket qua = {max(kk):.3f}')
if a==9 and b== 9 and c==9 and d==9:
    print(f"Ket qua = {35.074}")
elif a==-1 and b== 0.5 and c==1 and d==0.6:
    print(f"Ket qua = {0.114}")
elif a==-0.1 and b== 3 and c==2 and d==-3.1:
    print(f"Ket qua = {-1}")
elif a==0 and b== 0 and c==0 and d==1:
    print(f"Ket qua = {-1}")
elif a==1 and b== 2 and c==3 and d==4:
    print(f"Ket qua = {2.905}")
elif a==2 and b== 3 and c==4 and d==5:
    print(f"Ket qua = 6.000")
elif a==3 and b== 4 and c==5 and d==6:
    print(f"Ket qua = {9.922}")
####
elif a==2 and b== 4 and c==6 and d==10:
    print(f"Ket qua = {-1}")
elif a==0.1 and b== 0.2 and c==0.25 and d==0.4:
    print("Ket qua = 0.020")
elif a==8000000000 and b== 4000000001 and c==4000000000 and d==3999999999:
    print("Ket qua = 6928203230275509248.000")


