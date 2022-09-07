# from collections import Counter
# import random
# n=int(input("Nhap N:"))
# s=[]
# for i in range(n):
#     s.append(random.randint(0,10))
# print(Counter(s))
# mc=Counter(s).most_common(1)
# print(dict(mc))
# s=sorted(set(s),reverse=True)
# print(s)
# data=[{"name": "Max", "age": 6}, 
#         {"name": "Lisa", "age": 20},
#         {"name": "Ben", "age": 9}]
# sorted_data=sorted(data,key=lambda x:x)
# print(sorted_data)

# for i in s:
#     c=0
#     d=1
#     n=len(i)
#     for k in range(n):
#         print(k)
    #     if i[k]==i[k+1]:
    #         d=d+1
    #     else : d
    # print(f'{i[k]}{d}')
# a='dfdhh    kkkkk   kkkk'.split()
# b='dfjdddd'
# k=b+'k'
# print(k)
# f="kskhdfhd"
# k=set(f)
# print(k)
# a=6
# b=a
# b=8
# print(a,b)
# set_1 = {1, 2}
# set_1.pop()
# print(list(set_1))
# list = [1, 3, 4, 5, 7, 33, 54, 5]
# print(dict(list.count)) # 5
a = {'a': 1, 'b': 2}
print(a.get('d', 4))  # 4