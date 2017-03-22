from math import factorial


class ErlangAlgorithm():

    def __init__(self, model):
        self.obj = model

    def show(self):
        print(self.obj.users)

    def get_obj_lines_and_traffic(self):
        """
        Getting data from object
        :return: lines, traffic, blocking_rate
        """
     #   return self.obj.lines, self.obj.users * self.obj.block, self.obj.blocking_rate
        return self.obj.lines, self.obj.traffic, self.obj.blocking_rate

    def calculate(self):
        """
        Checks which parameter is false and call right function
        """
        n, a, p = self.get_obj_lines_and_traffic()

        if p is False:
            return self.calculate_erlang_p(a, n)
        elif n is False:
            return self.calculate_erlang_n(a, p)
        elif a is False:
            pass

    def calculate_erlang_p(self, a, n):
        """
        Default erlang algorithm, calculate blocking rate
        :param a: the traffic in Erlangs
        :param n: the number of lines
        :return: blocking rate
        """
        tab = [x for x in range(n+1)]

        _sum = 0
        for idx, val in enumerate(tab):
            _sum += self.ann(idx, a)

        p = self.ann(n, a) / _sum

        return p

    def calculate_erlang_n(self, a, p):
        """
        calculate the number of lines in a trunk group
        :param a: the traffic in Erlangs
        :param p: blocking rate
        :return: number of lines
        """
        _n = 1

        p_search = self.calculate_erlang_p(a, _n)
        while p_search >= p:
            _n += 1
            p_search = self.calculate_erlang_p(a, _n)

        return _n-1

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
