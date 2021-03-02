def frequency(lst, search_term):
    term_count = 0
    for i in lst:
        if i == search_term:
            term_count += 1
        else:
            continue
    print(term_count)
    return term_count
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

frequency([1, 4, 3], 7)
frequency([1, 4, 3, 4, 4], 4)
