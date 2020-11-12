"""
Title         : hollowTriangle.py
Source        : Module 1 Exam Purwadhika no.4

Summary       : Create a function hollowTriangle(height) that returns a hollow triangle 
                of the correct height or level. (40 Points)

Feat Req      : hollowTriangle(1)// would return or print    
                #
                    
                hollowTriangle(2)// would return or print  
                _#_  
                ###

                hollowTriangle(3)// would return or print  
                __#__
                _#_#_
                #####

                
"""

def hollowTriangle(n): #ver1
    k = 0
    for i in range(1,n+1) : #row 6 
      
        # Print spaces continously until it reached k
        for j in range(i,n) : 
            print('_', end='') 
          
        # Print # when the result of k equals with the condition of if
        while (k != (2 * i - 1)) : 
            if (k == 0 or k == 2 * i - 2) :     # in this line, the condition allows us having gap between # of k
                print('#', end='') 
            else : 
                print('_', end ='') 
            k = k + 1                           # in this line k got added to put continue the calculation under while function in the column
        k = 0;                                  # k got reset
        print ("")                              # print next row 
          
    # print last row as the row should be twice compared to the first row
    for i in range(0, 2 * n -1) : 
        print ('#', end = '') 

