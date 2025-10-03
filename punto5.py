from lista_doble import DoublyLinkedList

def rotar_hasta_maximo(lista):
   
    if lista.size <= 1 :
        return
    
    max_node = lista.head
    current_node= lista.head
    while current_node is not None:
        if current_node.value > max_node.value:
            max_node = current_node
        
        current_node= current_node.next

    while lista.head != max_node:
        tail= lista.tail
        new_tail= tail.prev

        new_tail.next = None
        tail.prev= None

        tail.next= lista.head
        lista.head.prev = tail
        lista.head= tail

        lista.tail= new_tail

    return


listad = DoublyLinkedList()
listad.append(1)
listad.append(2)
listad.append(3)
listad.append(8)
listad.append(5)
listad.append(6)
listad.append(7)
print(listad)
rotar_hasta_maximo(listad)
print(listad)
print(listad.head)
print(listad.tail)