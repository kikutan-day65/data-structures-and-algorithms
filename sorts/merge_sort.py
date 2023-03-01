def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    # First iteration untill either list1 or list2 reaches the length itself
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        
        else:
            combined.append(list2[j])
            j += 1
    
    # Second iteration for the leftover items of the first iteration
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined


print(merge([1,3,5,6], [2,4,7,8]))