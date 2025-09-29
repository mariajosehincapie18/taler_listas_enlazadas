from lista_simple import LinkedList,Node

def fusionar_segmento(lista):
    head = lista.head
    current_node = head
    suma =0
    inicio_segmento= None

    while current_node:
        if current_node.value == 0:
            if inicio_segmento is not None:
                inicio_segmento.value = suma
                inicio_segmento.next = current_node.next

                suma = 0
                inicio_segmento= None

        else:
            if inicio_segmento is None:
                inicio_segmento= current_node
                suma = current_node.value
            else:
                suma +=  current_node.value

        current_node = current_node.next

    lista.head= head.next

def imprimir(head):
    current_node = head
    while current_node:
        print(current_node.value, end= " -> ")
        current_node = current_node.next
    

lista= LinkedList ()

lista.append(0)
lista.append(3)
lista.append(1)
lista.append(0)
lista.append(4)
lista.append(5)
lista.append(2)
lista.append(0)

print("lista original: ")
print(lista)

lista_fusionada = fusionar_segmento(lista)
print("lista funcionada")
print(lista)

            