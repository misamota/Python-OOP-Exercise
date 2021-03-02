def remove_every_other(lst):
    print(lst[::2])
    return lst[::2]
   
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

lst = [1, 2, 3, 4, 5]
remove_every_other(lst)
        