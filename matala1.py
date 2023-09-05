# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:21:57 2023

@author: 97254
"""
###exc_1
def my_func(x1,x2,x3):
    try :
        numer = (x1+x2+x3)*(x2+x3)*x3
        denom = x1 +x2 +x3
        if denom == 0 :    
            return('“ Not a number – denominator equals zero ”')
            
        if  isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float):
            return float(numer/denom ) 
        elif isinstance(x1, int) or isinstance(x2, int) or isinstance(x3, int):
            return('“Error: parameters should be float”')
    except:
        return
    
print(my_func(1.5, 0.0, -1.5))
print(my_func(1.5, 4.5, 4.0))
print(my_func(1.5, 4.5, "4"))
print(my_func(1.5, 4.5, 4))
###exc_2
PATH = "C:\\Users\\97254\\Desktop\\phyton\\exc2\\"
fname = PATH +"text.txt"
handle = open(fname)
def revword(word:str) :
    return word[::-1]
lst = []

    
def countword():
    for l in handle:
        l=l.rstrip().split(" ")
        lst.append(l)
        
    word = ''
    num = 1
    
    for i in range(len(lst)):
        if i == 0 :
            word = lst[i][i]
            continue
        else:
            for j in range(len(lst[i])):
                lst[i][j] = revword(lst[i][j]).lower()
                if lst[i][j] == word:
                    num+= 1 
    return "Number of occurrences of the word is " + str(num) ,'The word is ' + word  

print(countword())
#print(lst)






    






