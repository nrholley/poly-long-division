from Monomial import Monomial # for testing
import functools


class MonomialOrder:

    def __init__(self, variable_order, order_name):
        self.variable_order = variable_order
        self.order_name = order_name

    def difference_vector(self, a, b):
        """
        :param variables: the variables, in order, string format. E.g. "xyz"
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
        if self.order_name == "lex":
            diff = self.difference_vector(a, b)
            for num in diff:
                if num != 0:
                    return num
            return 0
        raise NotImplementedError


if __name__ == "__main__":
    string = "5*x^5*y^4*z"
    string2 = "-y*z^2"
    m = Monomial(string)
    m2 = Monomial(string2)
    order = MonomialOrder("xyz", "lex")
    monlist = [m2, m]
    for mon in monlist:
        print(mon)
    print("--------")
    for mon in sorted(monlist, key=functools.cmp_to_key(order.compare), reverse=True):
        print(mon)