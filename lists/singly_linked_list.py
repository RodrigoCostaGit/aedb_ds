from abc import ABC, abstractmethod
from tad_list import List
from nodes import SingleListNode
from exceptions import EmptyListException, InvalidPositionException, NoSuchElementException

class SinglyLinkedList(List):
    def __init__(self):
        self.head=None


    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
 
    def size(self):
        count=0
        n=self.head
        while n is not None:
            count+=1
            n=n.next_node
        return count



    def get_first(self):
        if self.head==None:
            raise EmptyListException
        else:
            return self.head.element


    def get_last(self):
        if self.head==None:
            raise EmptyListException
        else:
            n=self.head
            while n.next_node is not None:
                n=n.next_node
            print(n.element)


    def get(self, position):
        n=self.head
        count=0
        while n.next_node is not None:
            if count==position:
                return n.element
            n=n.next_node
            count+=1
        if count==position:
            return n.element
        else:
            raise InvalidPositionException


    def find(self, element):
        n=self.head
        count=0
        while n.next_node is not None:
            if n.element==element:
                return count
            count+=1
            n=n.next_node
        if n.element==element:
            return count
        else:
            return -1

   
    def insert_first(self, element):
        new_node=SingleListNode(element)
        new_node.next_node=self.head
        self.head=new_node


    
    def insert_last(self, element):
        new_node=SingleListNode(element)
        if self.head==None:
            self.head=new_node
            return
        else:
            n=self.head
            while n.next_node is not None:
                n=n.next_node
            n.next_node=new_node
    

 
    def insert(self, element, position):
        new_node=SingleListNode(element)
        if position==0:
            new_node.next_node=self.head
            self.head=new_node
            return
        count=0
        n=self.head
        previous_node=0
        while n.next_node is not None:
            if count==position:
                previous_node.next_node=new_node
                new_node.next_node=n
                n=new_node
                return 
            count+=1
            previous_node=n
            n=n.next_node
        if count==position:
            n=self.head
            while n.next_node is not None:
                n=n.next_node
            n.next_node=new_node
        else:
            raise InvalidPositionException

    def remove_first(self):
        if self.head is None:
            raise EmptyListException
        else:
            self.head = self.head.next_node
            return self.head.element

    

    def remove_last(self):
        if self.head is None:
            raise EmptyListException
        else:
            n=self.head
            while n.next_node.next_node is not None:
                n=n.next_node
            n.next_node=None
            return n.element

    def remove(self, position):
        n=self.head
        previous_node=0
        count=0
        while n.next_node is not None:
            if count==position:
                previous_node.next_node=n.next_node
                return n.element
            previous_node=n
            n=n.next_node
            count+=1
        else:
            raise InvalidPositionException


    def make_empty(self):
        self.head=None

        

   
    def iterator(self):
        if self.head is None:
            raise EmptyListException
        else:
            n=self.head
            while n is not None:
                print(n.element," ")
                n=n.next_node