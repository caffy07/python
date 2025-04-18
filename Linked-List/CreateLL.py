class Node:
  def __init__(self, data):
    self.data = data
    self.next = none
    
  def __repr__(self):
    return self.data


class LinkedList:
  def __init__(self):
    self.head = None
    
  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append(node.data)
      node = node.next
    nodes.append("None")
    return '->'.join(nodes)


#creating a LL
ll = LinkedList()

#creating nodes
n1 = Node('d')
n2 = Node('e')
n3 = Node('a')

ll.head = n1
n1.next = n2
n2.next = n3

#print linked list
print(ll)

#output: d->e->a->None
