def feedDog(hunger_level, biscuit_size):
    """
    :param hunger_level: array hunger_level [1..n] (ith dog has hunger level of hunger_level [i])
    :param biscuit_size: dog biscuits of size given by biscuit_size [1…m].
    This function contains a greedy algorithm that is used to match biscuits to the appropriate
    hunger level of a dog. The function will return the total number of dogs that can be satisfied.
    """
    # Part 1: Sorting
    # Both arrays are sorted to make matching the smallest values easier
    hunger_level.sort()
    biscuit_size.sort()

    # Part 2:
    # Initialization
    total_dogs_satisfied = 0
    # Keep track of the indices with pointers
    hunger_pointer = 0
    biscuit_pointer = 0

    while hunger_pointer < len(hunger_level) and len(biscuit_size):


    return total_dogs_satisfied
