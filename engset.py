from utils import newton, precision


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
        elif lines is False:
            return self.calculate_n(traffic, block, sources)
        elif traffic is False:
            return self.calculate_a(lines, block, sources)

    def basic_engset(self, lines, traffic, Pb, sources):
        """
        :return: blocking rate when you know blocking rate
        Used in loops when looking for another params
        """
        a = traffic / (sources - traffic * (1 - Pb))
        l = newton(sources - 1, lines) * (a ** lines)
        sum = 0

        for i in range(lines):
            sum += newton(sources - 1, i) * (a ** i)
        return l / sum

    def calculate_p(self, lines, traffic, sources):
        """
        engset, calculate blocking rate
        :param lines: number of servers
        :param traffic: the traffic in Erlangs
        :param sources: the number of points generating the traffic
        :return: blocking rate
        """
        block = 0
        right = self.basic_engset(lines, traffic, block, sources)
        while block != right:
            block += .0001
            right = precision(right, 4)
            block = precision(block, 4)

        return block

    def calculate_n(self, traffic, block, sources):
        """
        :param traffic: the traffic in Erlangs
        :param block: blocking rate
        :param sources: the number of points generating the traffic
        :return: number of servers
        """
        lines = 1
        p_search = self.basic_engset(lines, traffic, block, sources)
        while p_search >= block:
            lines += 1
            p_search = self.basic_engset(lines, traffic, block, sources)

        return lines - 1

    def calculate_a(self, lines, block, sources):
        """
        :param lines:  number of servers
        :param block:  blocking rate
        :param sources: the number of points generating the traffic
        :return: the traffic in Erlangs
        """
        traffic = 0
        p_search = self.basic_engset(lines, traffic, block, sources)

        while p_search <= block:
            traffic += .1
            p_search = self.basic_engset(lines, traffic, block, sources)

        return traffic
