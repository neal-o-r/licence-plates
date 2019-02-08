from operator import add, sub, mul, truediv

class NotValidEqnError(BaseException):
    pass


def rpn(string):
    ops = {'+':add, '-':sub, '*':mul, '/':truediv}
    stack = []
    for s in string:
        if s in ops:
            try:
                stack.append(ops[s](stack.pop(), stack.pop()))
            except:
                raise NotValidEqnError
        else:
            stack.append(float(s))
    if len(stack) > 1: raise NotValidEqnError
    return stack[0]
