#TODO: error catching malformed mono/polynomials

from Polynomial import Polynomial
from Monomial import Monomial, divides
from MonomialOrder import MonomialOrder
import argparse

def long_divide(dividend, divisors, order):
    dividend.reorder(order)
    for divisor in divisors:
        divisor.reorder(order)
    quotients = [Polynomial('0')] * len(divisors)
    p = dividend
    r = Polynomial('0')

    while p != Polynomial('0'):
        i = 0
        division_occurred = False
        while i < len(divisors) and not division_occurred:
            lt_f_i = divisors[i].leading_term(order)
            lt_p = p.leading_term(order)
            if divides(lt_f_i,lt_p):
                div_result = lt_p / lt_f_i
                quotients[i] += Polynomial([div_result])
                p -= Polynomial([div_result]) * divisors[i]
                division_occurred = True
            else:
                i += 1
        if not division_occurred:
            r += Polynomial([p.leading_term(order)])
            p -= Polynomial([p.leading_term(order)])
    return quotients, r

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--monomial-order", "-mo", choices=["lex", "grlex", "grevlex"], help="Input lex, grlex, \
                        or grevlex as the monomial order. The default is lex", default="lex")
    parser.add_argument("--variable-order", "-vo", help="input a variable order, e.g. xyz or zyx, the default is xyz.\
                        Write in decreasing order from left to right", default="x>y>z")
    parser.add_argument("--dividend", help="input a polynomial to be used as the dividend. E.g. x^4*y+1")
    parser.add_argument("--divisors", nargs="+", help="input polynomials to be used as the divisors, separated by spaces")
    args = parser.parse_args()
    monomial_order = MonomialOrder(args.variable_order, args.monomial_order)
    dividend = Polynomial(args.dividend)
    divisors = [Polynomial(divisor) for divisor in args.divisors]
    quotients, remainder = long_divide(dividend, divisors, monomial_order)
    assert len(quotients) == len(divisors)
    print()
    print(f"Dividend: {dividend.ordered_str(monomial_order)}")
    print("----------------")
    for divisor, quotient in zip(divisors, quotients):
        print(f"Divisor: {divisor.ordered_str(monomial_order)}, quotient: {quotient.ordered_str(monomial_order)}")
    print()
    print(f"Remainder: {remainder.ordered_str(monomial_order)}")



    # testing code
    # p1 = Polynomial('x^7*y^2+x^3*y^2-y+1')
    # p2 = Polynomial('x*y^2-x')
    # p3 = Polynomial('x-y^3')
    #
    #
    # order = MonomialOrder('xyz','lex')
    #
    # quotients, remainder = long_divide(p1,[p2, p3],order)
    # [print(q.ordered_str(order)) for q in quotients]
    # print(remainder.ordered_str(order))