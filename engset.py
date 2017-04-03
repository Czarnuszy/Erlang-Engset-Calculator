from utils import newton, precision2
from decimal import *

class EngsetAlgorithm:
    def __init__(self, model):
        self.obj = model

    def get_obj_data(self):
        """
        Getting data from object
        :return: lines, traffic, blocking_rate
        """
        data = (self.obj.lines,
                self.obj.traffic,
                self.obj.blocking_rate,
                self.obj.sources)
        return data

    def calculate(self):
        """
        Checks which parameter is false and call right function
        """
        lines, traffic, block, sources = self.get_obj_data()

        if block is False:
            return self.calculate_p(lines, traffic, sources)

    def calculate_p(self, lines, traffic, sources):
        Pb = 0

        def calc():
            a = traffic / (sources - traffic * (1 - Pb))
            l = newton(sources-1, lines) * (a ** lines)
            sum = 0

            for i in range(lines):
                sum += newton(sources-1, i) * (a ** i)
            return l / sum

        right = calc()

        while Pb != right:
            Pb += .0001
            right = precision2(right, 4)
            Pb = precision2(Pb, 4)

        return Pb