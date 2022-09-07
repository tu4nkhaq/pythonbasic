# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)
# print(list(sortList(List)))
# # Get the second largest element
# secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
# res = secondLargest(List, sortList)

# print(res)
# Python Program to find all anagrams of str in
# a list of strings.
from collections import Counter

my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"

# use anonymous function to filter anagrams of x.
# Please refer below article for details of reversed
# https://www.geeksforgeeks.org/anagram-checking-python-collections-counter/
result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list))

# printing the result
print(result)

