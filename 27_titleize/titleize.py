def titleize(phrase):
    newStr = ""
    words = phrase.split()
    for i in words:
        newStr += i.capitalize() + " "
    print(newStr.strip())
    return newStr.strip()


    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'

        now that I've done this I know about l.title()
    """
titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')