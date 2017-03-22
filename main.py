import math
from erlang import ErlangAlgorithm


class MakeUpSomething():
    """
    Model dla wspolczynnika blokady

    users = amount of users / the mean call length or holding time
    lines =  the number of lines in a trunk group / liczba punktow obslugi
    blocking_rate = wspolczynnik blokady

    block = the mean arrival rate of new calls
    traffic = the traffic in Erlangs = users * block

    """
    def __init__(self, users, lines, blocking_rate, block=0.1):
        self.block = block

        self.users = users
        self.lines = lines
        self.blocking_rate = blocking_rate
        self.traffic = self.users * self.block #bussy hour traffic
        self.unknown_value = []

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        self.traffic = value * self.block
        self._users = value


obj = MakeUpSomething(34, 10, False)

algo = ErlangAlgorithm(obj)

print(algo.calculate())

obj.blocking_rate = 0.0019
obj.lines = False

print(algo.calculate())




# obj.users = 5000
# obj.lines = 400
# algo.calculate()
#
