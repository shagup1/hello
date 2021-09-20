#program1calculatorusingpython
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
#main program
a=double(input('enter first number:'))
b=double(input('enter second number:'))
obj=cal(a,b)
while True:
    def menu():
        x=('1.add\n2.sub\n3.mul\n4.div')
        print(x)
    menu()
    choice=int(input('please select your choice:'))
    if choice==1:
        print("addition:",obj.add())
    elif choice==2:
        print("sub:"obj.sub())
    elif choice==3:
        print("mul:",obj.mul())
    elif choice==4:
        print("div:",obj.div())
    elif choice==0:
        print('try again one of the following')
        break
   else:
    print('invalid option')
    break
print()    
    
