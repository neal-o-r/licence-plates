from itertools import combinations_with_replacement, product
from toolz import mapcat
from itertools import combinations_with_replacement, product

"""
Solves a game i played as a chap. Given a licence plate number
(some string of digits from 1 - 100000), can you make a balanced
equation by just inserting simple operators (+-*/) and an equals sign
i.e. 1234 => 1 - 2 = 3 - 4
"""


def splits(n):
    return [(n[:i], n[i:]) for i in range(1, len(n))]


def is_valid(pair):
    lhs, rhs = pair
    try:
        return eval(f"{lhs} == {rhs}")
    except ZeroDivisionError:
        return False


def interleave(a, b):
    ret = [ai + bi for ai, bi in zip(a, b)]
    return "".join(ret) + a[-1]


def equation(pair, ops):
    op_lhs, op_rhs = ops
    lhs, rhs = pair
    return interleave(lhs, op_lhs), interleave(rhs, op_rhs)


def all_equations(pair):
    lhs, rhs = pair
    ops = "+-*/"
    lhs_ops = combinations_with_replacement(ops, len(lhs)-1)
    rhs_ops = combinations_with_replacement(ops, len(rhs)-1)

    return [equation(pair, (lo, ro)) for lo, ro in product(lhs_ops, rhs_ops)]


def check_range(n_max):

    solved = []
    for n in range(1, n_max):
        n = str(n)
        eqns = list(filter(is_valid, mapcat(all_equations, splits(n))))
        solved.append(len(eqns))

    return solved

