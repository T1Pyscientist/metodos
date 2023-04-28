from vector import Vector



# TODO: eliminar redondeo en reduce()
#       implementar .Traspose
#       implementar .Determinant
#       implementar .Inverse 
#       implementar Matriz Identidad metodo static
#       gurdar componentes en .components pero acceder con [] operator
#       mejorar repr


class Matrix(object):
    """ Implementacion de clase Matriz

    Parameters
    ----------
    valores : list[list[float, int]]
        Valores de los componentes para inicializar la matriz.
        Es una lista de listas, donde el primer elemento es la primer fila, el segundo elemento la segunda fila..
        Notar que las listas deben ser del mismo largo

    Attributes
    ----------
    componentes : list[list]
        Componentes de la matriz

    dimension : tuple
        Dimensiones de la matriz

    Methods
    ----------
    * suma de matrices con misma dimension
    * prodcto entre dos matrices, matriz con vector, matriz con escalar. \n
        M1 * M2 -> M1.m = M2.n \n
        M1 * V1 -> M1.m = V1.dimension
    * reduce() devuelve la matriz en su forma escalonada reducida. No modifica la instancia 
    """
    @staticmethod
    def zeros(n, m):
        return Matrix([[0 for j in range(m)] for i in range(n)])

    def __init__(self, valores:list[list]) -> None:


        # Check dimensiones correctas
        for c in range(len(valores)-1):
            if len(valores[c]) != len(valores[c+1]):
                return ValueError("Todas las filas deben ser del mismo largo")

        self.components:list = valores
        self.dimensions:tuple = (len(valores), len(valores[0]))

    def __add__(self, other):
        # TODO: CHECK DIMENSIONES
        if not isinstance(other, Matrix):
            return ValueError("Solo se puede sumar matrices")
        else:
            m =  [[x + y for x, y in zip(f_1, f_2)] for f_1, f_2 in zip(self.components, other.components)]
            return Matrix(m)
        
    def __mul__(self, other, *args):
        if isinstance(other, (int, float)):
            return Matrix([[x * other for x in f] for f in self.components])
        elif isinstance(other, Vector):
            if self.dimensions[1] != other.dimension:
                return ValueError("Dimensiones del vector deber ser iguales que las columnas")
            else:
                v = []
                for i in range(self.dimensions[0]):
                    elem = 0
                    for j in range(self.dimensions[1]):
                        elem += (self.components[i][j] * other.componentes[j])
                    v.append(elem)

                return Vector(v)
        elif isinstance(other, Matrix):
            if self.dimensions[1] != other.dimensions[0]:
                return ValueError("Dimensiones incorrectas")
            else:
                m = [[] for i in range(self.dimensions[0])]
                for i in range(self.dimensions[0]):
                    for j in range(other.dimensions[1]):
                        c_ij = 0
                        for e in range(self.dimensions[1]):
                            c_ij += (self.components[i][e] * other.components[e][j])
                        m[i].append(c_ij)

                return Matrix(m)             
        else:
            return ValueError("No soporta ese tipo para multiplicar")

    def __rmul__(self, other): 
        if (isinstance(other, (int, float))): return self * other
        else:
            return ValueError("No soporta ese tipo para multiplicar")

    def __pow__(self, k):
        res = self
        for i in range(2, k):
            res = res * res
        return res

    def __repr__(self) -> str:
        str_comp = [[str(int(i)) for i in f] for f in self.components]
        repr = ""
        for i in range(self.dimensions[0]):
            repr += "["
            for j in range(self.dimensions[1]):
                repr += str_comp[i][j] + " "
            repr += "]\n"

        return "Matrix(\n" + repr +  ")"
    
    def reduce(self) -> 'Matrix':
        """
        Pre: 
        Post: self no se modifica; res = matriz escalonada reducida
        """
        matrix = Matrix(self.components).components.copy()
        pivot_col = 0
        n_rows, n_cols = self.dimensions

        for row in range(n_rows):

            if pivot_col >= n_cols:
                return Matrix(matrix)
            
            # Encontrar la primera fila con pivot diferent de 0
            # Cuando la encuentre, intercambiarla por la fila en la 
            # que se esta trabajando (Paso 2 del algoritmo)

            # Si no se encuentra ningun pivot != 0 en la primer columna,
            # se continua con la columna de la derecha
            row_pivot = row
            while matrix[row_pivot][pivot_col] == 0:
                row_pivot += 1
                if row_pivot == n_rows:
                    row_pivot = row
                    pivot_col += 1
                    if n_cols == pivot_col:
                        return matrix
            matrix[row_pivot], matrix[row] = matrix[row], matrix[row_pivot]

            # Divide la fila pivot por el pivot propiamente
            # para que sea 1.
            pivot = matrix[row][pivot_col]
            matrix[row] = [mrx / float(pivot) for mrx in matrix[row]]

            # Usar sustitucion en las filas arriba Y debajo del pivot elegido
            # para obtener 0. De esta manera, se obtiene la matriz escalonada
            # reducida.
            for other_row in range(n_rows):
                if other_row != row:
                    below_pivot = matrix[other_row][pivot_col]
                    matrix[other_row] = [iv - below_pivot * rv for rv, iv in zip(matrix[row], matrix[other_row])]
            pivot_col += 1

        return Matrix(matrix)
    
    def multPartes(self, other, bloque):
        if self.dimensions[0] % bloque != 0:
            return ValueError('No se puede dividir en esos bloques') 
    
        c_b = self.dimensions[0] // bloque
        C = []
        A = self.components
        B = other.components
        for i in range(c_b):
            for j in range(c_b):
                Aij = [row[j*c_b: (j+1)*c_b] for row in A[i*c_b: (i+1)*c_b]]
                Bij = [row[i*c_b: (i+1)*c_b] for row in B[j*c_b: (j+1)*c_b]]
                print(Matrix(Aij), Matrix(Bij))
                C_ij = Matrix.zeros(c_b, c_b)
                for e in range(self.dimensions[1]):
                    C_ij += (self.components[i][e] * other.components[e][j])

        