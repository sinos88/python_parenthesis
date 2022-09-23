'''
A simple function to test that the parenthesis are 
valid or not.
'''


def valid_parentheses(string):
    open = 0
    close = 0
    
    if string[0] == ')':
        return False    
    
    for n in string:
        if n == '(':
            open += 1
        if n == ')':
            close += 1

        if close > open:   
            return False
    if open == close:
        return True
    else: 
        return False

string = ')test'
print(valid_parentheses(string))
