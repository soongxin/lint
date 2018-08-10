class A(object):
    def doprint(self):
        print('--A--')

print(A.__mro__)


class B(A):
    def doprint(self):
        super(B, self).doprint()
        print('--B--')

print(B.__mro__)
class C(A, B):
    def doprint(self):
        super(C, self).doprint()
        super(B, self).doprint()
        print('--C--')

print(C.__mro__)



