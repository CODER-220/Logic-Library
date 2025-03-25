#A demo of the 'show()' method
from logic import operators #imports the 'operators' module

my_gate = operators.AND(1, 1) #create an AND gate object and names it my_gate
print(my_gate.show()) #displays the output of my_gate

'''expected output:

    a|b|out
    -|-|---
    1|1|1
    0|1|0
    1|0|0
    0|0|0
    
            '''
