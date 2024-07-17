def create_list(n):
     if n <= 0:
        return []
    else:
        return list(range(1, n + 1))
    if n <= 0:
        raise ValueError("Number of elements must be positive")
    return 0


def access_list_element(my_list, index):
    if index<0 or index>=len(my_list):
        return "Invalid index"
    
    return my_list[index], index
    if index<0 or index>=len(my_list):
        return "Invalid index"
    
    return -1


def reverse_list(my_list):
    return my_list[::-1]
    return 0


def combine_lists(list1, list2):
    return list1+list2
    return 0


