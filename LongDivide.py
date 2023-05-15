#TODO: move arithmetic operations into magic methods
#TODO: construct polynomial from string
#TODO: argparse entry point

from Polynomial import Polynomial, poly_add, poly_multiply
from Monomial import Monomial, divides, divide
from MonomialOrder import MonomialOrder

def long_divide(dividend, divisors, order):
    dividend.reorder(order)
    for divisor in divisors:
        divisor.reorder(order)
    quotients = [Polynomial([Monomial('0')])] * len(divisors)
    p = dividend
    r = Polynomial([Monomial('0')])

    while p != Polynomial([Monomial('0')]):
        i = 0
        division_occurred = False
        while i < len(divisors) and not division_occurred:
            lt_f_i = divisors[i].leading_term(order)
            lt_p = p.leading_term(order)
            if divides(lt_f_i,lt_p):
                div_result = divide(lt_p, lt_f_i)
                quotients[i] = poly_add(quotients[i], Polynomial([div_result]))
                # there is no forgiveness
                p = poly_add(p, poly_multiply(Polynomial([Monomial('-1')]),poly_multiply(Polynomial([div_result]), divisors[i])))
                division_occurred = True
            else:
                i += 1
        if not division_occurred:
            r = poly_add(r, Polynomial([p.leading_term(order)]))
            p = poly_add(p, poly_multiply(Polynomial([Monomial('-1')]), Polynomial([p.leading_term(order)])))
    return (quotients, r)

if __name__ == "__main__":
    m1 = Monomial("x^2*y")
    m2 = Monomial("x*y^2")
    m3 = Monomial("y^2")
    p1 = Polynomial([m1,m2,m3])

    m4 = Monomial("x*y")
    m5 = Monomial("-1")
    p2 = Polynomial([m4,m5])

    m6 = Monomial("y^2")
    m7 = Monomial("-1")
    p3 = Polynomial([m6, m7])

    # p1 = Polynomial([Monomial("x^2")])
    # p2 = Polynomial([Monomial('3*x^4'), Monomial('y^2')])
    # p3 = Polynomial([Monomial('y')])

    order = MonomialOrder('xy','lex')

    quotients, remainder = long_divide(p1,[p2, p3],order)
    [print(q.ordered_str(order)) for q in quotients]
    print(remainder.ordered_str(order))