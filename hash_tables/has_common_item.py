def has_common_item(list1, list2):
    my_dict = {}

    for i in list1:
        my_dict[i] = True
    
    # print(my_dict)

    for j in list2:
        if j in my_dict:
            return True
    
    return False

list1 = [2, 3, 5]
list2 = [1, 4, 5]

result = has_common_item(list1, list2)
print(result)

# time complexity: O(2n) = O(n)