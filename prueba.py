from vector import Vector
from matrix import Matrix


a = Matrix([[1, 2, 2], [2, 3, 1]])
b = Matrix([[1, 1], [2, 1], [2, 1]])
v = Vector([1, 1, 1])

m = a * b

print(m)