# make a class named X that is-a Y
class X(Y)

# class X has-a __init__ that takes self and J parameters
class X(object):
    def __init__(self, J)

# class X has-a function named M that takes self and J parameters
class X(object):
    def M(self, J)

# set foo to an instance of class X
foo = X()

# from foo get the M funcion, and call it with parameters self, J
foo.M(J)

# from foo get the K attribute and set it to Q
foo.K = Q
