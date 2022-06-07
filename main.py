# this is the main file which imports the another file of calci.py
#using simple if-elif-else conditions

from calci import to_add,to_sub,to_mul,to_div
print("""/
   _____________________
  |  _________________  |
  | |const 3.14159265 | |
  | |_________________| |
  |  ___ ___ ___   ___  |
  | | 7 | 8 | 9 | | + | |
  | |___|___|___| |___| |
  | | 4 | 5 | 6 | | - | |
  | |___|___|___| |___| |
  | | 1 | 2 | 3 | | x | |
  | |___|___|___| |___| |
  | | . | 0 | = | | / | |
  | |___|___|___| |___| |
  |_____________________|

""")
list1=['+','-','/','*',"e","E"]   #if these are not given as input by user the program doesn't continue and shows error as in line 27 
calci_on=True
while calci_on:   #while true it executes the program
        
        oper=input('enter the symbol(+,-,*,/) or enter "e" to exit from program: ')
        if oper not in list1:
                print("wrong input.TRY AGAIN")
        else:
                if oper.lower()=="e" :
                        print("terminated successfully")
                        calci_on=False
                else:
                    var1=int(input("enter the num1: "))
                    var2=int(input("enter the num2: "))
                    if oper=="+":
                        add_res =to_add(var1,oper,var2)
                        print(f" the result is :{add_res}")
                    elif oper=="-":
                        sub_res=to_sub(var1,oper,var2)
                        print(f" the result is :{sub_res}")        
                    elif oper=="*":          
                        mul_res=to_mul(var1,oper,var2)
                        print(f" the result is :{mul_res}")        
                    elif oper=="/":            
                        div_res=to_div(var1,oper,var2)
                        print(f" the result is :{div_res}")

