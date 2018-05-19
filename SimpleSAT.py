def SimpleSAT(raw_input="a&(b|c)&~b&~c"):

    # function to preapre variations from an iterable that contains iterable items
    def variations(items, i=0, output=''):
        if i == len(items):
            yield output.split()
        else:
            for item in items[i]:
                for xxx in variations(items, i + 1, output + ' ' + item):
                    yield xxx

    # extract the variables(letters) from the expression
    letters = list(set([char for char in raw_input if char.isalpha()]))

    # function to replace the operator to its word form
    rep_dict = {'&': ' and ', '|': ' or ', '~': ' not '}
    def replace_operators(string):
        for variable, value in rep_dict.items():
            string = string.replace(variable, value)
        return string

    """
    try all possible value (0/1) and evaluate these expressions
        until one setup is True(1)
        or no setup is True
    """
    for setup in variations([['0','1']]*len(letters)):
        # replace the letters(a,b,c,...) to 0/1 for the current setup
        to_replace_letters = raw_input
        for value, letter in zip(setup, letters):
            to_replace_letters = to_replace_letters.replace(letter, value)
        # after replacing the operators, it can be evaluated
        if eval(replace_operators(to_replace_letters))*1:
            return 'yes'
    # getting here means no setup is True
    return 'no'