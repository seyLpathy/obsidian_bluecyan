# an array of sequence
## built-in sequences

^27b031

| group    | container sequence                              | flat sequence                                                             |
| -------- | ----------------------------------------------- | ------------------------------------------------------------------------- |
| varities | list, tuple, and collections.deque              | str, bytes, bytearray, memoryview, and array.array                        |
| trait    | hold the reference to the objects they contains | store the value of each item within its own memory space,primitive values |
![[Pasted image 20240606145602.png]]
## list
```python
colors = ['black', 'white']
 sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
		   for size in sizes]
tshirts 
```

### generator expression
```python
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
 print(tshirt)
```

## tuple
### tuple as records
```python
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
print('%s/%s' % passport)
```

### tuple unpacking
```python
divmod(20,8)
t=(20,8)
divmod(*t)
quotient, remainder = divmod(*t)

# access items
a, b, *rest = range(5)
a, *body, c, d = range(5)
```

### tuple as immutable lists
compare with list,tuple cannot alter items in tuple 

## slicing
