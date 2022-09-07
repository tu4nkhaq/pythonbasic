def nen(s=""):
    dem=0
    temp=s[0]
    k=len(s)
    i=0
    b=""
    while i<k:
        if temp==s[i]:
            dem=dem+1
        else:
            b=b+temp+str(dem)
            temp=s[i]
            dem=0
            i=i-1
        i=i+1
    return b
# if __name__=='__main__':
#     s=str(input('Nhap chuoi can nen:')).split(" ")
#     for item in s:
#         k=item+'k'
#         print(nen(k),end=" ")
#giai chuoi
def giai(s=""):
    dem=0
    temp=s[0]
    k=len(s)
    i=0
    b=""
    while i<k:
        if temp==s[i]:
            b=b+temp
        else:
        
           b=b+s[i-1]*int(s[i]-1)

            # b=b+temp+str(dem)
        temp=s[i+1] 
        i=i+1
    return b
if __name__=='__main__':
    s=str(input('Nhap chuoi can nen:')).split(" ")
    for item in s:
        # k=item+'k'
        print(giai(item),end=" ")


