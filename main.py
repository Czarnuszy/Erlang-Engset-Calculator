import math
from erlang import ErlangAlgorithm


class MakeUpSomething():
    """
    Model dla wspolczynnika blokady

    blocking_rate = the mean arrival rate of new calls
    users = the mean call length or holding time
    traffic = the traffic in Erlangs.

    serves = liczba punktow obslugi

    block = wspolczynnik blokady
    """
    def __init__(self, users, servers, block, blocking_rate=0.1):
        """
        :param users: Amount of user's using web
        :param servers: Amount of service points
        :param block: Wspolczynnik blokady
        :param blocking_rate: the mean arrival rate of new calls
        """
        self.users = users
        self.blocking_rate = blocking_rate
        self.servers = servers
        self.block = block
        self.traffic = self.users * self.blocking_rate #bussy hour traffic
        self.unknown_value = []

    def set_users(self, new_users):
        self.users = new_users

    def set_servers(self, new_servers):
        self.servers = new_servers

    def set_block(self, new_block):
        self.block = new_block

    def set_blocking_rate(self, new_rate):
        self.blocking_rate = new_rate

    def set_custom_traffic(self, new_traffic):
        self.traffic = new_traffic


def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    else:
        return 1
#
# N = 10
# B = 0.002
# A = 3.42
#
# tab = [x for x in range(N+1)]
# print(tab)
# a = A**N
# b = silnia(N)
#
# c = 0
#
# for idx, val in enumerate(tab):
#
#     c += (A**idx)/silnia(idx)
#     print('{} = {} do potegi {} podzielic przez {}'.format(c, val, idx, silnia(idx)))
#
# d = a/b/c
# print(d)
#
#
# b = 0.4510370834892845

obj = MakeUpSomething(100, 10, False)

algo = ErlangAlgorithm(obj)

algo.calculate()

obj.set_users(200)
algo.calculate()
