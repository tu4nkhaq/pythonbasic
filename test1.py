# def N23(f):
#     b=f+10
#     a=[1]
#     c=1
#     for i in a:
#         if c<b:
#             a.append(2*i+1)
#             c+=1
#         if c<b:
#             a.append(3*i+1)
#             c+=1
#         if c>=b:
#             break
#     return a
# if __name__=="__main__":
#     b=int(input("N = "))
#     a=set(N23(b))
#     c=list(a)
#     print(f"{b} so dau tien cua N23: ",end="")
#     for i in range(b):
#         print(c[i],end=" ")
########
# n = int(input("N = "))
# g = 1
# left = 0
# k = [1]
# count = 1
# while True:
#     e = 2*g +1 
#     z = 3*g+1
#     k.append(e)
#     k.append(z)
#     left+= 1
#     g = k[left]
#     count += 2
#     if count >=n*10:
#         break 
# h=[o for o in set(k)]
# h.sort()
# print(f"{n} so dau tien cua N23: ",end="")
# for i in range(n):
#     print(h[i],end=" ")
################
# n=int(input("N = "))
# l=[1]
# def creat_list():
#     a=0
#     while len(l)<n:
#         k=l[a]
#         l.append(2*k+1)
#         if l[-1]<l[-2]:
#             l[-1],l[-2]=l[-2],l[-1]
#         if len(l)>=n:
#             break
#         if 3*k+1 in l:
#             a+=1
#         l.append(3*k+1)
#         if l[-1]<l[-2]:
#             l[-1],l[-2]=l[-2],l[-1]
#         a+=1
# creat_list()
# print(l)
#abcdcdcba
# s="cadabcb"
# b="bcbadac"
# if s == s[::-1]:
#    print(s)
# else:
#     temp=''.join(list(dict.fromkeys(s)))
#     s1=''.join(map(str,s))
#     for ch in temp[::-1][1:]:
#         s1+=ch
#         if s1 == s1[::-1]:
#             break
#     print(s)
# s = input().strip()
# print(s[::-1][1:])
import matplotlib.pyplot as plt % matplotlib inline  

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
RedCircle = Circle(10, 'red')
RedCircle.drawCircle()