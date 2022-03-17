# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# code to test
arr = []
length = int(input("Enter the number of element: "))

for i in range(length):
    item = int(input("Enter here: "))
    arr.append(item)

insertionSort(arr)
print("\nSorted array is: ")
for i in range(len(arr)):
    print("%d" % arr[i])


# by James Vanlalpeka
