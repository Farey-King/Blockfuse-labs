

def asc(arr):
    """
    
    
    Parameters:
    arr (list): 
    
    Returns:
    list: 
    """
    return sorted(arr)

def desc(arr):
    """
    
    
    Parameters:
    arr (list): 
    
    Returns:
    list: 
    """
    return sorted(arr, reverse=True)


if __name__ == "__main__":
    nums = [5, 20, 19, 11, 56, 12]
    
    print("Original array:", nums)
    print("Sorted in ascending order:", asc(nums))
    print("Sorted in descending order:", desc(nums))