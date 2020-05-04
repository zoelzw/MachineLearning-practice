# LinkedList class object

# Define node object
class _ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None  # I don't know which next to point to, so use None


# MyLinkedList is a linked list
class MyLinkedList(object):
    def __init__(self):
        '''
        Initialize your data structure here.
        Here, we will construct an empty linked list.
        '''
        self._head = None  # always maintain a reference that points to the head
        self._tail = None  # always maintain a reference that points to the tail
        self._size = 0  # always represents the current number of nodes

    def _get(self, index):
        '''
        Find node that corresponds to index.
        Assume index is within [0, self._size]
        '''
        node = self._head
        for _ in xrange(index):
            node = node.next
        return node

    def get(self, index):
        '''
        get the value of the index node in the linked list. If the index is invalid, return -1 (actually not good because -1 might be a data value).
          :type index: Int
          :rtype: int
        '''
        # check index is valid or not
        if index < 0 or index >= self._size:
            return -1
        return self._get(index).value

    def addAtHead(self, val):
        '''
        Add a node of value before the first element of the linked list
          :type val: int
          :rtype: None
        '''
        if self._head is None:
            self._head = self._tail = _ListNode(val)
        else:
            new_head = _ListNode(val)  # add
            new_head.next = self._head
            self._head = new_head  # redefine head
        self._size += 1

    def addAtTail(self, val):
        '''
        Add a node of value after the last element of the linked list
          :type val: int
          :rtype: None
        '''
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            self._tail.next = _ListNode(val)  # add
            self._tail = self._tail.next  # redefine tail
        self._size += 1

    def addAtIndex(self, index, val):
        '''
        Add a node of value val before the index node in the linked list. If index equals the length of linked list, the node will be appended to the end. If index is greater than the length, the node will not be inserted.
          :type index: int
          :tyep val: int
          :rtype: None
        '''
        # Index validation
        if index < 0 or index > self._size:  # note len = size - 1
            return  # do nothing
        if index == 0:
            self.addAtHead(val)  # note size already added
        elif index == self._size:
            self.addAtTail(val)
        else:
            prev_node = self._get(index - 1)
            new_node = _ListNode(val)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self._size += 1

    # AddAtIndex better solution with dummy head
    def add_to_index(head, index, val):
        fake_head = ListNode(None)
        fake_head.next = head
        insert_place = search_by_index(fake_head, index)
        if insert_place is None:
            return fake_head.next
        new_node = ListNode(val)
        new_node.next = insert_place.next
        insert_place.next = new_node
        return fake_head.next

    def deleteAtIndex(self, index):
        '''
        Delete the index node in the linked list, if the index is valid.
          :type index: int
          :rtype: None
        '''
        if index < 0 or index >= self._size:
            return
        if index == 0:
            #delete old head
            #deletion means two things:
            #1. most important: from linked list perspective, you can not see this node
            #2. optional:from this node perspective, there is no other nodes after it
            # if delete head
            new_head = self._head.next
            self._size -= 1
            self._head.next = None  #
            self._head = new_head
            # if I remove the last and first node
            if self._head is None:
                self._tail = None
        else:
            prev_node = self._get(index - 1)
            remove_node = prev_node.next
            prev_node.next = remove_node.next
            remove_node.next = None
            # what if I remove the original tail node?
            if index == self._size - 1:
                self._Tail = prev_node
        self._size -= 1

    def __str__(self):
        '''
        Get the string representation of the internal singly list
        '''
        strs = []
        node = self._head
        while node is not None:
            strs.append(str(node.val))
            node = node.next
        return ' -> '.join(strs)