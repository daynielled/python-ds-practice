def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    for first_letter in phrase:
        return phrase[0].capitalize()+ phrase[1:]
    
    