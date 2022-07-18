###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    # pass

    FILENAME = open(filename, 'r')
    cows = {}
    lines = FILENAME.readlines()
    for line in lines:
        commastrip = line.split(",")
        cows[commastrip[0]] = commastrip[1]
        
    return cows
    
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # pass

    # Initiate the variables
    result = []
    cows_not_taken = cows.copy()
    
    # Loops through the dictionary until all cows are taken    
    while len(cows_not_taken) != 0:
        total_weight = 0
        this_trip = []
        cows_eval = cows_not_taken.copy()
        for i in range(len(cows_not_taken)):
            # Greedy algorithm: gets the heaviest that fits
            heavier = max(cows_eval, key=cows_eval.get) # Looks for the heaviest cows
            if (int(cows[heavier]) + total_weight) <= limit: # See if it fits
                this_trip.append(heavier) # Adds to the list of the trip
                total_weight += int(cows[heavier]) # Total weight of the trip
                cows_eval.pop(heavier) # Removes the heavier an possible fit
                cows_not_taken.pop(heavier)
            else:
                cows_eval.pop(heavier)
        else:
            result.append(this_trip)
    else:
        return result
    
    # BACKUP CODE
    # total_weight = 0
    # cows_eval = cows.copy()
    # this_trip = []
    # for i in range(len(cows_not_taken)):
    #     # Greedy algorithm: gets the heaviest that fits
    #     heavier = max(cows_eval, key=cows_eval.get) # Looks for the heaviest cows
    #     if (int(cows[heavier]) + total_weight) <= limit: # See if it fits
    #         this_trip.append(heavier) # Adds to the list of the trip
    #         total_weight += int(cows[heavier]) # Total weight of the trip
    #         cows_eval.pop(heavier) # Removes the heavier an possible fit
    #         cows_not_taken.pop(heavier)
    #     else:
    #         cows_eval.pop(heavier)
    # else:
    #     result.append(this_trip)        
    # # Second try        
    # this_trip = []
    # for cow in cows:
    #     heavier = max(cows_copy, key=cows_copy.get)
    #     if int(cows.get(cow)) >= int(cows.get(heavier)): # Looks for the heaviest cows
    #         if (int(cows.get(cow)) + total_weight) <= limit: # See if it fits
    #             this_trip.append(cow) # Adds to the list of the trip
    #             total_weight += int(cows.get(cow)) # Adds to total weight of the trip
    #             cows_copy.pop(cow) # Removes the heavier and possible fit
    #         else:
    #             cows_copy.pop(cow) # Removes from the list to evaluate
    # result.append(this_trip)
    
    # # Thrid Try
    # this_trip = []
    # heavier = max(cows_copy, key=cows_copy.get) # Looks for the heaviest cow

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # pass
    
    # cows_copy = cows.copy()
    # result = []
    
    # # List all cows
    # cows_list = list(cows.keys())
    
    # # Loop through each possible combination
    # partitions = get_partitions(cows_list)
    # for partition in partitions:
    #     # Checks if the combination is fit
    #     partition_sum = 0
    #     for cow in partition:
    #         partition_sum += int(cows[cow])
    #     if partition_sum <= 10:
    #         result.append(partition.sort())
    
    # # Partition each possible list and order them
    # result = result.sort()

    # # Takes the min length of all possible lists
    # for trip in result:
    #     min_lenght = 100
    #     if len(trip) < min_lenght:
    #         min_lenght = len(trip)
    #         optimal_trip = trip
            
    # return optimal_trip
    
    # List all cows
    cows_list = list(cows.keys())
    cows_copy = cows.copy()
    result = []
    
    # Loop through each possible combination
    for partition in get_partitions(cows_list):
        # Checks if the combination is fit
        over_limit = False # Defaults the value to emmpty
        for sublist in partition: 
            weight = 0 # Defaults the value to empty
            for cow in sublist:
                weight += int(cows_copy[cow])
            if weight > limit:
                over_limit = True
                break
        if over_limit is True:
            continue
        # Takes the min length of all possible lists
        elif len(result) == 0 or len(result) > len(partition):
            result = partition
        # Return call
    return result
       
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    # pass

    cows = load_cows('ps1_cow_data.txt')
    # Testing greedy algorithm
    start = time.time()
    greedy_result = greedy_cow_transport(cows,10)
    end = time.time()
    greedy_time = end - start
    # Testing brute force algorithm
    start = time.time()
    brute_result = brute_force_cow_transport(cows,10)
    end = time.time()
    brute_time = end - start
    
    return greedy_result, greedy_time, brute_result, brute_time

greedy_result, greedy_time, brute_result, brute_time = compare_cow_transport_algorithms()

print('\nThe greedy result is: ', greedy_result)
print('\nTime elapsed: ', greedy_time)
print('\n====================')
print('\nThe brute force result is: ', brute_result)
print('\nTime elapsed: ', brute_time)