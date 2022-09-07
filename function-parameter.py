def tong (*data):
    k=[]
    t=0
    for item in data:
        for n in item:
            t=t+n
        k.append(t)
    s=0
    for x in k:
        s=s+x
    return s
ketqua=tong([53,34,23],[32,32,3],[83,54,45,34,23])
print(ketqua)