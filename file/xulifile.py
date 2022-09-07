# def luufile(path,data):
#     file=open(path,"a",encoding="utf-8")
#     file.writelines(data)
#     file.writelines("\n")
#     file.close()
def docfile(path):
    file=open(path,"r",encoding="utf-8")
    arr=[]
    for i in file:
        data=i.strip()
        a=data.split(",")
        arr.append(a)
    file.close()
    return arr
    


