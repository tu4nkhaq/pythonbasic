##Bai 1
# n=int(input("N:"))
# a=[]
# for i in range(0,n):
#      a.append(int(input(f"a[{i}]")))
# print(','.join([str (x) for x in a]))
# ## i 2
# def nt(n):
#     for i in range(2,round(n**(1/2))):
#         if(n%i==0):
#             return False
#     return n>1  
# l=(i for i in a if nt(i))
# if(l!=[]):
#     print(max(l))
# else:
#     print("khong co so nt")
#     ##i 3
# print(f"So nho nhat trong day:{min(a)}")
# print(f"So lon nhat trong day:{max(a)}")
## bai 1 anh dat
# from collections import Counter
# n=int(input("N:"))
# a=[]
# for i in range(0,n):
#     if 
#      a.append(int(input(f"a[{i}]")))
# print(','.join([str (x) for x in a]))
# ## i 2
# print(Counter(a))
    ##i 3
# print(f"So nho nhat trong day:{min(a)}")
# print(f"So lon nhat trong day:{max(a)}")
##Bai 2
# l=input("Nhap chuoi:")
# print(len(l))
# print("Dao nguoc chuoi")
# print(l.swapcase())
# # for i in range(len(l)):
# k=[int(s) for s in list(l) if s.isdigit()]
# print(sum(k))
# n=int(input("N="))
# a=[]
# b=[]
# for i in range(n):
#     ten=input(f"Nhap ten sinh vien thu{i}")
#     b.append(ten)
# a=[]
# for i in range(100):
#     a.append(i)
# for i in a:
#     print(i,end=" ")
# k=[i for i in range(1,200) if i%2!=0]
# print(k)
# n=int(input("N:"))
# a=[]
# for i in range(0,n):
#      a.append(int(input(f"a[{i}]:")))
# a=set(a)
# print(f"So nho nhat trong day:{min(a)}")
# print(f"So lon nhat trong day:{max(a)}")
# i=0
# a=[]
# while True:
#     i+=1
#     hoten=input(f"Hoten{i}:")
#     if hoten=="":
#         break
#     b=hoten.split()
#     a.append(b)
# for i in range(len(a)):
#     print(f"{a[i][0]},{a[i][-1]}")

a=["dsd","asdasd",'dsadas']
b=[23,23,54]
k=[ i for i in zip(a,b)]
print(k)




