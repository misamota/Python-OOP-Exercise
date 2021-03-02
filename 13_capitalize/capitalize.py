def capitalize(phrase):
    phraseList = phrase.split()
    newPhrase = phraseList[0].capitalize()
    print(newPhrase)
    return newPhrase
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
capitalize('python')
capitalize('only first word')
