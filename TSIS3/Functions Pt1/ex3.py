import numpy
def chickandrab(n, m):
    M = numpy.array([[1, 1], [2, 4]])
    V = numpy.array([n, m])
    return numpy.linalg.solve(M, V)
n = 35
m = 94
print(chickandrab(n, m))