#A demo of the 'int_operate' and 'str_operate' methods
from logic import operators

ANDy = operators.AND(1, 1)
print(ANDy.int_operate())
del ANDy
ANDy = operators.AND("True", "True")
print(ANDy.str_operate())

'''expected output:

    1
    True
            
            '''