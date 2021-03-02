def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    counts = {}
    counts2 = {}

    for x in str(num1):
        counts[x] = counts.get(x, 0) + 1
    for y in str(num2):
        counts2[y] = counts2.get(y, 0) + 1

    if counts == counts2:
        print("True")
    else:
        print("False")
    return counts == counts2

same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)
