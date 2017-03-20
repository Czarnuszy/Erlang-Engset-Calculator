class ErlangAlgorithm():

    def __init__(self, model):
        self.obj = model

    def silnia(self, n):
        if n > 1:
            return n * self.silnia(n - 1)
        else:
            return 1

    def show(self):
        print(self.obj.users)

    def calculate(self):
        N = self.obj.servers
        B = self.obj.block
        A = self.obj.users * self.obj.blocking_rate
        tab = [x for x in range(N+1)]
        a = A ** N
        b = self.silnia(N)

        c = 0

        for idx, val in enumerate(tab):
            c += (A ** idx) / self.silnia(idx)

        d = a / b / c
        print(d)
        return d