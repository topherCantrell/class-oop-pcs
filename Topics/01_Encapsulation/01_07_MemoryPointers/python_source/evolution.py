def do_fun():
    a = 5
    while a>0 and a!=10:   
        if a==3:
            continue        
        a = a - 1     
        
class Account:
    
    def _helper_function(self):
        pass
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self):
        pass
    
    def chargeFee(self,amount):
        pass
    
def say_hi_EN():
    print('Hello')
    
def say_hi_SP():
    print('Hola')
    
greet = say_hi_EN
greet()

greet = say_hi_SP
greet()

   
        
import dis
print( dis.dis(do_fun))