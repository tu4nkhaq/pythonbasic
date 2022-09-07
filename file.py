# with open("text.txt") as f:
#     fw=f.read()
# w=fw.split(' ')
# print(w)
# fe=f.read()
# words=fe.split(' ')
# w_count=len(words)
# print(w_count)
# f1=open('text.txt','r')
# fr10=f1.read(10)
# print(fr10)
# import os
# f2 = open('text.txt', 'a+')
# f2.write('Attack detected')
# f1=open('text.txt','r')
# fr=f1.read()
# print(fr)
# os.rmdir('test.txt')
# with open("123.txt","r") as file:
#     with open("file.txt","w") as f:
#         for i in file:
#             f.write(i)
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)
