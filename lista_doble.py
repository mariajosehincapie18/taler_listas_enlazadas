import random

class Node:
  __slots__ = ('__value','__next','__prev')

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,newNext):
    if newNext is not None and not isinstance(newNext,Node):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = newNext

  @property
  def prev(self):
    return self.__prev

  @prev.setter
  def prev(self,newPrev):
    if newPrev is not None and not isinstance(newPrev,Node):
      raise TypeError("prev debe ser un objeto tipo nodo ó None")
    self.__prev = newPrev

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class DoublyLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @head.setter
  def head(self,newHead):
    if newHead is not None and not isinstance(newHead,Node):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = newHead

  @property
  def tail(self):
    return self.__tail

  @tail.setter
  def tail(self,newTail):
    if newTail is not None and not isinstance(newTail,Node):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = newTail

  @property
  def size(self):
    return self.__size

  @size.setter
  def size(self, newSize):
    if not isinstance(newSize, int):
      raise TypeError("El tamaño debe ser un objeto tipo numerico entero")
    self.__size = newSize

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def prepend(self, value):

    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      newnode.next = self.__head #enlazo nuevo nodo
      self.__head.prev = newnode
      self.__head = newnode
    self.__size += 1


  def append(self,value):
    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      newnode.prev = self.__tail
      self.__tail = newnode

    self.__size += 1

  def getbyindex(self, index):
    if index < 0 or index > self.__size:
      return "Error, indice fuera de rango"

    cont = 0
    for currentNode in self:
      if cont == index:
        return currentNode
      cont += 1

  def insertinindex(self, value, index):

    if index == 0:
      self.prepend(value)
    elif index == -1 or index == self.__size:
      self.append(value)
    else:
      prevNode = self.getbyindex(index-1)
      print("prevNode",prevNode)
      nextNode = prevNode.next
      print("nextNode",nextNode)
      newNode = Node(value)
      newNode.prev = prevNode # 1 Linea nueva por doblemente enlazada
      newNode.next = nextNode #Enlazo el next del nuevo nodo, que es el next del previo

      prevNode.next = newNode
      nextNode.prev = newNode # 2 Linea nueva por doblemente enlazada
      print("prevNode newNode",newNode.prev)
      print("prevNode nextNode",nextNode.prev)
      self.__size +=1

  def searchbyvalue(self, valuetosearch):
    for currentNode in self:
      if currentNode.value == valuetosearch:
        return True

    return False

  def setnewvalue(self, valuetochange, newvalue):
    for currentNode in self:
      if currentNode.value == valuetochange:
        currentNode.value = newvalue
        return True

    return False

  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return "Lista vacia, no hay elementos a eliminar"
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__head.prev = None
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode


  def pop(self):
    tempNode = self.__head
    if self.__head is None:
       print("Lista vacia, no hay elementos a eliminar")
       return None
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      poppednode = self.__tail
      prevnode = self.__tail.prev #self.getbyindex(self.__size-2)
      print("prevnode",prevnode)
      prevnode.next = None
      self.__tail = prevnode
      self.__size -= 1
      poppednode.prev = None
      return poppednode
    
  def generate(self, n, minvalue, maxvalue):
    for i in range(n):
      self.append(random.randint(minvalue, maxvalue))
    return self