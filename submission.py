#Note: the heap prettyprint is not written by me, but I copied it to better show the heaps

# STATEMENTS
list=[5, 2, 9, 3, 33457, 1]
import math #prettyprint heaps (https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-19.php)
from io import StringIO #prettyprint heaps (https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-19.php)

import heapq #used for heaps
from collections import deque #used for ques (based on Py2 docs)

# FUNCTIONS
def show_tree(tree, total_width=60, fill=' '): #prettyprint heaps (https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-19.php)
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

def mergeSort(passthrough):
 if len(passthrough)>1:
  mid=len(passthrough)//2 #Find the middle (mathematical formula m=(l+(r-1))/2
  L=passthrough[:mid] #Create list called L. Start to middle
  R=passthrough[mid:] #Create list called R. Middle to end
  mergeSort(L) #repeat division for list L
  mergeSort(R) #repeat division for list R
#until here we just keep dividing the lists till we get single item list. Now we start building the orriginal list back up
  i=j=k=0 # i used for L, j for R, k for the sorted one

  while i < len(L) and j < len(R): #Repeat this process when both are true
#    if x-th element of L smaller than x-th element of R, add L'th element on original list
    if L[i] < R[j]:
     passthrough[k] = L[i]
     i+=1 #now that we got the current lowest value, we increment i and repeat the while loop
    else:
     passthrough[k] = R[j]
     j+=1
    k+=1 #Increment k, so that we can add new values

#up until now, we sorted the lists under the assumptions both semilists had elements to compare. But if it's the end of that, just start adding the >
  while i<len(L):
    passthrough[k]=L[i]
    i+=1
    k+=1
  while j<len(R):
    passthrough[k]=R[j]
    j+=1
    k+=1

def stackCreator(passthrough):
    stack = []
    for i in passthrough:
        stack.append(i)
    print('\n\nStacked list')
    print(stack)

def printList(passthrough):
 for n in range(len(passthrough)): #repeat for each of the items
  print(passthrough[n], end=", ") #print that iteration's item

def queueCreator(passthrough):
    queue = deque([])
    for i in passthrough:
        queue.append(i)
    print('\nQueued list')
    print(queue)

def minHeapify(passthrough,element):#First heapify, then  add element
    print("\nFollowing function will convert to min heap, add second argument and pop first item")
    heapq.heappush(passthrough, element)
    heapq.heappop(passthrough)
    heapq.heapify(passthrough)

def maxHeapify(passthrough,element):
    print("\nFollowing function will convert to max heap, add second argument and pop first item")
    heapq.heappush(passthrough, element)
    heapq.heappop(passthrough)
    heapq._heapify_max(passthrough) #First heapify, then  add element

#PROCEDURE

## print the list
print("\nInitial list:")
printList(list) #args: array to use

## sort and print the list
mergeSort(list) #args: array to use
print("\n\nSorted list:")
printList(list) #args: array to use

## stack the list (function prints results)
stackCreator(list)

## queue the list (function prints results)
queueCreator(list)

minHeapify(list,5) #args: array to use, element to add
print(list)
show_tree(list) #prettyprint heaps (https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-19.php)

maxHeapify(list,5) #args: array to use, element to add
print(list)
show_tree(list) #prettyprint heaps (https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-19.php)