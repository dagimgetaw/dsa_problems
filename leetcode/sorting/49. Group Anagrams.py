from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

hashmap = defaultdict(list)
arr = []

for i in strs:
    n = tuple(sorted(i))
    hashmap[n].append(i)
    
for i in hashmap.values():
    arr.append(i)
    
print(arr)