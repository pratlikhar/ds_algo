l = [1,2,3,4,5]
l.append(6)
print(l)
l.insert(1,0)
print(l)
print(5 in l)
print(l.count(5))
print(l.index(5))
print(l.index(5,1,-1)) # item, start_idx(inclusive), end_idx(exclusive)
l.remove(2)
print(l)
l.pop()
print(l)
l.pop(2) # index
print(l)
del l[0] # del at index 0
print(l)
del l[0:2]
print(l)

# more functions

l = [1,2,3,4,5,6,7,8,9,10]

print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)
