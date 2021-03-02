def multiple_letter_count(phrase):
    let_dict = {}
    for i in phrase:
        if i in let_dict:
            let_dict[i] += 1
        else:
            let_dict[i] = 1
    print(let_dict)
    return(let_dict)
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
multiple_letter_count('yay')
multiple_letter_count('Yay')
