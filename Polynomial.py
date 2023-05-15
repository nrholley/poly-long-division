import functools
from Monomial import Monomial, like_terms, multiply # for testing
from MonomialOrder import MonomialOrder # also for testing
from copy import copy


class Polynomial:


    def __init__(self, monomials):
        """
        :param monomials: list of Monomials
        """
        self.terms = combine_terms(monomials)

    def get_terms(self):
        return copy(self.terms)

    def reorder(self, monomial_order):
        self.terms = sorted(self.terms, key=functools.cmp_to_key(monomial_order.compare), reverse=True)


    def leading_term(self, monomial_order):
        """
        :return: returns the leading term, a Monomial
        """
        self.reorder(monomial_order)
        return self.get_terms()[0]


    def ordered_str(self, monomial_order):
        self.reorder(monomial_order)
        ret = " + ".join([term.ordered_str(monomial_order.get_variable_order()) for term in self.terms])
        ret = ret.replace("+ -", "- ")
        return ret
    
    def __eq__(self, other):
        self_terms = set(self.terms)
        other_terms = set(other.terms)
        return self_terms == other_terms


def combine_terms(terms):
        new_terms = []
        combined = []
        for i, m1 in enumerate(terms):
            if m1 not in combined:
                term_group = [m1]
                for m2 in terms[i+1:]:
                    if m2 not in combined:
                        if like_terms(m1, m2):
                            term_group.append(m2)
                            combined.append(m2)
                new_coefficient = sum([m.coefficient for m in term_group])
                new_vars = m1.get_vars()
                new_monomial = Monomial(new_vars, new_coefficient)
                new_terms.append(new_monomial)
        return new_terms

def poly_multiply(p1, p2):
    prod_terms = []
    for term1 in p1.get_terms():
        for term2 in p2.get_terms():
            prod_term = multiply(term1, term2)
            prod_terms.append(prod_term)
    return Polynomial(prod_terms)

def poly_add(p1, p2):
    return Polynomial(p1.get_terms() + p2.get_terms())

if __name__ == "__main__":
    # string = "5*x^5*y^4*z"
    # string2 = "y^2*z^9"
    # string3 = "x^3*z^8"
    # string4 = "2"
    # string5 = "0"

    # m = Monomial(string)
    # m2 = Monomial(string2)
    # m3 = Monomial(string3)
    # m4 = Monomial(string4)
    # m5 = Monomial(string5)
    # p = Polynomial([m, m2, m3, m4, m5])

    # lt = p.leading_term(order)
    # print(lt.ordered_str("xyz"))

    # m1 = Monomial("5.3*x^2*y^2")
    # m2 = Monomial("-3*x^2*y^2")
    # m3 = Monomial({'x':1,'y':1},1)
    # p = Polynomial([m1,m2,m3])
    
    # order = MonomialOrder("xyz", "lex")
    # print(p.ordered_str(order))

    p1 = Polynomial([Monomial('2*x')])
    p2 = Polynomial([Monomial('3*y^2')])
    [print(m) for m in poly_multiply(p1,p2).get_terms()]
    [print(m) for m in poly_multiply(p2,p1).get_terms()]
    [print(m) for m in poly_add(p1,p2).get_terms()]