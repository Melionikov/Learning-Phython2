array = [5 , 4 , 20 , 40 , 1 , 6 , 99 , 92329]

new_array = []

for f in array:
    minValue = array[0]
    for b in array:
        if minValue >= b:
            minValue = b
    # minValue is the minimum value in the array
    print(minValue)
    print(new_array)
    print(array)
    new_array.append(minValue)
    array.remove(minValue)

print(new_array)
