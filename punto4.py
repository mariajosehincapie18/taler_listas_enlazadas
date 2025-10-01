from lista_doble import DoublyLinkedList

def eliminar_duplicados(lista):
    if lista.head is None:
        return
    
    i = lista.head

    while i != None:
        j = i.next
        duplicado = False

        while j != None:
            if j.value == i.value:
                duplicado = True
                break
            else:
                j = j.next

        
        if duplicado:
            siguiente= i.next

            if i.prev != None:
                i.prev.next = i.next
            else:
                lista.head = i.next

            if i.next != None:
                i.next.prev= i.prev
            else:
                lista.tail= i.prev
            
            

        i= i.next






listad = DoublyLinkedList()
listad.append(1)
listad.append(2)
listad.append(1)
listad.append(3)
listad.append(2)
listad.append(1)
listad.append(1)
print(listad)
eliminar_duplicados(listad)
print(listad)
