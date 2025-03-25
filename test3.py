#A demo to see how much easier it is to use the 'logic_int' and 'logic_str' modules than the 'opertors' one
from logic import operators, logic_str, logic_int

#logic_int
print(logic_int.AND(1, 0)) #fast single line usage

#logic_str
print(logic_str.str_AND("True", "False")) #also, fast single line usage

#operators
and_gate = operators.AND(1, 1) #unfortunatly dual line usage
print(and_gate.int_operate()) #easier (individual) argument changing

'''expected output:
    
    0
    False
    1
    
            '''