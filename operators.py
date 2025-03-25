'''operators module!
        Welcome!     '''

def int_str_converter(a):
    if a == 1:
        return "True"
    else:
        return "False"

def str_int_converter(a):
    if a == "True":
        return 1
    else:
        return 0


class AND:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def int_operate(self):
        if self.a and self.b == 1:
            return 1
        else:
            return 0
    
    def str_operate(self):
        if self.a and self.b == "True":
            return "True"
        else:
            return "False"
    
    def show(self):
        return "a|b|out\n-|-|---\n1|1|1\n0|1|0\n1|0|0\n0|0|0"

    

class OR:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def int_operate(self):
        if self.a == self.b or self.a or self.b == 1:
            return 1
        else:
            return 0
    
    def str_operate(self):
        if self.a == self.b or self.a or self.b == "True":
            return "True"
        else:
            return "False"
    
    def show():
        return "a|b|out\n-|-|-\n1|1|1\n1|0|1\n0|1|1\n|0|0|0"

class NOT:
    def __init__(self, a):
        self.a = a
    
    def int_operate(self):
        if self.a == 1:
            return 0
        else:
            return 1
    
    def str_operate(self):
        if self.a == "True":
            return "False"
        else:
            return "True"
    
    def show():
        return "a|out\n-|---\n1|0\n0|1"

class NOR:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def int_operate(self):
        if self.a and self.b or self.a and self.b == 1:
            return 0
        else:
            return 1
    
    def str_operate(self):
        if self.a and self.b or self.a and self.b == "True":
            return "False"
        else:
            return "True"
    
    def show():
        return "a|b|out\n-|-|-\n1|1|0\n1|0|0\n0|1|0\n|0|0|1"

class NAND:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operate(self):
        if self.a and self.b == 1:
            return 0
        else:
            return 1
    
    def operate(self):
        if self.a and self.b == "True":
            return "False"
        else:
            return "True"
    
    def show():
        return "a|b|out\n-|-|---\n1|1|0\n0|1|1\n1|0|1\m0|0|1"
    
class XOR:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operate(self):
        if self.a or self.b == 1:
            return 1
        else:
            return 0
        
    def operate(self):
        if self.a or self.b == "True":
            return "True"
        else:
            return "False"
    
    def show():
        return "a|b|out\n-|-|---\n1|1|0\n1|0|1\n0|1|1\n0|0|0"

class XNOR:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operate(self):
        if self.a or self.b == 0:
            return 1
        else:
            return 0
        
    def operate(self):
        if self.a or self.b == "False":
            return "True"
        else:
            return "False"
        
    def show():
        return "a|b|out\n-|-|---\n1|1|1\n1|0|0\n0|1|0\n0|0|1"

class DUAL_AND:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def operate(self):
        if self.a and sel.b and self.c and self.d == 1:
            return 1
        else:
            return 0
        
    def operate(self):
        if self.a and self.b and self.c and self.d == "True":
            return "True"
        else:
            return "False"
        
    def show():
        return "a|b|c|d|out\n-|-|-|-|---\n0|0|0|0|0\n0|0|0|1|0\n0|0|1|0|0\n0|0|1|1|0\n0|1|0|0|0\n0|1|0|1|0\n0|1|1|0|0\n0|1|1|1|0\n1|0|0|0|0\n1|0|0|1|0\n1|0|1|0|0\n1|0|1|1|0\n1|1|0|0|0\n1|1|0|1|0\n1|1|1|0|0\n1|1|1|1|1"

class HALF_ADDER:
    def __init__(self, choice, a, b):
        self.choice = choice
        self.a = a
        self.b = b
    
    def operate(self):
        if self.choice == "SUM":
            if self.a or self.b == 1:
                return 1
            else:
                return 0
            
        elif self.choice == "CARRY":
             if self.a and self.b == 1:
                return 1
             else:
                return 0
    
    def show():
        return "a|b|carry|sum\n-|-|-----|---\n0|0|0|0|0\n1|0|0|1\n0|1|0|1\n1|1|1|0"
        
    class FULL_ADDER:
        def __init__(self, choice, a, b, c):
            self.choice = choice
            self.a = a
            self.b = b
            self.c = c
            
        def operate(self): 
            sumo1 = HALF_ADDER("SUM", self.a, self.b)
            sum1 = sumo1.operate()
            carryo1 = HALF_ADDER("CARRY", self.a, self.b)
            carry1 = carryo1.operate()
            sumo2 = HALF_ADDER("SUM", sum1, self.c)
            sum2 = sumo2.operate()
            carryo2 = HALF_ADDER("CARRY", sum1, self.c)
            carry2 = carryo2.operate()
            
            sum_out = sum2
            carryo_out = OR.operate(carry1, carry2)
            carry_out = carryo_out.operate()
            
            if choice == "CARRY":
                return carry_out
            elif choice == "SUM":
                return sum_out
            
    def show():
        return "a|b|carry_in|sum|carry_out\n-|-|--------|---------\n0|0|0|0|0\n0|0|1|1|0\n0|1|0|1|0\n0|1|1|0|1\n1|0|0|1|0\n1|0|1|0|1\n1|1|0|0|1\n1|1|1|1|1"
