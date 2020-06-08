def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # create hash
    # iterate through array
    # Set key value pairs
    # loop 
    # count integers with duplicates
    # return them
    result = []
    ints = {}
    
    for i in range(len(arrays)):
        for integer in arrays[i]:
            if None:
                return None
            if integer in ints:
                ints[integer] += 1
            else:
                ints[integer] = 1
    for ints1 in ints:
        if ints[ints1] ==len(arrays):
            result.append(ints1) 
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
