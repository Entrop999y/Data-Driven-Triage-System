


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_obj(self):  # getter method for object part of node
        return self.data

    def set_obj(self, data):  # setter method to insert the data object into the node
        self.data = data

    #def get_next(self):  # getter method for the pointer to next node #7pm
       # return self.next

    #def set_next(self,next): #7pm didn't seem to work or make a difference once i got rid of hidden varial code
        #self.next = next




class LinkedList: # define the list template
    def __init__(self):
        self.head = None

    def get_node(self, pos):
        counter = 1
        tmp_node = None

        while counter <= pos:# find out is current node the head
            if counter == 1:
                tmp_node = self.head
            else:# move to the next node and increment the counter

                tmp_node = tmp_node.next
            counter = counter + 1
        return tmp_node

    def print_list(self):# prints the whole sll as objects
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):# add a node plus data
        new_node = Node(data) # instantiate a new node

        if self.head is None:# check for empty list
            self.head = new_node
            return

        last_node = self.head # append to the end by traversing to find the tail
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node



    def pop_front(self):

        if (self.head != None):
            # 1. if head is not null, create a
            #   temp node pointing to head
            temp=self.head
            # 2. move head to next of head
            self.head = self.head.next

            # 3. delete temp node
            temp = None


    def pop_any(self, position):

        # check if the position is > 0 (a type of try catch method)
        if (position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1 and self.head != None):

            # if the position is 1 and head is not null, make head next as head and delete previous head
            node_to_delete = self.head
            self.head = self.head.next
            node_to_delete = None
        else:

            # Else, make a temp node and traverse to the node previous to the position
            temp = self.head
            for i in range(1, position - 1):
                if (temp != None):
                    temp = temp.next

                    # If the previous node and next of the previous is not null, adjust links
            if (temp != None and temp.next != None):
                node_to_delete = temp.next
                temp.next = temp.next.next
                node_to_delete = None
            else:

                # Else the given node will be empty.
                print("\nThe node is already null.")



    def size(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count







