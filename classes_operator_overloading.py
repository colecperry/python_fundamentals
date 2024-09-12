class Fraction:
    '''Attributes:
    num: the numerator int
    den: the denominator int - nonzero
    num/den is reduced to the lowest terms
    '''
    def gcd(a,b):
        a = abs(a)
        b = abs(b)
        r = a%b
        while r>0:
            a = b
            b = r
            r = a%b
        return b
    
    def __init__(self, p, q=1):
        # Run the gcd function from the fraction class and store the gcd in d
        d = Fraction.gcd(p,q)
        # Divide the numerator and denominator by the gcd to reduce the fraction to it's lowest terms
        self.num = p/d
        self.den = q/d
    
    def __add__(self, f):
        N = self.num * f.den + self.den * f.num
        D = self.den * f.den
        return Fraction(N,D)
    
    def __mul__(self, f):
        N = self.num * f.num
        D = self.den * f.den
        return Fraction(N,D)


A = Fraction(2,3)
B = Fraction(1,4)
# Operator overloading - can say A + B and it will run the add function (A.__add__(B))
C = A + B
print(C.num, C.den)

D = A * B
print(D.num, D.den)

# isinstance
print(isinstance(A, Fraction))



