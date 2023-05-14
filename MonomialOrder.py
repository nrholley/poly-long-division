class MonomialOrder:

    def __init__(self, variable_order):
        self.variable_order = variable_order


    def less_than(self, a, b):
        pass


    def greater_than(self, a, b):
        pass


    def equal(self, a, b):
        pass


class LexOrder:

    def __init__(self):
        super.__init__()


    def less_than(self, a, b):
        for var in self.variable_order:
            pass