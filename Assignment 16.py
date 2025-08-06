
'''Challenge: Optimize the function to handle large input lists efficiently.
==============================
Description: Develop a function called find_common_elements
that takes two lists as input and returns a new list containing
elements that are common to both input lists.'''

def find_common_elements(list1, list2):
    try:
        set1 = set(list1) if len(list1) < len(list2) else set (list2)
        other_list = list2 if len(list1) < len(list2) else list1

        common = [item for item in other_list if item in set1]

    except TypeError:
        print('TypeError: one or both inputs are not iterable')
        return[]

    else:
        return common

    finally:
        print('execution completed')
print (find_common_elements ([1,2,3,4,5], [2,3,4,5]))

