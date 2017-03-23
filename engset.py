
class Engset:

    def newton(self, n, k):
        if k == 0 or k == n:
            return 1
        else:
            return float(n) / k * self.newton(n - 1, k - 1)