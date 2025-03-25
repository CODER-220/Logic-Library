# Logic Library
---------------
 Welcome
 Welcome to the Logic library! 
 To install, download the source code from this repository, and move it to the  correct path, (depends on your IDE), and pip insatl the path.
 
 Overview
 The Logic library is a python library programmed entirely in python 3, and is designed to allow
 users like you to acces logical operators. Don't worry if you don't know too much about these
 operators for we have provided some links to great websites to learn about them (below):
 >-https://www.geeksforgeeks.org/logic-gates/

 >-https://www.geeksforgeeks.org/difference-between-half-adder-and-full-adder/

 Usage
 This library has seperate modules for string boolean (str_logic) and integer binary (int_logic), the
 str_logic library has less functions, but may be more useful depending on the problem. Here are
 some examples of both modules:
 ```python
 #int_logic example
 from logic import logic_int
 print(logic_int.AND(1,0)) 
#prints output (0) of an AND gate with the inputs 1 and 0
```
```python
 #logic_str example
 from logic import logic_str
 print(logic_str.AND("True","False") 
#prints output ("False") of an AND gate with the inputs "True" and "False"
```

 There is also the more complex to use 'operators' library, which is class based instead of function
 based. Here is an example:
 ```python
 #opertors module example
 from logic import operators
 my_gate = operators.AND(1, 0)
 print(my_gate.operators.int_operate) #prints output using integer operate funtion
 my_other = operators.AND("True", False")
 print(my_other.operators.str_operate) #prints output using string operate function
```
 For some more (runnable) examples of both modules, go to logic>Tests>test1, test2, test3.
 Note: Remember that some funtions despend on others in the same module, so remember to
 import the entire module for simplicity.

 -------
 Any complaints are accepted 
