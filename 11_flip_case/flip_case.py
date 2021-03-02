def flip_case(phrase, to_swap):
    newPhrase = ""

    for i in phrase:
        if i.lower() == to_swap.lower():
            if i.isupper():
                newPhrase += i.lower()

            if i.islower():
                newPhrase += i.capitalize()
        else:
            newPhrase += i
    print(newPhrase)

 
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'h')
