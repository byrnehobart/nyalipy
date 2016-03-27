# Byrne Hobart
# [2016-03-27 Sun]

def read_lisp(arg): # still buggy
    """Takes a string, splits it into a list of atoms, lists"""
    output = []
    elts = arg.split()
    if elts[0][0] != '(':
        return elts[0]
    else: 
        output.append(elts[0][1:]) 
    for elt in elts[1:]:
        print('Now parsing: ',elt)
        if elt[-1] == ')':
            return output
        else:
            output.append(read_lisp(elt))

test_string = '(+ 1 2 (- 3 4))'

test_parsed_string = ['+',1,2,['-',3,4]]

def l_apply(func, args):
    try:
        return funclist[func](args)
    except:
        print('Function \"'+func+'\" is not a valid function.')

def l_plus(args):
    return sum(args)

def l_minus(args):
    if len(args) == 1:
        return args[0]
    else:
        ans = args[0]
        for minuend in args[1:]:
            ans -= minuend
        return ans

def l_mult(args):
    ans = 1
    for arg in args:
        ans = ans * arg
    return args

def l_div(args):
    ans = arg[0]

funclist = {'+':l_plus,
            '-':l_minus,
            '*':l_mult,
            '/':l_div}



# Take a list of elements. One at a time, append to the output list.
# If an element starts with '(', look for next ')', run read_lisp on that slice
# of the list.
