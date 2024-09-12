D1 = {'a':'one', 'b':'two', 'c': 'three', 'd':'four'}
D2 = {'c':'five', 'd':'six', 'e': 'seven' ,'f':'eight'}
D = {}

for d in D1:
    D[d] = D1[d]
    print(D)
    
for d in D2:
    D[d] = D2[d]
    print(D)
