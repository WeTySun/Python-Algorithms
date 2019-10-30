# Simple heap program
import heapq

H = [21,1,45,78,3,5]
# Heapify to rearrange the elements
heapq.heapify(H)
print(H)
# Add user input element
a = int(input())
heapq.heappush(H,a)
print(H)
# Elements automatically be added to begining if a < H or to end if a > H
# Removing elements

# Remove from beginning
heapq.heappop(H)

print(H)
