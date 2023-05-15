class Monomial:

    def __init__(self, *args):
        # it's not our fault python doesn't allow constructor overloading
        if len(args) > 1:
            self.dict_init(args[0], args[1])
        else:
            self.str_init(args[0])


    def str_init(self, str_representation):
        """
        Initialize a Monomial using a string
        Use ^ for powers and * for multiplication
        :param str_representation: E.g. "5*x^3*y*z^2"
        Part without a letter variable is treated as the coefficient
        """
        self.str_representation = str_representation
        if self.str_representation == '0':
            self.coefficient = 0
            self.vars = {}
            return
        # store the variables and their powers in a dict
        self.vars = {}
        self.coefficient = 1
        # parse string input
        negative = False
        if str_representation.startswith('-'):
            negative = True
            str_representation = str_representation[1:]
        parts = str_representation.split('*')
        for part in parts:
            if is_float(part):
                self.coefficient = float(part)
            else:
                if '^' in part:
                    var, power = part.split('^')
                    self.vars[var] = int(power)
                else:
                    self.vars[part] = 1
        if negative:
            self.coefficient = -self.coefficient


    def dict_init(self, vars, coefficient):
        """
        Alternative initialization where vars and coefficient attributes are directly provided
        :param vars: dict
        :param coefficient: float
        :return:
        """
        self.vars = {}
        for var in vars:
            if vars[var] != 0:
                self.vars[var] = vars[var]
        self.coefficient = coefficient
        if self.coefficient == 0:
            self.str_representation = '0'
            self.vars = {}
            return
        self.str_representation = str(coefficient) + "*" + "*".join([f"{key}^{value}" for key, value in vars.items()])


    def get_coefficient(self):
        """
        :return: the coefficient
        """
        return self.coefficient

    def get_vars(self):
        """
        :return: the {variable: power} dictionary
        """
        return self.vars.copy()

    def total_degree(self):
        """
        Calculates the total degree of the monomial
        :return: int
        """
        degree = 0
        for power in self.vars.values():
            degree += power
        return degree

    def __str__(self):
        return self.str_representation
    
    def __repr__(self):
        return self.str_representation
    
    def __hash__(self):
        """
        Necessary to put Monomials in a set
        """
        return hash(self.str_representation)
    
    def __mul__(self, other):
        """
        Multiplies Monomials
        :param other: a second Monomial
        :return: the product of the Monomials, a new Monomial
        """
        prod_coeff = self.get_coefficient() * other.get_coefficient()
        prod_vars = self.get_vars()
        for var, power in other.get_vars().items():
            if var in prod_vars:
                prod_vars[var] += power
            else:
                prod_vars[var] = power
        return Monomial(prod_vars, prod_coeff)
    
    def __truediv__(self, other):
        """
        Divides Monomials. Should not be called without checking divisibility
        :param other: a second Monomial
        :return: the results of dividing the Monomials, a new Monomial
        """
        quotient_coeff = self.get_coefficient() / other.get_coefficient()
        quotient_vars = {}
        for var in self.get_vars():
            dividend_power = self.get_vars()[var]
            if var in other.get_vars():
                divisor_power = other.get_vars()[var]
                new_power = dividend_power - divisor_power
                quotient_vars[var] = new_power
            else:
                quotient_vars[var] = dividend_power
        return Monomial(quotient_vars, quotient_coeff)


    def ordered_str(self, variable_order):
        """
        :param variable_order: eg "xyz"
        :return: string representation of monomial with its variables in order
        """
        # make floats for sake of consistency
        if self == Monomial("1"):
            # cosmic joke
            return '1.0'
        if self == Monomial("0"):
            # cosmic joke pt 2
            return '0.0'
        parts = [str(self.coefficient)] if self.coefficient != 1 else []
        for var in variable_order:
            if var in self.vars:
                power = self.vars[var]
                new = str(var) if power == 1 else f"{var}^{power}"
                parts.append(new)
        ret = '*'.join(parts)
        # get rid of -1 coefficient
        if ret.startswith("-1*"):
            ret = "-" + ret[3:]
        elif ret.startswith("-1.0*"):
            ret = "-" + ret[5:]
        return ret


    def __eq__(self, other):
        """
        Monomials are equal if their variables, powers, and coefficients are all the same
        :param other: the second Monomial
        :return: boolean
        """
        return self.vars == other.vars and self.coefficient == other.coefficient

def like_terms(m1, m2):
    """
    Determines if two Monomials are like terms
    :param m1: Monomial
    :param m2: Monomial
    :return: boolean
    """
    return m1.get_vars() == m2.get_vars()


def is_float(string):
    """
    Hacky way of figuring out whether a string is a coefficient when parsing the monomial string, since coefficients
    need not be integers
    :param string: a string, e.g. "1.0" or "x^7"
    :return: boolean
    """
    # we apologize on behalf of pythonhow.com
    try:
        float(string)
        return True
    except ValueError:
        return False

def divides(divisor, dividend):
    """
    Checks divisibility of two Monomials
    :param divisor: Monomial
    :param dividend: Monomial
    :return: boolean
    """
    if not (set(divisor.get_vars().keys()) <= set(dividend.get_vars().keys())):
        return False
    for var in divisor.get_vars():
        divisor_power = divisor.get_vars()[var]
        dividend_power = dividend.get_vars()[var]
        if divisor_power > dividend_power:
            return False
    return True


# for testing
if __name__ == '__main__':
    # string = "5*x^5*y^4*z"
    # string2 = "-y*z^2"
    # m = Monomial(string)
    # m2 = Monomial(string2)
    # order = "zyx"
    # print(m.ordered_str(order))
    # print(m2.ordered_str(order))
    # print(difference_vector("xyz", m, m2))
    # print(m)
    # print(m.vars)
    # print(m.total_degree())
    # print(m.get_coefficient())
    # print("--------")
    # print(m2)
    # print(m2.vars)
    # print(m2.total_degree())
    # print(m2.get_coefficient())
    m1 = Monomial('2*x')
    m2 = Monomial('-1')
    # print(multiply(m1,m2))
    # m2 = Monomial('y')
    # m3 = Monomial('5*x^3')
    # print(divides(m1,m2))
    # print(divides(m1, m3))
    # print(divides(m3,m1))
    # print(divide(m3,m1))
    # m4 = multiply(m1,m2)
    # print(multiply(m3,m4))
    # print(multiply(m4,m3))
    


