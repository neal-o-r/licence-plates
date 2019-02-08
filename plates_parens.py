from itertools import combinations_with_replacement
from operator import add, mul, sub, truediv
from rpn import rpn


"""
This uses reverse polish notation to solve the problem but
allowing operator precedence to be changed (with parens).
It also solves a slight variant on the problem,
it tries to find an eqn which can be made == 0,
which is a little easier e.g. 1137 = (1-1)*3*7 = 0
"""

def numtostring(n):
    ns = str(n)
    s = ns[:2]
    for c in ns[2:]:
        s += "_" + c
    return s + "__"


def fill_slots(s, v):
    vi = iter(v)
    ret = [next(vi) if si is "_" else si for si in s]
    return "".join(ret).replace(" ", "")


def all_eqn(s):
    ops = combinations_with_replacement("+-/* ", s.count("_"))
    all_fills = [fill_slots(s, o) for o in ops]
    return all_fills


def apply_rpn(s):
    try:
        return rpn(s)
    except NotValidEqnError:
        return None


def valid_solutions(n):
    return list(filter(lambda x: apply_rpn(x) == 0.0, all_eqn(numtostring(n))))
