from Polynomial import Polynomial
from Monomial import Monomial
from MonomialOrder import MonomialOrder

def long_divide(dividend, divisors, order):
    dividend.reorder(order)
    for divisor in divisors:
        divisor.reorder(order)
    quotients = [Polynomial([Monomial('0')])] * len(divisors)
    p = dividend
    while p != Polynomial([Monomial('0')]):
        i = 1
        division_occurred = False
        while i <= len(divisors) and not division_occurred:
            