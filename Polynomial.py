import functools
from Monomial import Monomial # for testing
from MonomialOrder import MonomialOrder # also for testing


class Polynomial:


    def __init__(self, monomials):
        """
        :param monomials: list of Monomials
        """
        self.terms = monomials


    def reorder(self, monomial_order):
        self.terms = sorted(self.terms, key=functools.cmp_to_key(monomial_order.compare), reverse=True)


    def leading_term(self, monomial_order):
        """
        :return: returns the leading term, a Monomial
        """
        self.reorder(monomial_order)
        return self.terms[0]


    def ordered_str(self, monomial_order):
        self.reorder(monomial_order)
        ret = "+".join([term.ordered_str(monomial_order.get_variable_order()) for term in self.terms])
        ret = ret.replace("+-", "-")
        return ret


if __name__ == "__main__":
    string = "5*x^5*y^4*z"
    string2 = "-y*z^2"
    m = Monomial(string)
    m2 = Monomial(string2)
    p = Polynomial([m, m2])
    order = MonomialOrder("xyz", "lex")
    lt = p.leading_term(order)
    print(lt.ordered_str("xyz"))
    print(p.ordered_str(order))