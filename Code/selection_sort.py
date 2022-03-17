# Selection Sort

Array = []
length = int(input("Enter the number of element: "))

for i in range(length):
    item = int(input("Enter here: "))
    Array.append(item)

# Traverse through all array elements
for i in range(len(Array)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(Array)):
        if Array[min_idx] > Array[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    Array[i], Array[min_idx] = Array[min_idx], Array[i]

# code to test
print("Sorted array")
for i in range(len(Array)):
    print("%d" % Array[i]),

# by James Vanlalpeka
