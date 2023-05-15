class Monomial:

    def __init__(self, *args):
        # it's not our fault python doesn't allow constructor overloading
        if len(args) > 1:
            self.dict_init(args[0], args[1])
        else:
            self.str_init(args[0])


    def str_init(self, str_representation):
        """
        Use ^ for powers and * for multiplication
        E.g. 5*x^3*y*z^2
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
        return self.coefficient


    def get_vars(self):
        return self.vars.copy()


    def total_degree(self):
        degree = 0
        for power in self.vars.values():
            degree += power
        return degree


    def __str__(self):
        return self.str_representation
    
    def __hash__(self):
        return hash(self.str_representation)


    def ordered_str(self, variable_order):
        """
        :param variable_order: eg "xyz"
        :return: string representation of monomial with its variables in order
        """
        if self == Monomial("1"):
            # cosmic joke
            return '1'
        parts = [str(self.coefficient)] if self.coefficient != 1 else []
        for var in variable_order:
            if var in self.vars:
                power = self.vars[var]
                new = str(var) if power == 1 else f"{var}^{power}"
                parts.append(new)
        ret = '*'.join(parts)
        # get rid of -1 coefficient. There's probably a better way to do this but whatever
        if ret.startswith("-1*"):
            ret = "-" + ret[3:]
        return ret


    def __eq__(self, other):
        return self.vars == other.vars and self.coefficient == other.coefficient

def like_terms(m1, m2):
    return m1.get_vars() == m2.get_vars()



def is_float(string):
    # we apologize
    # on behalf of pythonhow.com
    try:
        float(string)
        return True
    except ValueError:
        return False

def divides(divisor, dividend):
    if not (set(divisor.get_vars().keys()) <= set(dividend.get_vars().keys())):
        return False
    for var in divisor.get_vars():
        divisor_power = divisor.get_vars()[var]
        dividend_power = dividend.get_vars()[var]
        if divisor_power > dividend_power:
            return False
    return True

def divide(dividend, divisor):
    quotient_coeff = dividend.get_coefficient() / divisor.get_coefficient()
    quotient_vars = {}
    for var in dividend.get_vars():
        dividend_power = dividend.get_vars()[var]
        if var in divisor.get_vars():
            divisor_power = divisor.get_vars()[var]
            new_power = dividend_power - divisor_power
            quotient_vars[var] = new_power
        else:
            quotient_vars[var] = dividend_power
    return Monomial(quotient_vars, quotient_coeff)

def multiply(m1, m2):
    prod_coeff = m1.get_coefficient() * m2.get_coefficient()
    prod_vars = m1.get_vars()
    for var, power in m2.get_vars().items():
        if var in prod_vars:
            prod_vars[var] += power
        else:
            prod_vars[var] = power
    return Monomial(prod_vars, prod_coeff)



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
    print(multiply(m1,m2))
    # m2 = Monomial('y')
    # m3 = Monomial('5*x^3')
    # print(divides(m1,m2))
    # print(divides(m1, m3))
    # print(divides(m3,m1))
    # print(divide(m3,m1))
    # m4 = multiply(m1,m2)
    # print(multiply(m3,m4))
    # print(multiply(m4,m3))
    


