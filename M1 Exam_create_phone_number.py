"""
Title         : create_phone_number.py
Source        : Module 1 Exam Purwadhika no.2

Summary       : Write a function that accepts a list of 10 integers (between 0 and 9), 
                that returns a string of those numbers in the form of a phone number (10 points).

Feat Req      : - The returned format must follow the example. 
                - Don't forget the space after the closing parentheses!

                
"""
# step by step logic:
# ask for input to put only 10 integers between 0 and 9
# create a function to do so.
# split1 first 3 numbers inside () and turn it into strings
# split2 another 3 numbers to be string
# split3 the rest to be turned into list
# join the rest, split1 with spaces and split2 separated by '-' followed by split3

numbers = list(input('Put numbers only 10 integers between 0 and 9 : '))

def create_phone_number(x):
    splits = ''.join(map(str,x))
    form = f'"({splits[0:3]}) {splits[3:6]}-{splits[6:]}"'
    return form

print (create_phone_number(numbers))