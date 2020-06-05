# import numpy as np
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # empty hash
    s = {}
    # loop through array
    for i, weight in enumerate(weights):
        # subract an index value from hash
        if limit - weight in s:
            #if difference exists, return indices
            return (i, s[limit - weight])
            # give first index variable
        s[weight] = i
 
    return None
