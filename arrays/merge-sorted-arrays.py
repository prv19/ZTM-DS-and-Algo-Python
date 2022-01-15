arr1 = [2,4,6,8,10,12,14,16,18,20]
arr2 = [1,3,5,7,9,11,13,15]

def merge(arr1, arr2):
    i=j=0
    merged = []
    
    while (i<=len(arr1)-1 and j<=len(arr2)-1):
        if (arr1[i] < arr2[j]):
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
        
    if (i < len(arr1)-1):
        for l in range(i, len(arr1)):
            merged.append(arr1[l])
    elif (j < len(arr2)-1):
        for l in range(j, len(arr2)):
            merged.append(arr2[l])
        
    return merged

print("Merging two sorted integer arrays ...")
print("array-1:", arr1)
print("array-2:", arr2)
print("merged array:", merge(arr1, arr2))

