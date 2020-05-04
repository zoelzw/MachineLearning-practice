def PrintList(head):
    if head is None:
        return
    else: print(head.value)
    PrintList(head.next)
def reverseLinkedList(head):
    #return value: new head after the reversal
    if head is None or head.next is None:
        return head
    node = reverseLinkedList(head.next) #this node is the original tail but the new head
    #Add original head to tail

    head.next.next = head
    head.next = None

