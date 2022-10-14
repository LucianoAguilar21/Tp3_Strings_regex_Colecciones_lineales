from ast import List
from typing import Any
from python_ed_fcad_uner.data_structures.linear.stacks.linked_stack import LinkedStack
from ej2_linked_stack_ext_abstract import LinkedStackExtAbstract

class LinkedStackExt(LinkedStack,LinkedStackExtAbstract):

    def   multi_pop(self, num: int) -> list[any]:

        # """Realiza la cantidad de operaciones pop() indicada por num.
        # Args:
        # num (int): número de veces que se va a ejecutar pop().
        # Raises:
        # Exception: Arroja excepción si se invoca a pop() por cuando la estructura
        # está vacía.
        # Returns:
        # List[Any]: lista formada por todos los topes que se quitaron de la pila.
        # """
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        resultados= []

        for i in range(0,num,1):
            resultados.append( self.pop())
          
        
        return resultados


    def replace_all(self, param1: Any, param2: Any) -> None:


        # """Reemplaza todas las ocurrencias de param1 en la pila por param2.
        # Args:
        # param1 (Any): Valor a buscar/reemplazar.
        # param2 (Any): Nuevo valor.
        # """
        
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")

        lista = []

        for i in range(0,self.__len__()):
            if self.top() == param1:
                self.pop()
                self.push(param2)
            else:
                lista.append(self.pop())

        tam = len(lista)
        for i in range(0,tam):
            self.push(lista.pop())


  
    def exchange(self) -> None:

        """Intercambia el elemento ubicado en el tope con el más antigüo o último.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """

        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")

        tope = self.pop()
        lista = []
        for i in range(0,self.__len__()):
            while not self.is_empty():
                lista.append(self.pop())

        ultimo = lista.pop()

        if self.is_empty():
            self.push(tope)

        tamanio= len(lista)
        for i in range(0,tamanio):
            self.push(lista[tamanio-1])
            tamanio -= 1
        
        self.push(ultimo)
        