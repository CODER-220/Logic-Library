#A demo of the 'convert()' method/function
from logic import operators, logic_int, logic_str

print(operators.int_str_converter(1)) #int to str using operators
print(operators.str_int_converter("True")) #str to int using operators

print(logic_int.convert("True")) #only str to int using logic_int
print(logic_str.str_convert(1)) #only int to str using logic_str
'''Note: the 'logic_str' and 'logic_int' have been designed to be used together
   'logic_int' is designed for hardware computing
    while 'logic_str' is designed for more software computing!
    But, the 'operators' module is for a mix of both!'''

'''Expected output:
    
    True
    1
    1
    True
    
        '''
