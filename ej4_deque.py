from ctypes import Union
from tkinter.messagebox import RETRY
from typing import Any
from ej4_nodo_con_prev import Nodo
from python_ed_fcad_uner.data_structures.linear.queues import LinkedQueue
from ej4_deque_abstract import DequeAbstract

class Deque(DequeAbstract):

    def __init__(self) -> None:
        """Crea una cola vacía"""
        self._front: Union[Nodo, None] = None
        self._back: Union[Nodo, None] = None
        self._size : int = 0

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:

        if self.is_empty():
            return "LinkedQueue()"

        resultado = "" # inicializo resultado con el string vacío

        #Me quedo en actual con el elemento ubicado en el frente
        actual = self._front
        while actual != None:
            # proceso el elemento del nodo actual
            resultado += str(actual.element) + ", "
            
            # establezco el siguiente nodo como nodo actual
            actual = actual.next 
        
        #Quito los dos últimos caracteres del string    
        resultado = resultado[:len(resultado)-2]
        
        return f"LinkedQueue({resultado})"

    def is_empty(self) -> bool:
        return self._size == 0
    
    def first(self) -> Any:
        """Devuelve el elemento ubicado en el frente de la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        Returns:
        Any: Devuelve el elemento dato correspondiente al frente de la
        estructura.
        """

        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar")
        
        return self._front.element


    def last(self) -> Any:
        """ Devuelve el elemento correspondiente al nodo ubicado al final de
        la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        Returns:
        Any: Devuelve el elemento dato correspondiente al final de la estructura.
        """
        if self.is_empty():
            raise Exception("Lista vacía. No se puede continuar")        

        return self._back.element
    
    def add_first(self, element : Any) -> None:
        """_summary_
        Args:
        element (Any): elemento que va a ser agregado al principio de la
        estructura.
        """
        nuevo_nodo = Nodo(element, self._front,None)

        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._front.prev = nuevo_nodo
            self._front = self._front.prev
            
        self._size +=1


    
    def add_last(self, element : Any) -> None:
        """Agrega un elemento al final de la estructura.
        Args:
        element (Any): elemento que va a ser agregado al final de la estructura.
        """
        nuevo_nodo = Nodo(element, None,self._back)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo
            self._back = nuevo_nodo

            
        self._size += 1
    
    def delete_first(self) -> None:
        """Quita el elemento ubicado en el frente de la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """
        
        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        
        
        self._front = self._front.next
        self._size -= 1
        

    
    def delete_last(self) -> None:
        """Quita el elemento ubicado al final de la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """

        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")

       
        self._back = self._back.prev
        self._back.next = None
        self._size -= 1

        
    

