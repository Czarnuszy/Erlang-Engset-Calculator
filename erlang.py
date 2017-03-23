from math import factorial


class ErlangAlgorithm:

    def __init__(self, model):
        self.obj = model

    def get_obj_lines_and_traffic(self):
        """
        Getting data from object
        :return: lines, traffic, blocking_rate
        """
        return self.obj.lines, self.obj.traffic, self.obj.blocking_rate

    def calculate(self):
        """
        Checks which parameter is false and call right function
        """
        lines, traffic, block = self.get_obj_lines_and_traffic()

        if block is False:
            return self.calculate_erlang_p(traffic, lines)
        elif lines is False:
            return self.calculate_erlang_n(traffic, block)
        elif traffic is False:
            return self.calculate_erlang_a(lines, block)

    def calculate_erlang_p(self, traffic, lines):
        """
        Default erlang algorithm, calculate blocking rate
        :param traffic: the traffic in Erlangs
        :param lines: the number of lines
        :return: blocking rate
        """
        tab = [x for x in range(lines + 1)]

        _sum = 0
        for idx, val in enumerate(tab):
            _sum += self.ann(idx, traffic)

        Pb = self.ann(lines, traffic) / _sum

        return format(Pb, self.precision(Pb))

    def precision(self, number):
        amount = 0
        for n in str(number):
            if n == '0':
                amount += 1
            elif n == '.':
                continue
            else:
                break
        return '.{}f'.format(amount+1)

    def calculate_erlang_n(self, traffic, Pb):
        """
        calculate the number of lines in a trunk group
        :param traffic: the traffic in Erlangs
        :param Pb: blocking rate
        :return: number of lines
        """
        lines = 1
        p_search = Pb
        while p_search >= Pb:
            lines += 1
            p_search = self.calculate_erlang_p(traffic, lines)

        return lines-1

    def calculate_erlang_a(self, n, Pb):
        """
        calculate traffic in erlangs
        :param n: the number of lines
        :param Pb: blocking rate
        :return: number of lines
        """

        return "Not implemented yet. Sorry"

    def ann_small(self, n, a):
        """
        Default  a^n / n! algorithm for small numbers
        :param n: lines
        :param a: traffic
        :return: a^n / n!
        """
        exponent = a ** n
        b = factorial(n)
        return exponent/b

    def ann(self, n, a):
        """
        a^n / n! algorithm for big numbers
        :param n: lines
        :param a: traffic
        :return: a^n / n!
        """
        result = 1
        for n in range(1, n + 1):
            result = result * a / n

        return result
