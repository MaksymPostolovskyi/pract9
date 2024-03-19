class Begin():
    pass

class BI(Begin):
    def set_message(self):
        pass
        
    def result(self):
            return print("Big")
        
class M(Begin):
    def set_message(self):
        pass
        
    def result(self):
            return print("Men")

class C(Begin):
    def set_message(self):
        pass
        
    def result(self):
            return print("Cat")
        
class T(BI):
    def set_message(self):
        pass
        
    def result(self):
            return print("Bitter")
        
class E(M, C, BI):
    def set_message(self):
        pass
        
    def result(self):
            return print("Women")
        
class A(C):
    pass
        
class R(T, E):
    pass

class N(E, A):
    pass

R = R()
R.set_message()
R.result()
N = N()
N.set_message()
N.result()