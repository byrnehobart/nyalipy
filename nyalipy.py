# Byrne Hobart
# [2016-03-27 Sun]

def read_lisp(elts):
    """parses tokens one at a time, stores in nested lists"""
    if len(elts) == 1: # atom evaluates to itself
        elt = elts[0]
        try:
            elt = int(elt)
        except:
            pass
        return elt
    else:
        output = []
        while True:
            if elts == []:
                return output
            else:
                elt = elts.pop(0)
                try:
                    elt = int(elt)
                except:
                    pass
                if elt == ')':
                    return output
                elif elt == '(':
                    output.append(read_lisp(elts))
                else:
                    output.append(elt)

def parse_string(arg):
    """Takes a string as input, turns into a list of tokens, sends to token-parser"""
    elts =  [item for sublist in [split_parens(x) for x in arg.split()] for item in sublist]
    return read_lisp(elts)[0] # so ugly. Why does it add an extra list?
        
def split_parens(string):
    """For any string beginning/ending w/a paren, returns string and paren separately"""
    if string[0] == '(':
        return ['(',string[1:]]
    elif string[-1] == ')':
        return [string[:-2], ')']
    else:
        return string

test_string = '(+ 1 2 (- 3 4))'

test_parsed_string = ['+',1,2,['-',3,4]]

# Lisp Functions, operating on lists

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

def l_cons(args):
    if len>args != 2 or type(args[1]) != list:
        print('error')
    else:
        return [args[0]]+args[1]

def l_car(args):
    if type(args) != list:
        print('Error:',args,'is not a list')
    else:
        return args[0]

def l_cdr(args):
    if type(args) != list:
        print('Error:',args,'is not a list')
    else:
        return args[1:]

# list of existing functions

funclist = {'+':l_plus,
            '-':l_minus,
            '*':l_mult,
            '/':l_div,
            'cons':l_cons,
            'car':l_car,
            'cdr':l_cdr}



# Take a list of elements. One at a time, append to the output list.
# If an element starts with '(', look for next ')', run read_lisp on that slice
# of the list.
