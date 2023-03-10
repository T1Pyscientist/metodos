from vector import Vector

class Matrix:
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

    """

    def __init__(self, valores: list[list]) -> None:


        # Check dimensiones correctas
        for c in range(len(valores)-1):
            if len(valores[c]) != len(valores[c+1]):
                return ValueError("Todas las filas deben ser del mismo largo")

        self.compoments = valores
        self.dimensions = (len(valores), len(valores[0]))


    def __add__(self, other):
        if not isinstance(other, Matrix):
            return ValueError("Solo se puede sumar matrices")
        else:
            m =  [[x + y for x, y in zip(f_1, f_2)] for f_1, f_2 in zip(self.compoments, other.compoments)]
            return Matrix(m)
        

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[x * other for x in f] for f in self.compoments])
        elif isinstance(other, Vector):
            if self.dimensions[1] != other.dimension:
                return ValueError("Dimensiones del vector deber ser iguales que las columnas")
            else:
                v = []
                for i in range(self.dimensions[0]):
                    elem = 0
                    for j in range(self.dimensions[1]):
                        elem += (self.compoments[i][j] * other.componentes[j])
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
                            c_ij += (self.compoments[i][e] * other.compoments[e][j])
                        m[i].append(c_ij)

                return Matrix(m)
                
        else:
            return ValueError("No soporta ese tipo para multiplicar")


    def __rmul__(self, other): 
        if (isinstance(other, (int, float)) or
            isinstance(other, Vector) or
            isinstance(other, Matrix)): return self *other
        else:
            return ValueError("No soporta ese tipo para multiplicar")


    def __repr__(self) -> str:
        str_comp = [[str(i) for i in f] for f in self.compoments]
        repr = ""
        for i in range(self.dimensions[0]):
            repr += "["
            for j in range(self.dimensions[1]):
                repr += str_comp[i][j] + " "
            repr += "]\n"

        return "Matrix(\n" + repr +  ")"