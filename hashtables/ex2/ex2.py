#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create hash
    # iterate through array
    # Set key value pairs
    # set 1st pair
    # loop through the rest
    # stop when the first and last key match

    route = []
    place = {}
    x = "NONE"
    for i in range(length):
        key = tickets[i].source
        value = tickets[i].destination
        place[key] = value
    
    key = place[x]
        # return 
    while key is not x:
        route.append(key)
        key = place[key]
    route.append(key)
  
    return route
 
