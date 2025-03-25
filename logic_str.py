'''logic str module!
       Welcome!'''

#This converter is used to convert data 
def str_convert(a):
    if a == 1:
        return "True"
    elif a == 0:
        return "False"
    
#The AND operator returns 1 if only both inputs are 1
def str_AND(a, b):
    if a and b == "True":
        return "True" 
    else:
        return "False"

#The NOT operator returns the opposite of the input
def str_NOT(a):
    if a == "True":
        return "False"
    else:
        return "True"

#The OR operator returns a 1 if either one of the inputs or both are 1
def str_OR(a,b):
    if a or b or a and b == "True":
        return "True"
    else:
        return "False"

#The NOR operator flips the output of an OR gate
def str_NOR(a,b):
    return str_NOT(str_OR(a,b))  

#The NAND operator flips of the output of an AND gate
def str_NAND(a,b):
    return str_NOT(str_AND(a,b))


#The XOR operator returns 1 if one and only one input is 1
def str_XOR(a,b):
    if a or b == "True":
        return "True"
    else:
        return "False"

#The XNOR operater flips the output of a XOR gate
def str_XNOR(a,b):
    return str_NOT(str_XOR(a,b))

#The dual four-input AND operator returns 1 if all the inputs are 1
def str_DUAL_AND(a,b,c,d):
    if a and b and c and d == "True":
        return "True"
    else:
        return "False"

#The dual four input NAND operator flips the output of a dual AND gate
def str_DUAL_NAND(a,b,c,d):
    return str_NOT(str_DUAL_AND(a, b, c, d))
    
#To learn more about these gates go here: https://www.geeksforgeeks.org/logic-gates/