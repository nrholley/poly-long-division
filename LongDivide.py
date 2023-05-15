#TODO: move arithmetic operations into magic methods
#TODO: argparse entry point
#TODO: error catching malformed mono/polynomials

from Polynomial import Polynomial, poly_add, poly_multiply
from Monomial import Monomial, divides, divide
from MonomialOrder import MonomialOrder

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
                div_result = divide(lt_p, lt_f_i)
                quotients[i] = poly_add(quotients[i], Polynomial([div_result]))
                p = poly_add(p, poly_multiply(Polynomial('-1'),poly_multiply(Polynomial([div_result]), divisors[i])))
                division_occurred = True
            else:
                i += 1
        if not division_occurred:
            r = poly_add(r, Polynomial([p.leading_term(order)]))
            p = poly_add(p, poly_multiply(Polynomial('-1'), Polynomial([p.leading_term(order)])))
    return (quotients, r)

if __name__ == "__main__":

    p1 = Polynomial('x^7*y^2+x^3*y^2-y+1')
    p2 = Polynomial('x*y^2-x')
    p3 = Polynomial('x-y^3')


    order = MonomialOrder('xyz','grlex')

    quotients, remainder = long_divide(p1,[p2, p3],order)
    [print(q.ordered_str(order)) for q in quotients]
    print(remainder.ordered_str(order))