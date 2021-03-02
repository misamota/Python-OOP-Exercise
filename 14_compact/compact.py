def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newlst = []
    for i in lst:
        if i is True:
            newlst.append(i)
        else:
            continue
    print(newlst)
    return(newlst)
compact([0, 1, 2, '', [], False, (), None, 'All done'])
