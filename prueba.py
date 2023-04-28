from vector import Vector
from matrix import Matrix


A = Matrix([
    [1, 2, 3, 1], 
    [1, 3, 3, 1], 
    [1, 2, 4, 1],
    [2, 3, 5, 8]
])

B = Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# C = A.multPartes(B, 2)
print(Matrix.zeros(4, 2))