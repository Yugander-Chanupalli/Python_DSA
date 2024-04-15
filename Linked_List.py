class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
    
l=[1,2,3,4,5]

head=Node(l[0])
current_node=head


for i in l[1:]:
  new_node=Node(i)
  current_node.next=new_node
  current_node=new_node
  
current_node=head
while current_node:
  linked_list=current_node.data
  print(linked_list)
  current_node=current_node.next
