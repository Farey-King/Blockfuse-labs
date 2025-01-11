

def asc(arr):
    """
    Sorts the given array in ascending order.
    
    Parameters:
    arr (list): The list of numbers to be sorted.
    
    Returns:
    list: A new list with the numbers sorted in ascending order.
    """
    return sorted(arr)

def desc(arr):
    """
    Sorts the given array in descending order.
    
    Parameters:
    arr (list): The list of numbers to be sorted.
    
    Returns:
    list: A new list with the numbers sorted in descending order.
    """
    return sorted(arr, reverse=True)


if __name__ == "__main__":
    nums = [5, 20, 19, 11, 56, 12]
    
    print("Original array:", nums)
    print("Sorted in ascending order:", asc(nums))
    print("Sorted in descending order:", desc(nums))