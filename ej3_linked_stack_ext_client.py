from ej2_linked_stack_ext import LinkedStackExt

linked_stack = LinkedStackExt()

print("###### HACEMOS ALGUNOS PUSH 5, 8, 7, 6, 8, 9, 1, 15, 20")
linked_stack.push(5)
linked_stack.push(8)
linked_stack.push(7)
linked_stack.push(6)
linked_stack.push(8)
linked_stack.push(9)
linked_stack.push(1)
linked_stack.push(15)
linked_stack.push(20)


print("\n###### LEN ######")
print(linked_stack.__len__())

print("\n###### POP ######")
print(linked_stack.pop())

print("\n###### LEN ######")
print(linked_stack.__len__())

print("\n ####### TOP ######")
print(linked_stack.top())

print("###### MULTI POP : 3 POP() ######")
print(linked_stack.multi_pop(3))

print("\n###### LEN ######")
print(linked_stack.__len__())


print("\n###### LISTA ANTES [8, 6, 7, 8, 5] REPLACE ALL : REEMPLAZAR 8 por 0 ######")
linked_stack.replace_all(8,0)
lista = []
print("Lista Despues")
for i in range(0,linked_stack.__len__()):
        print(linked_stack.top())
        lista.append(linked_stack.pop())

tam = len(lista)
for i in range(0,tam):
    linked_stack.push(lista.pop())

print("\n###### LISTA ANTES [0, 6, 7, 0, 5] EXCHANGE : CAMBIA 0 por 5 ######")
linked_stack.exchange()
print("Lista Despues")
for i in range(0,linked_stack.__len__()):
        print(linked_stack.top())
        lista.append(linked_stack.pop())