from utils import newton


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
        l = newton(sources-1, lines) * (traffic ** lines)
        sum = 0

        for i in range(lines):
            sum += newton(lines-1, i) * (sources ** i)

        return l/sum