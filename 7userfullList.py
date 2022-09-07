from itertools import count
#list 1
#s=[32,13,4,35,36,40]
#print([t for t in s if 31<t<36])
#list 2
# s=["loc","dkhsa","aja","32","43"]
# c=["fkf","34","65","33","jgd"]
# print([(t1,t2) for t1 in s for t2 in c],sep="\n")
#List 4
#names = ["John", "Mary", "Lea"]
#surnames = ["Smith", "Wonder", "Singer"]
#ages=["22", "19", "25"]
#print([f'{names} {surnames}-{ages}'for names,surnames,ages in zip(names,surnames,ages)])
#List 5 convert value
#def dollar(eur):
#    return round(eur*1.19,2)
#prices=[12,1,21,31,2,1,6]
#print([dollar(t) for t in prices])
#List 6
# s="kasdhfkdsgks sdfkhasdfk euwfb wefuwf weufbw vfhv"

# print({c :s.count(c) for c in s})
#List 7
s=[3,4,3,5,6,7,8,3,5,6,8,4,3,6,6,6,6,6,6]
# print({c:s.count(c) for c in s})
# print(max(s,key=s.count))
print(s.count(3))