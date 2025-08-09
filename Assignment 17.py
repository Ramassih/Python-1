'''
Challenge: Ensure that the function works correctly with tuples of different lengths.
=============================================
Description: Create a function called concat_tuples that
takes two tuples as input and returns a new tuple containing
all elements from both input tuples.
'''


def concat_tuples(tuple1, tuple2):
    try:
        # Combine elements from both tuples
        combined = tuple1 + tuple2

    except TypeError:
        print('TypeError: one or both inputs are not tuples')
        return ()

    else:
        return combined

    finally:
        print('Execution completed')

print (concat_tuples ((1,2,3),(4,5,6)))