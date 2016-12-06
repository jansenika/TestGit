# Branch test
# Yayayayayay
# Hello
#Assuming all 3 arrays are presorted
#Merge all 3 arrays into a single sorted array

def merge(arr1, arr2):
	left = 0
	for i in range(len(arr2)):
		for j in range(left, len(arr1)):
			if arr2[i] >= arr1[j]:
				if j==len(arr1)-1:
					arr1.insert(j+1,arr2[i])
					left = j+1
					break
				else:
					if arr2[i] < arr1[j+1]:
						arr1.insert(j+1,arr2[i])
						left = j+1
						break
	return arr1


arr1 = [0,4,7,9,10,15,34,47,79,345,"A"]
arr2 = [5,8,13,45,55,100]
arr3 = [1,2,34,56,1233]
newarray = merge(merge(arr1,arr2),arr3)
print newarray
