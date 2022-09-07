# typeMonney = [200, 500, 1000, 2000, 5000]
# monney = int(input("N = "))
# number = int(input("M = "))
# numberRes = 0
# sumMonneyCurrent = 0
# def find(k, j):
#     global numberRes, sumMonneyCurrent
#     for i in range(j, 5):
#         # listMonney[k] = typeMonney[i]
#         sumMonneyCurrent += typeMonney[i]
#         if sumMonneyCurrent == monney:
#                 numberRes += 1
#         if k < number and sumMonneyCurrent + (number - k + 1) * 5000 > monney and sumMonneyCurrent < monney:
#             find(k + 1, i)

#         sumMonneyCurrent -= typeMonney[i]
#             # listMonney[k + 1] = 0

# find(1, 0)
# print("Co %d phuong an doi tien"%numberRes)

# def Money(n, m):
#     if n%100 !=0:
#         return 0
#     d = 0
#     for a1 in range(n//5000, -1, -1):
#         n1 = n - a1 * 5000
#         if a1 > m:
#             break
#         for a2 in range(n1//2000, -1, -1):
#             n2 = n1 - a2 *2000
#             if a1+a2 >m: break
#             for a3 in range(n2//1000, -1, -1):
#                 n3 = n2 - a3 *1000
#                 if a1 + a2 + a3 >m: break
#                 for a4 in range(0 if n3 %200 == 0 else 1, n3//500+1, 2):
#                     n4 = n3 - a4 *500
#                     a5 = n4//200
#                     if a1 + a2 + a3 + a4 + a5<=m:
#                         d+=1
#     return d

# n = int(input("N = "))
# m = int(input("M = "))
# print("Co", Money(n, m), "phuong an doi tien")


# print("Co %d phuong an doi tien" %Money(n, m))
# print(f"Co {Money(n, m)} phuong an doi tien")
# print("Co {} phuong an doi tien".format(Money(n, m)))