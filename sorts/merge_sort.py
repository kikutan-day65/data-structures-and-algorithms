"""
    space complexity: O(n)
    time complexity: O(n*log(n))

"""

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


def merge_sort(mylist):

    # base case for recursion
    if len(mylist) == 1:
        return mylist
    
    # divide the mylist in half,
    mid_index = len(mylist) // 2

    # and create two lists recursively
    left = merge_sort(mylist[:mid_index])
    right = merge_sort(mylist[mid_index:])

    # merge them
    return merge(left, right)


mylist = [1,4,3,6,7,2,5,9,8]
res = merge_sort(mylist)
print(res)