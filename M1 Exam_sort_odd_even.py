"""
Title         : sort_odd_even.py
Source        : Module 1 Exam Purwadhika no.3

Summary       : You are given a list of integers. 
                Your task is to sort odd numbers within the list in ascending order
                and even numbers in descending order 
                but keep all the odds or the evens number in the same index group (35 Points).
                
Feat Req      : - Note that zero is an even number. 
                - If you have an empty list, you need to return it.

                
"""

data = [5, 3, 2, 8, 1, 4]

# sorting odd or even without emptied index

def sort_odd_even(num):
    genap = []
    ganjil = []
    for i in num:
        if i % 2 == 0:
            genap.append(i)
        elif i % 2 != 0:
            ganjil.append(i)
    print (sorted(ganjil))
    print (sorted(genap))

sort_odd_even(data)



# def sort_odd_even(num):
#     genap = []
#     ganjil = []
#     for i in (len(num)):
#         if num[i] % 2 == 0:
#             genap.append(i)
#             genap.append(num[i])
#         elif num[i] % 2 != 0:
#             ganjil.append(i)
#             ganjil.append(num[i])
#     ganjil.sort()
#     genap.sort()
#     print (sorted(ganjil))
#     print (sorted(genap))

# sort_odd_even(data)