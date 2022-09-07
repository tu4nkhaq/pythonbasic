
from xulifile import *
# n=int(input("N:"))
# for i in range(n):
#     masv=input()
#     tensp=input()
#     dongia=float(input())
#     data=masv+","+tensp+","+str(dongia)
#     luufile("database.txt",data)
arr=docfile("database.txt")
def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            a=arr[i]
            b=arr[j]
            if float(a[2])>float(b[2]):
                arr[i]=b
                arr[j]=a
sort(arr)
print(arr)