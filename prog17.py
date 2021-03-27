import collections

def CountFrequency(array):
    return collections.Counter(array)  
  
array = [1,5,4,6,5,4,1,6,5,2,1,4,5,6,5,1,4,5,6,2]
frequency = CountFrequency(array)

for (key, value) in frequency.items():
    print (key, " -> ", value)