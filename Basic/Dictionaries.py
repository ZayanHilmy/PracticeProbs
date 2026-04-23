exDict = {'Jack':[15, 'blonde'], 'Alice':[12, 'brown'], 'Bob':[20,'ginger'] , 'Horton':[18,'black']}

print(exDict)

print(exDict['Jack'])

exDict['Tim'] = [14, 'white']

print(exDict)

exDict['Tim'][0] = 15

print(exDict)

del(exDict['Tim'])

print(exDict)