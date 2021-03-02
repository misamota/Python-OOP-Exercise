def multiply_even_numbers(nums):
    num = 1
    for i in nums:
        if i % 2 == 0:
            num *= i
        else:
            continue
    print(num)
    return num


multiply_even_numbers([2, 3, 4, 5, 6])
multiply_even_numbers([3, 4, 5])
multiply_even_numbers([1, 3, 5])

"""Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
