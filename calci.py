#contains only the def to the file main.py 
# separate functions for each operations (*like to add ,sub and etc) 

def to_add(var1,oper,var2):
    print(f'you entered: {var1} {oper} {var2}')
    result=var1+var2
    return result

def to_sub(var1,oper,var2):
    print(f'you entered: {var1} {oper} {var2}')
    res=var1-var2
    return res

def to_mul(var1,oper,var2): 
    print(f'you entered: {var1} {oper} {var2}')
    res=var1*var2
    return res

def to_div(var1,oper,var2):
    print(f'you entered: {var1} {oper} {var2}')
    res=int(var1)/var2
    return res
