from lista_doble import DoublyLinkedList

def lista_palindroma(head):
    palindromo= True
    if head is None or head.next is None:
        palindromo= True

    izquierda= head
    derecha= head

    while derecha.next != None:
        derecha= derecha.next

    while izquierda != derecha and izquierda.prev != derecha:
        if izquierda.value != derecha.value:
            palindromo = False

        izquierda= izquierda.next
        derecha= derecha.prev

    return palindromo




listad = DoublyLinkedList()
listad.append(1)
listad.append(2)
listad.append(3)
listad.append(4)
listad.append(1)
print(lista_palindroma(listad.head))

lista2= DoublyLinkedList()
lista2.append(1)
lista2.append(2)
lista2.append(3)
lista2.append(2)
lista2.append(1)
print(lista_palindroma(lista2.head))
