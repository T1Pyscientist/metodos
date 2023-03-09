class Vector():
    """  Vector de n-dimensiones
    
    Parameters
    ----------
    valores : list[(int, float)]
        Valores de los componentes para inicializar el vector

    Attributes
    ----------
    componentes : list
        Componentes del vector

    dimension : int
        Dimension del vector

    """
    
    def __init__(self, valores) -> None:
        self.componentes = valores
        self.dimension = len(valores)

    def __add__(self, other):
        """Solo puede sumarse otro vector de igual dimensiones"""
        if (not isinstance(other, Vector)) or (other.dimension != self.dimension):
            return ValueError("Unsupported!")
        else:
            return Vector([a_1 + a_2 for a_1, a_2 in zip(self.componentes, other.componentes)])
        
    def __mul__(self, value):
        if not isinstance(value, (int, float)):
            return ValueError("Must be a real number")
        else:
            return Vector([a_1 * value for a_1 in self.componentes])
        
    def __rmul__(self, value):
        if not isinstance(value, (int, float)):
            return ValueError("Must be a real number")
        else:
            return self * value
        
    def __repr__(self) -> str:
        str_comp = [str(i) for i in self.componentes]
        return "Vector" + str(self.dimension) + "D(" + ", ".join(str_comp) + ")"