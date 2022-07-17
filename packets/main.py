import heapq

a = (1, 0, 0)
b = (0.2, 1, 0)
c = (0.3, 2, 0)
d = (0.1, 3, 0)

myheap = [a,b,c,d]
heapq._heapify_max(myheap)
print(heapq.heappop(myheap))
print(heapq.heappop(myheap))
print(heapq.heappop(myheap))
print(heapq.heappop(myheap))
