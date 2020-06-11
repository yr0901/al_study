#수열합치기
import sys

sys.stdin = open('input.txt','r')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst, temp):
    first = last = Node(temp[0])
    for val in temp[1:]:
        new = Node(val, last)
        last.next = new
        last = new
    
    if lst.head is None:
        lst.head = first
        lst.tail = last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > temp[0] :break
            cur = cur.next
        if cur is None :
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last

        elif cur.prev is None :
            last.next = lst.head
            lst.head.prev = last
            lst.head = first

        else:
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(temp)

def printList(lst):
    if lst.head is None : return

    cur = lst.tail
    n=0
    print(f'#{tc+1}', end=' ')
    while cur is not None and n<10:
        print(cur.data, end=' ')
        cur = cur.prev
        n+=1
    print()

    
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    mylist = LinkedList()
    for m in range(M):
        tlist = list(map(int, input().split()))
        addList(mylist, tlist)

    printList(mylist)