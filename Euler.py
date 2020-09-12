"""
(3) Given the differential equation f'(x) = x^x, write a function that uses Euler's method to approximate the value of
f(x1) given an initial condition (x0, f(x0)) and the value of x1.
"""
import unittest
class eulers_method(unittest.TestCase):
    def eulers_method(self, x1: float, initial_x: float, initial_f_of_x: float, step: float, derivative_f_x: callable):
        if (x1 - initial_x) % step != 0:
            return None

        x = initial_x
        y = initial_f_of_x
        rate_of_change = derivative_f_x(x, y)

        while x < x1:
            y += rate_of_change
            x += step
            rate_of_change = derivative_f_x(x, y)

        return y

    def test_eulers_method(self):
        def fun_1(x, y): return y
        self.assertEqual(self.eulers_method(x1=3, initial_x=0, initial_f_of_x=1, step=1, derivative_f_x=fun_1), 8)
        def fun_2(x,y): return x**2
        self.assertEqual(self.eulers_method(x1=4, initial_x=0, initial_f_of_x=1, step=1, derivative_f_x=fun_2), 15)

    def test_impossible_step(self):
        def fun_2(x,y): return x**2
        self.assertEqual(self.eulers_method(x1=1.5, initial_x=1, initial_f_of_x=1, step=(1/3), derivative_f_x=fun_2), None)

if __name__ == '__main__':
    unittest.main()