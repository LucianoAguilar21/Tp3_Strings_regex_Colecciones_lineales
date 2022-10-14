from ej4_deque import Deque


deque = Deque()
print("\n######### AÑADIENDO ELEMENTOS A LA DEQUE (2, 3, 4, 5, 6) #########")
deque.add_first(2)
deque.add_first(3)
deque.add_first(4)
deque.add_first(5)
deque.add_first(6)


print("\nDEQUE STR:  "+str(deque))

print("\n######### TAMAÑO DE COLA = " + str(deque.__len__())+ " #########")

print("\n######### PRIMER ELEMENTO: " + str(deque.first()) + " #########")
print("\n######### ULTIMO ELEMENTO: " + str(deque.last()) + " #########")

print("\n######### AGREGO UN ELEMENTO AL FINAL = 1 | deque.add_last(1) #########")
deque.add_last(1)

print("\n######### ULTIMO ELEMENTO : " + str(deque.last()) + " #########")
print(deque)


print("\n######### ELIMINO EL ULTIMO ELEMENTO CON deque.delete_last() #########")
print("\n######### QUITA EL NUMERO 1 #########")
deque.delete_last()
print(deque)
print("\n REDUCE EL TAMAÑO  EN -1 : TAMAÑO =  "+str(deque.__len__()))

print("\n ######### ELIMINO EL PRIMER ELEMENTO CON deque.delete_FIRST() #########")
print("\n######### QUITA EL NUMERO 6 #########")
deque.delete_first()
print(deque)
print("\n REDUCE EL TAMAÑO  EN -1 : TAMAÑO =  "+str(deque.__len__()))
