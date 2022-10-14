from ctypes import Union
from typing import Any

# Creacion de nodo para realizar el ejercicio 4. Cuenta con un nodo previo
class Nodo():
     
    def __init__(self, element : Any, next = None, prev = None) -> None:
        self.element = element
        self.next : Union[Nodo, None] = next
        self.prev : Union[Nodo,None] = prev