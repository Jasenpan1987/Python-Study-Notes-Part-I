def cap_text(mystr):
    '''
    Input a string
    Output the string with capitalize
    '''
    strlist = mystr.split(" ")
    if len(strlist) == 1:
        return mystr.capitalize()
    else:
        return " ".join(map(lambda w: w.capitalize(), strlist))
