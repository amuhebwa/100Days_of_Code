import code

# node has a value and a pointer to the next node
class Node():
	def __init__(self, data):
		self.data = data 
		self.next = None 

class LinkedList():
	def __init__(self):
		self.head = None

	def print(self):
		if self.head is None:
			print('List is empty')
			return
		current = self.head
		while current != None:
			print('->>>', current.data)
			current = current.next

	def append_top(self, item):
		if self.head == None:
			self.head = Node(item)
		new_head = Node(item)
		new_head.next = self.head
		self.head = new_head

	def append_bottom(self, item):
		if self.head is None:
			self.head = Node(item)
		elif self.head.next is None:
			self.head.next = Node(item)
		else:
			current = self.head 
			while current.next != None:
				current = current.next
			current.next = Node(item)

	def delete_node(self, item):
		if self.head is None:
			return
		else:
			current = self.head
			prev = None
			while current.next != None:
				if current.data == item:
					break
				prev = current
				current = current.nextz



	
if __name__=="__main__":
	# Mon, Tues, Wed, Thurs, Fri
	linked = LinkedList()
	#linked.append_top('Mon')
	#linked.append_top('Sunday')
	#linked.append_top("Saturday")
	linked.append_bottom('Monday')
	linked.append_bottom('Tuesday')
	linked.append_bottom('Wednesday')
	linked.append_bottom('Thursday')
	linked.append_bottom('Friday')
	linked.print()
	# code.interact(local=locals())