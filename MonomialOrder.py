from Monomial import Monomial # for testing
import functools


def lex_compare(diff):
    for num in diff:
        if num != 0:
            return num
    return 0


class MonomialOrder:


    def __init__(self, variable_order, order_name):
        self.variable_order = variable_order
        self.order_name = order_name


    def difference_vector(self, a, b):
        """
        :param a: first monomial
        :param b: second monomial
        :return: tuple of the differences of variable powers, corresponding to alpha - beta in the textbook/handout
        """
        diff = []
        for v in self.variable_order:
            a_vars = a.get_vars()
            b_vars = b.get_vars()
            a_pow = a_vars[v] if v in a_vars else 0
            b_pow = b_vars[v] if v in b_vars else 0
            diff.append(a_pow - b_pow)
        return tuple(diff)

    def compare(self, a, b):
        """
        :param a: first monomial
        :param b: second
        :return: positive # if a > b, negative # if a < b, 0 if a == b
        """
        diff = self.difference_vector(a, b)
        if self.order_name == "lex":
            return lex_compare(diff)
        degree_diff = a.total_degree() - b.total_degree()
        if degree_diff:
            return degree_diff
        if self.order_name == "grlex":
            return lex_compare(diff)
        if self.order_name == "grevlex":
            for num in diff[::-1]:
                if num != 0:
                    return -num
                return 0
        raise Exception("What the hell happened?")


    def get_variable_order(self):
        return self.variable_order


if __name__ == "__main__":
    # TODO: MORE TESTING
    string = "5*x^4*y^3*z^3"
    string2 = "-x^5*y*z^4"
    m = Monomial(string)
    m2 = Monomial(string2)
    m3 = Monomial("x^4*y^3*z^3")
    order = MonomialOrder("zyx", "grevlex")
    monlist = [m, m2, m3]
    for mon in monlist:
        print(mon)
    print("--------")
    for mon in sorted(monlist, key=functools.cmp_to_key(order.compare), reverse=True):
        print(mon)