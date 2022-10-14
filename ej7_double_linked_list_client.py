
from ej6_double_linked_list import DoubleLinkedList

print("#### Creacion de lista: doubleLL = DoubleLinkedList() #####")
doubleLL = DoubleLinkedList()

print("\n#### TAMAÑO INICIAL : " + str(doubleLL.__len__()))

print("\n#### INICIALMENTE ESTA VACIO: " + str(doubleLL.is_empty()))

print("\n#### _str_ CON LISTA VACIA: "+ doubleLL.__str__())

print("\n#### LANZARA EXCEPCIONES SI INTENTAMOS USAR: doubleLL.__delitem__(), doubleLL.__getitem__(), doubleLL.__setitem__()")


print("\n#### AGRAMOS ELEMENTOS CON doubleLL.append()")
for i in range(1,11):
    doubleLL.append(i)

print("\n#### TAMAÑO DESPUES DE AGREGAR ELEMENTOS : " + str(doubleLL.__len__()))


if not doubleLL.is_empty():
    vacio = "No"
else:
    vacio = "Si"

print("\n#### ESTA VACIO?: " + vacio)

print("\#### __str__() CON ELEMENTOS: " +doubleLL.__str__())

print("#### OBTENER ELEMENTO EN POSICION 0: "+ str(doubleLL.__getitem__(0)))
print("\n#### __delitem__() EN UN INDICE FUERA DE RANGO LANZARA UNA EXCEPCION: ")
#doubleLL.__delitem__(11)

print("\n#### BORRAR ELEMENTO EN LA POSICION 0:")
doubleLL.__delitem__(0)
print("\n#### BORRA EL ELEMENTO 1: "+ doubleLL.__str__())
print("\n#### TAMAÑO: "+str(doubleLL.__len__()))

print("\n#### BORRAR ELEMENETO EN LA POSICION 5:")
doubleLL.__delitem__(5)
print("\n#### BORRA EL ELEMENTO 7: "+ doubleLL.__str__())
print("\n#### TAMAÑO: "+str(doubleLL.__len__()))

print("\n#### MODIFICAR EL ELEMENTO EN LA POSICION 0: doubleLL.__setitem__(0,99)")
doubleLL.__setitem__(0,99)
print(doubleLL)

print("\n#### MODIFICAR EL ELEMENTO EN LA POSICION 4: doubleLL.__setitem__(4,44)")
doubleLL.__setitem__(4,44)
print(doubleLL)

print("\n#### ITERADOR")
elementos= []
for i in doubleLL.__iter__():
    elementos.append(i)
print(elementos)


print("\n#### RECORRER DESDE EL PRINCIPIO HASTA EL FINAL")
i = doubleLL._header

for j in range(0,doubleLL.__len__()):
    print(str(i.next.element))
    i = i.next

print("#### RECORRER DESDE EL FINAL HASTA EL PRINCIPIO")

for j in range(0,doubleLL.__len__()):
    print(i.element)
    i = i.prev

print(doubleLL)