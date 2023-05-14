class Monomial:

    def __init__(self, str_representation):
        """
        Use ^ for powers and * for multiplication
        E.g. 5*x^3*y*z^2
        Part without a letter variable is treated as the coefficient
        """
        self.str_representation = str_representation
        # store the variables and their powers in a dict
        self.vars = {}
        self.coefficient = 1
        negative = False
        if str_representation.startswith('-'):
            negative = True
            str_representation = str_representation[1:]
        parts = str_representation.split('*')
        for part in parts:
            if part.isdecimal():
                self.coefficient = int(part)
            else:
                if '^' in part:
                    var, power = part.split('^')
                    self.vars[var] = int(power)
                else:
                    self.vars[part] = 1
        if negative:
            self.coefficient = -self.coefficient



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


    def __eq__(self, other):
        return self.vars == other.vars and self.coefficient == other.coefficient


# for testing
if __name__ == '__main__':
    string = "5*x^5*y^4*z"
    string2 = "-y*z^2"
    m = Monomial(string)
    m2 = Monomial(string2)
    # print(difference_vector("xyz", m, m2))
    print(m)
    print(m.vars)
    print(m.total_degree())
    print(m.get_coefficient())
    print("--------")
    print(m2)
    print(m2.vars)
    print(m2.total_degree())
    print(m2.get_coefficient())



