c = 0

for n in range(136818, 685980):

    passwd = [int(d) for d in str(n)]

    """ 
    i = 0
    is_not_decreasing = True
    while i < len(passwd) - 1:
        if not passwd[i] <= passwd[i+1]:
            is_not_decreasing = False
            break
        i += 1
    """    

    is_not_decreasing = all([passwd[i] <= passwd[i+1] for i in range(len(passwd) - 1)])

    """
    i = 0
    has_duplicates = False
    while i < len(passwd) - 1:
        if passwd[i] == passwd[i+1]:
            has_duplicates = True
            break
        i += 1
    """

    has_adjacent_duplicates = any([passwd[i] == passwd[i+1] for i in range(len(passwd) - 1)])

    if is_not_decreasing and has_adjacent_duplicates:
        c += 1

print(c)
