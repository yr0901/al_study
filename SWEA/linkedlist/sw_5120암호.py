class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

def addLast(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1 
        
def printList(lst):
    if lst.head is None : return

    cur = lst.head.prev
    n = 0
    print(f'#{tc+1}', end=' ')
    while n < 10 and n<lst.size :
        print(cur.data, end=' ')
        cur = cur.prev
        n+=1
    print()

T = int(input())
for tc in range(T):
    mylist = LinkedList()
    N, M, K = map(int, input().split())
    tlist = list(map(int, input().split()))
    for val in tlist:
        addLast(mylist, Node(val))

    cur = mylist.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next

        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new
        
        mylist.size += 1

    printList(mylist)