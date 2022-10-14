from typing import Any, Iterator
from ej6_double_linked_list_abstract import DoubleLinkedListAbstract
from ej4_nodo_con_prev import Nodo

class DoubleLinkedList(DoubleLinkedListAbstract):

    def __init__(self) -> None:
        """Crea una lista vacía"""
        self._header: Nodo = Nodo(None, None, None)
        self._size: int = 0

    #@abstractmethod
    def __len__(self) -> int:
        """Devuelve la cantidad de elementos que tiene actualmente la lista.
        Returns:
        int: entero que indica a longitud de la lista. 0 si está vacía.
        """
        return self._size
        
    #@abstractmethod
    def __getitem__(self, key: int) -> Any:
        """Devuelve el elemento ubicado en la posición indicada por key.
        Args:
        key (int): posición de la que se va a retornar el elemento de la lista.
        Raises:
        Exception: Arroja excepción si el índice está fuera de rango.
        Returns:
        Any: Devuelve el valor ubicado en la posición indicada por key.
        """
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if key < 0 or key >= self._size:
            raise Exception("Índice fuera de rango.")

        i = 0
        actual = self._header.next 
        while actual: 
            if i == key: 
                return actual.element 
            actual = actual.next 
            i += 1

        return None

    #@abstractmethod
    def __setitem__(self, key: int, value: Any) -> None:
        """En la posición indicada por key se va a colocar value.
        Args:
        key (int): posición que se va a actualizar.
        value (Any): nuevo valor que se va a colocar.
        Raises:
        Exception: Arroja excepción si el índice está fuera de rango.
        """

        if self.is_empty():
            raise Exception("La estructura está vacía.")

        if key < 0 or key >= self._size:
            raise Exception("Índice fuera de rango.")

        i = 0 
        
        actual = self._header.next 
        
        while actual: 
            if i == key: 
                actual.element = value
            actual = actual.next
            i += 1

    #@abstractmethod
    def __delitem__(self, key: int) -> None:
        """Elimina de la estructura el elemento ubicado en la posición key.
        Args:
        key (int): posición cuyo nodo se va a quitar de la estructura.
        Raises:
        Exception: Arroja excepción si el índice está fuera de rango.
        """

        if self.is_empty():
            raise Exception("La estructura está vacía.")

        if key < 0 or key >= self._size:
            raise Exception("Índice fuera de rango.")

        i = 0

        # previo = None
        # actual = self._header.next 
        # while actual: 
        #     if i == key: 
        #         break
        #     previo = actual 
        #     actual = actual.next 
        #     i += 1

        
        # if previo: 
        #     previo.next = actual.next
        # else:
            
        #     self._header.next = actual.next

        # self._size -= 1
        
        #SE BORRA LA VARIABLE AUXILIAR previo
        actual = self._header.next # Arranco en el primer nodo de la lista.
        while actual: # Si existe...
            if i == key: # Si el i es igual a key => corto.
                break
            
            actual = actual.next # Continúo con el siguiente nodo.
            i += 1

        # Si previo existe => elimino el nodo actual haciendo que el siguiente del previo sea igual al siguiente de actual
        # Y que el previo del siguiente del actual sea el previo del actual.
        if actual.prev:  
            actual.prev.next = actual.next
            actual.next.prev = actual.prev
        else:
            # Si previo no existe => se está queriendo eliminar el primer nodo.
            self._header.next = actual.next

        self._size -= 1
        
        
    #@abstractmethod
    def __iter__(self) -> Iterator[Any]:
        """ Visita desde el principio hacia el final todos los nodos de la lista y
        retorna sus elementos.
        Yields:
        Iterator[Any]: Cada uno de los elementos de los nodos de lista.
        """

        actual = self._header.next
        
        #Si existe un nodo
        while actual:
            #Devuelve el elemento del nodo actual
            yield actual.element
            
            #Continúa con el siguiente.
            actual = actual.next
        
    #@abstractmethod
    def __str__(self) -> str:
        """Concatena en un único string todos los elementos de la lista.
        Returns:
        str: string con todos los elementos de la lista convertidos en str.
        """

        if self.is_empty():
            return "LinkedList()"
        
        res = "" 

        actual = self._header.next 

        while actual: 
            
            res += str(actual.element) + ", "
            
            actual = actual.next

        res = res[:-2]

        return f"LinkedList({res})"
        
    #@abstractmethod
    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía.
        Returns:
        bool: True si la lista está vacía, caso contrario, False.
        """
        return self._size == 0

    #@abstractmethod
    def append(self, elem: Any) -> None:
        """ Agrega el elemento pasado por parámetro al final de la lista.
        Args:
        elem (Any): elemento que va a quedar ubicado en la última posición
        """

        nuevo_nodo = Nodo(elem)
        # Si la lista está vacía => el nuevo nodo es el primero.
        if self.is_empty():
            self._header.next = nuevo_nodo
        else:
            # Caso contrario => me muevo hasta el final...
            actual = self._header

            while actual.next:
                actual = actual.next

            # Agrego el nuevo nodo como siguiente del último.
            # Linea agregada
            # Y hago que previo del siguiente sea el actual
            actual.next = nuevo_nodo
            actual.next.prev = actual

        self._size += 1


#EJEMPLOS DE PRUEBA AL ELIMINAR UN ELEMENTO
# doubleLL = DoubleLinkedList()
# doubleLL.append(1)
# doubleLL.append(2)
# doubleLL.append(3)

# print(doubleLL)

# doubleLL.__delitem__(1)

# print(doubleLL)
# print(doubleLL._header.next.next.prev.element)