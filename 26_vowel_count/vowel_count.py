def vowel_count(phrase):
    phraseDict = {}
    vowels = "aeiou"
    for i in phrase:
        if i.lower() in vowels:
            if phraseDict.get(i.lower()):
                phraseDict[i.lower()] += 1
            else:
                phraseDict[i.lower()] = 1
    print(phraseDict)
    return(phraseDict)
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>>  vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
vowel_count('rithm school')
vowel_count('HOW ARE YOU? i am great!')
