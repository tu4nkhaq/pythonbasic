#nhap="python la ngon ngu nhanh nhat the giới python Nguyen Tuan Khang"
#print (nhap.replace("python","php"))
# hello="hello World"
#hello.capitalize()
#print(hello.capitalize())
#from ntpath import join
#from lib2to3.pgen2.token import NUMBER
#from ntpath import join
# print(hello.endswith('g'))
'''
import string
import random

LETTERS=string.ascii_letters
NUMBERS=string.digits
PUNCTUATION=string.punctuation

def password_generator (length=8):
    printable = f'{LETTERS} {NUMBERS} {PUNCTUATION}'
    printable = list (printable)
    random.shuffle (printable)
    randon_password = random. choices (printable, k=length)
    randon_password = ''.join(randon_password)
    return randon_password
def get_password_length():
    password_length = input ("How long do you want your password: ")
    return int (password_length)
def main():
    password_length = get_password_length()
    password = password_generator (password_length)
    print (password)
if __name__=="__main__":
    main()
'''
# name=str(input("N="))
# isplain=name.find(name[::-1])==0
# print(bool(isplain))





# n=list(input("N=").split())
# for i in n:
#     if i.isdigit():
#         print(i,end=" ")

#bai 3
# def hoten(hovaten):
#     ho=hovaten[0:hovaten.index(" ")]
#     timten=hovaten[::-1]
#     ten=timten[0:hovaten.index(" ")]
#     tendung=ten[::-1]
#     return(ho,tendung)
# s=input("Nhap ho va ten:")
# ho,ten=hoten(s)
# print(f"Ho:{ho};Ten:{ten}")

#bai 3 lan 2
def hoten(hovaten):
    ho=hovaten[0:hovaten.index(" ")]
    ten=hovaten[-1:hovaten.index(" ")]
    return(ho,ten)
s=input("Nhap ho va ten:")
ho,ten=hoten(s)
print(f"Ho:{ho};Ten:{ten}")



#bai4
# string = "fgdf 76 87  7fdgsdfs?"
# new_string= ''
# for char in string:
#     if (char.isalpha() == True):
#         new_string += char
# print(new_string)
# string = "fgdf 76 87  7fdgsdfs?"
# new_string = ''.join(char for char in string if char.isalpha())
# print(new_string)

