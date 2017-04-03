import unittest
from main import Model


class Tests(unittest.TestCase):

    def setUp(self):
        self.model_p = Model(traffic=3.4, lines=10, blocking_rate=False)
        self.model_n = Model(traffic=3.4, lines=False, blocking_rate=0.0019)
        self.model_a = Model(traffic=False, lines=10, blocking_rate=0.0019)

    def test_erlang_p(self):
        self.assertEqual(self.model_p.calculate_erlang(), '0.0019')

    def test_erlang_n(self):
        self.assertEqual(self.model_n.calculate_erlang(), 10)

    def test_erlang_a(self):
        self.assertEqual(self.model_a.calculate_erlang(), 3.5)

if __name__ == '__main__':
    unittest.main()