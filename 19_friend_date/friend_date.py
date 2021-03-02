def friend_date(a, b):
    test = 0
    for i in a[2]:
        if i in b[2]:
            test += 1
        else:
            continue
    if test > 0:
        print("True")
        return True
    else:
        print("False")
        return False
            
        
            

    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True

        better Answers:
        
            if set(a[2]) & set(b[2]):
                return True
            else:
                return False

            # can even do by converting to boolean!
            #
            # return bool(set(a[2] & set(b[2])
                
    """
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

friend_date(elmo, sauron)
friend_date(sauron, gandalf)
