'''logic_int module!
       Welcome!'''

#This converter is used to convert data 
def convert(a):
    if a == "True":
        return 1
    elif a == "False":
        return 1
    
#The AND operator returns 1 if only both inputs are 1
def AND(a, b):
    if a and b == 1:
        return 1
    else:
        return 0

#The NOT operator returns the opposite of the input
def NOT(a):
    if a == 1:
        return 0
    else:
        return 1

#The OR operator returns a 1 if either one of the inputs or both are 1
def OR(a,b):
    if a or b or a and b == 1:
        return 1
    else:
        return 0

#The NOR operator flips the output of an OR gate
def NOR(a,b):
    return NOT(OR(a,b))  

#The NAND operator flips of the output of an AND gate
def NAND(a,b):
    return NOT(AND(a,b))


#The XOR operator returns 1 if one and only one input is 1
def XOR(a,b):
    if a or b == 1:
        return 1
    else:
        return 0

#The XNOR operater flips the output of a XOR gate
def XNOR(a,b):
    return NOT(XOR(a,b))

#The dual four-input AND operator returns 1 if all the inputs are 1
def DUAL_AND(a,b,c,d):
    if a and b and c and d == 1:
        return 1
    else:
        return 0

#The dual four input NAND operator flips the output of a dual AND gate
def DUAL_NAND(a,b,c,d):
    return NOT(DUAL_AND(a, b, c, d))

#Adds two single bits
def HALF_ADDER(choice,a,b): 
    if choice == "CARRY":
        return AND(a, b)#Carry bit
    elif choice == "SUM":
        return XOR(a, b)#Sum bit

#Adds two single bits and carry
def FULL_ADDER(choice,a,b,c):
    sum1 = HALF_ADDER("SUM",a,b)
    carry1 = HALF_ADDER("CARRY",a,b)
    sum2 = HALF_ADDER("SUM",sum1,c)
    carry2 = HALF_ADDER("CARRY",sum1,c)
    
    carry_out = OR(carry2,carry1)
    sum_out = sum2
    
    if choice == "CARRY":
        return carry_out#Carry bit
    elif choice == "SUM":
        return sum_out  #Sum bit

    
#To learn more about these gates go here: https://www.geeksforgeeks.org/logic-gates/