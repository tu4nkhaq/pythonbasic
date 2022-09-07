my_dict = {"name": "CodeXplore","content": "Programming Youtube Channel", "city": "Singapore"}
s=[5,3,6,3,7,4,3,2,9]
d=dict.fromkeys(s,'khang')
dict.has_key()
# print (my_dict)
# Looping through Dictionary
# loop over keys and values
# for value in my_dict.values():
#     print (value)

# import unittest
# def unique(str):
# # Hint: Hash Table => Dict: key-value
#     char_set = {}
#     for char in str:
# # print(char)
#         if char in char_set:
#             return False
#         char_set[char] = True
#     return True
# class Test(unittest.TestCase):
#     dataT=[('asdgfh'),('dgfsy'),('hr423'),('fdkh54')]
#     dataF=[('asdgfhas'),('dgfsysd'),('hr4223h'),('fddkh54f')]
#     def test_unique(self):
#         for test in self.dataT:
#             actualResult=unique(test)
#             self.assertTrue(actualResult)
#         for test in self.dataF:
#             actualResult=unique(test)
#             self.assertFalse(actualResult)

# if __name__=="__main__":
#     unittest.main()