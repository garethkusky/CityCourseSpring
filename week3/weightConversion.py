def stone_to_kgs(stone):
    '''
    (number) -> number
    converts weight in stone to kilograms
    >>> stone_to_kgs(10)
    63.5029
    >>> stone_to_kgs(9.25)
    58.7401825
    '''
    return stone * 6.35029

def kgs_to_stone(kgs):
    '''
    (number) -> number
    converts weight in kilograms to stone
    >>> kgs_to_stone(80)
    12.597849862
    >>> kgs_to_stone(69)
    10.865645506
    '''
    return kgs / 6.35029