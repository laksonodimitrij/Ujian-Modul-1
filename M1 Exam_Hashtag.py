"""
Title         : Hashtag.py
Source        : Module 1 Exam Purwadhika no.1

Summary       : Create a function called Hashtag that generate hashtag which accepting string 
                separated by space as presented the below with following rules (15 Points):
                
Feat Req      : - It must start with a hashtag (#).
                - All words must have their first letter capitalized.
                - If the final result is longer than 140 chars it must return False.
                - If the input or the result is an empty string it must return False.

                
"""

# put the input string first.
String = input('Please put a sentence : ')

# define the function with all prerequisite conditions.
def Hashtag(x):
    
    # if the input is empty string, it should return False. 
    #Has to be prioritised first as a preliminary or otherwise it won't get read and print '#' instead if empty.
    if x == '':
        return False
    
    # else if the length is more than 140, it should return False.
    # This should works as a second preliminary function.
    elif len(x) > 140:
        return False
    
    # when all of the preliminary function filled, this last condition goes.
    # else if the length of a string is less than 140 then it is operable.
    elif len(x) <= 140:
        z = x.title() # use title to make every first word capitalized.
        y = z.split() # turn it into list so every element is independent.
        word = '#'+''.join(y)
        return f'"{word}"' # return the joined string with added '#' on front.

print(Hashtag(String))



