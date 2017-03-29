# Byrne Hobart
# [2016-03-27 Sun]

from collections import namedtuple
import re

ConsCell = namedtuple('ConsCell','car cdr')

def tokenize_str(string):
    """Take a string, return a list of tokens"""
    return [x for x in re.split(' |(\()|(\))',string) if x != None and x != '']

def list_to_conses(lst):
    """Convert a list to a collection of conses

    I may not need to use this"""
    if lst == []:
        return '()'
    return ConsCell(lst[0],list_to_conses(list[1:]))

def grab_sublist(token_list):
    """Extract a sub-list from a list
    
    Returns 1) the extraced sublist, and 2) the remainder of the original list"""
    parencount = 1
    sublist = []
    while token_list != []:
        elt = token_list.pop(0)
        if elt == '(':
            subsublist,token_list = grab_sublist(token_list)
            sublist.append(subsublist)
        elif elt == ')':
            parencount -= 1
            if parencount == 0:
                print("Parencount-induced exit")
                print(sublist[0],token_list)
                return sublist,token_list # don't return the closing paren of the sublist
        else:
            try:
                elt = int(elt)
            except:
                pass
            sublist.append(elt)
    print(sublist[0],token_list)
    return sublist[0], token_list
    print("Somehow token list got returned, not parsed")
    
def atomp(elt):
    """Check a string to see if it's an atom"""
    if elt not in ['(',')']:
        return True
    else:
        False
            
test_string = '(+ 1 2 (- 3 4))'

test_2 = '(cons a (car (cdr (b c d))))'

test_parsed_string = ['+',1,2,['-',3,4]]

# Lisp Functions, operating on lists

def l_eval(lst):
    func = l[0]
    args = l[1:]
    for x in args:
        if not atomp(x):
            x = l_eval(x)
    return l_apply(func,args)

def l_lambda(vars,func):
    return func(vars)

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
    if len(args) != 2 or type(args[1]) != list:
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
