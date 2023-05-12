class Monomial:

    def __init__(self, str_representation):
        """
        Use ^ for powers and * for multiplication
        E.g. 5*x^3*y*z^2
        Part without a letter variable is treated as the coefficient
        """
        self.str_representation = str_representation
        parts = str_representation.split('*')
        # store the variables and their powers in a dict
        self.vars = {}
        self.coefficient = 1
        for part in parts:
            if part.isdecimal():
                self.coefficient = int(part)
            else:
                if '^' in part:
                    var, power = part.split('^')
                    self.vars[var] = int(power)
                else:
                    self.vars[part] = 1


    def get_coefficient(self):
        return self.coefficient


    def vars(self):
        return self.vars.copy()


    def total_degree(self):
        degree = 0
        for power in self.vars.values():
            degree += power
        return degree


    def __str__(self):
        return self.str_representation


# for testing
if __name__ == '__main__':
    string = "5*x^3*y*z*x_0^7"
    m = Monomial(string)
    print(m)
    print(m.vars)
    print(m.total_degree())
    print(m.get_coefficient())



