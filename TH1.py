#bai6:
# def xeploai(diem):
#     if diem >=0 and diem<3.5:
#         print('yeu')
#     elif diem>=3.5 and diem <5:
#         print('kem')
#     elif diem>=5 and diem <6.5:
#         print('trung binh')
#     elif diem>=6.5 and diem <8:
#         print('kha')
#     elif diem>=8 and diem <9:
#         print('gioi')
#     elif diem >=9 and diem <=10 :
#         print('xuat sac')
#     else :
#         print('Eror')
# if __name__ == '__main__':
#     while True:
#         f=int(input('Nhap diem:'))
#         xeploai(f)
#         f=input('Bạn muốn tiếp tục không plese(yes/no)!:')
#         f_lo=f.lower()
#         if f_lo=='no':
#             print("Thank for joining . Have a nice day ! :) ")
#             break
#bai7:
# f,c,d=input('Nhap ba so:').split(' ')
# if f==c and f!=d:
#     print(d)
# elif f==d and f!=c:
#     print(c)
# elif c==d and f!=c:
#     print(f)
# else :
#    print(f"gia tri lon nhat trong ba so la:{max(f,c,d)}")
#bai8:
if __name__ == '__main__':
    while True:
        d_k,m_k,y_k=input().split('/')
        d=int(d_k)
        m=int(m_k)
        y=int(y_k)
        m_30=[4,6,9,11]
        m_31=[1,3,5,7,8,10]
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) and (d==29) and (m==2):    
            day = 1
            month = 3
            year = y
            print(f'{day}/{month}/{year}')
        else:
            if (m == 2) and (d <= 28) and (m<12):
                if d == 28:
                    day = 1
                    month = m+1
                    year = y
                    print(f'{day}/{month}/{year}')
                else:
                    day = d+1
                    month = m
                    year = y
                    print(f'{day}/{month}/{year}')
            elif m in m_30 and (m<12) and (d<=30):
                if d == 30:
                    day = 1
                    month = m+1
                    year = y
                    print(f'{day}/{month}/{year}')
                else:
                    day = d+1
                    month = m
                    year = y
                    print(f'{day}/{month}/{year}')
            elif m in m_31 and (d <= 31) and (m<12) and (d<=31):
                if d == 31:
                    day = 1
                    month = m+1
                    year = y
                    print(f'{day}/{month}/{year}')
                else:
                    day = d+1
                    month = m
                    year = y
                    print(f'{day}/{month}/{year}')
            elif (m == 12) and (d <= 31):
                if d == 31:
                    day = 1
                    month = 1
                    year = y
                    print(f'{day}/{month}/{year}')
                else:
                    day = d+1
                    month = m
                    year = y
                    print(f'{day}/{month}/{year}')
            else:
                print("nhap sai")
        guess=input('Can you repeat please(Yes/No):')
        guess_af=guess.lower()
        if guess_af=='no':
            break
        elif guess_af=='yes':
            continue







