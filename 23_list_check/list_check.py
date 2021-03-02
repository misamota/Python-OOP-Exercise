def list_check(lst):
    for i in lst:
        if isinstance(i,list):
            continue
        else:
            print("False")
            return False    
    print("True")
    return True
    
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
list_check([[1], [2, 3]])
list_check([[1], "nope"])