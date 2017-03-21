from math import factorial


class ErlangAlgorithm():

    def __init__(self, model):
        self.obj = model

    def show(self):
        print(self.obj.users)

    def get_obj_lines_and_traffic(self):
       # print(self.obj.users, self.obj.block, self.obj.traffic)
        return self.obj.lines, self.obj.users * self.obj.block

    def calculate(self):
        """
        Default algorithm for small numbers
        :return: blocking rate
        """
        n, a = self.get_obj_lines_and_traffic()

        tab = [x for x in range(n+1)]
        exponent = a ** n
        b = factorial(n)

        c = 0

        for idx, val in enumerate(tab):
            c += (a ** idx) / factorial(idx)

        d = exponent / b / c
        print(d)
        return d