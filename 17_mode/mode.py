def mode(nums):
    countDict = {}
    for i in nums:
        countDict[i]= countDict.get(i,0) + 1
    highestNum = max(countDict.values())
    for(num, freq) in countDict.items():
        if freq == highestNum:
            print(num)
            return num

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
mode([1, 2, 1])
mode([2, 2, 3, 3, 2])
