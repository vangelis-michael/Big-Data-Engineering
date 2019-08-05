
# BUBBLE SORT

# Bubble sort works by constantly iterating through an unsorted array and swapping values within
# that array until such times as no swaps are made within a full passs through the array.

def bubbleSort(arr):
	n = len(arr) # Get the length of array
	
	# Loop through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):
			
			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				
array = [44, 23, 1, 45, 5, 100]
bubbleSort(array)
print(array)


# INSERTION SORT

# Insertion sorting algorithm works by iterating through an array and sorting elements in a 
# linear fashion.
# It can sort an unsorted array in a worst case time of O(N^2) time. 
# If the array is already sorted, it has time complexity of O(N).				

def insertionSort(myList):

	# loop through every element in the array
	for index in range(1, len(myList)):
		# Get the current value of the element at the current index 'position'
		current = myList[index]
		position = index
		
		# Compare the previous value(s) with the current and swap if greater than current value
		
		while position > 0 and myList[position-1] > current:
			# Swap the previous value with the value at index 'position'
			myList[position] = myList[position-1] 
	
			# Reduce the position so that we can compare the value at that index against the current value again
			position -= 1
			
		# Let the current value (current) be at the last known position
		myList[position] = current
			
	return myList


	
	
unsortedArray = [4, 22, 100, 2, 3, 4, 2]
sortedArray = insertionSort(unsortedArray)
print(sortedArray) 	
