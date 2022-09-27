def two_fer(name:str=''):
    '''Function that returns a 'one for me and one for you' string
    
    :param name: the name you wanna play
    :return: 'one for name, one for me.
    
    '''
    if name == '':
        return f"One for you, one for me."
    else:
        return f"One for {name}, one for me."
