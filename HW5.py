def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Rational:

    def __init__(self, n, m):
        if m == 0:
            raise ValueError('Zero dominator')
        elif m < 0:
            n, m = -n, -m
        g = gcd(n, m)
        self.n, self.m = n // g, m // g

    def __str__(self):
        return f'{self.n}/{self.m}'

    @classmethod
    def parse_from_str(cls, string):
        if string[0] == '-':
            n, m = string[1:].split('/')
        else:
            n, m = string.split('/')
        n, m = int(n), int(m)
        if string[0] == '-':
            n = -n
        return cls(n, m)

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n * other.m + self.m * other.n, self.m * other.m)
        else:
            return Rational(self.n + other * self.m, self.m)

    def __neg__(self):
        return Rational(-self.n, self.m)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.m * other.m)
        else:
            return Rational(self.n * other, self.m)

    def inv(self):
        return Rational(self.m, self.n)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return self * other.inv()
        else:
            return Rational(self.n, self.m * other)

    def __float__(self):
        return self.n / self.m


def test_operations():
    x = Rational(14, 128)
    y = Rational(15, 7)

    z = x + y
    assert str(z) == '1009/448'

    z = x - y
    assert str(z) == '-911/448'

    z = x * y
    assert str(z) == '15/64'

    z = x / y
    assert str(z) == '49/960'


def test_cast_to_float():
    x = Rational(1, 8)
    float_x = float(x)
    assert float_x == 0.125


def test_parse_from_string():
    x = Rational.parse_from_str('5/10')
    assert x.n == 1
    assert x.m == 2


if __name__ == '__main__':
    test_operations()
    test_cast_to_float()
    test_parse_from_string()
