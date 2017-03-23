import math
from erlang import ErlangAlgorithm


class MakeUpSomething:
    """
    Model for ErlangB algorithm

    users = amount of users / the mean call length or holding time
    lines =  the number of servers(lines) in a trunk group / liczba punktow obslugi
    blocking_rate = Probability of blocking

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

    def calculate_traffic_per_hour(self, calls, duration, seconds=True):
        """ Calculate the total traffic volume of one hour.
        :param calls: amount of calls made in hour
        :param duration: average duration time in seconds or minutes
        :param seconds: If duration in seconds set True, if in minutes set as False
        :return: Erlang traffic representation
        """
        if seconds:
            return calls*duration/3600
        return calls*duration/60

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        if value is False:
            self.traffic = False
        else:
            self.traffic = value * self.block
        self._users = value


obj = MakeUpSomething(users=17.986, lines=False, blocking_rate=0.01)
obj.traffic = 17.986
algo = ErlangAlgorithm(obj)
#print(obj.calculate_traffic_per_hour(350, 180))

print(algo.calculate())
#
# obj.blocking_rate = 0.0019
# obj.lines = False
#
# print(algo.calculate())
#
# obj.traffic = False
# obj.lines = 10
# print(algo.calculate())



# obj.users = 5000
# obj.lines = 400
# algo.calculate()
#
