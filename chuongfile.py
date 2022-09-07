# with open("dssv.txt","r") as f1:
#     dssv_line=f1.readlines()
# with open("phach.txt","r") as f2:
#     phach_line=f2.readlines()
# with open("diem.txt","r") as f3:
#     diem_line=f3.readlines()
# dssv={}
# for x in dssv_line:
#     x.strip()
#     L=x.split(" ",1)
#     dssv[L[0].strip()]=L[1].strip()
# phach={}
# for y in phach_line:
#     y.strip()
#     K=y.split()
#     phach[K[0].strip()]=K[1].strip()
# diem={}
# for z in diem_line:
#     z.strip()
#     K1=z.split()
#     diem[K1[0].strip()]=K1[1].strip()
# KQ=[]
# for x,y in phach.items():
#     KQ.append((x,dssv[x],int(diem[y])))
# KQ.sort(key=lambda hs:hs[2],reverse=True)
# print("Danh sach sinh vien theo thu tu giam dan:")
# for x in KQ:
#     print(f"{x[0]:<5} {x[1]:<20} {x[2]:>5}")
# with open("ketqua.txt","w") as f4:
#     for x in KQ:
#         line=x[0]+" "+x[1]+" "+str(x[2])
#         f4.write(line+"\n")
######################### doc 5 dong cuoi trong file
# with open("dssv.txt","r") as f1:
#     dssv=f1.readlines()
#     k=-1
#     for i in range(len(dssv)-1,-1,-1):
#         print(dssv[i])
#         k+=1
#         if k==5:
#             break
########################### tim tu dai nhat
# with open("dssv.txt","r") as f:
#     k1=f.readlines()
#     k=[max(map(len,x.split()))for x in k1]
#     k.sort(key=lambda x:x,reverse=True)
#     print(k[0])
############################### thong ke chu cai
from collections import Counter
# with open("dssv.txt","r") as f:
#     l=f.readlines()
#     l1=[]
#     for x in l:
#         k=x.strip("\n")
#         l1.append(k.strip())
#     k1=[]
#     for x in l1:
#         r=filter(lambda x:x.isalpha(),x)
#         k1.extend(list(r))
#     h=Counter(k1)
#     print(h.most_common(1))
########################### thong ke tat ca cac tu
# with open("dssv.txt","r") as f:
#     l=f.readlines()
#     l1=[]
#     for x in l:
#         k=x.strip("\n")
#         l1.append(k.strip())
#     print(l1)
#     k1=[]
#     for x in l1:
#         r=x.split()
#         k1.extend(r)
#     h=Counter(k1)
#     print(h.most_common())
#######################################


