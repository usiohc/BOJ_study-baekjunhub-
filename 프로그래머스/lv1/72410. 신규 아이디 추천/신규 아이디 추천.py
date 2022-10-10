def solution(new_id):
    #1
    new_id = new_id.casefold()
    
    #2
    id = ''
    for i in range(len(new_id)):
        if new_id[i].isalnum() or new_id[i] in ('-', '_', '.'):
            id += new_id[i]

    #3
    while id.find('..')>-1:
        id = id.replace('..', '.')

    #4
    if id:
        try:
            if id[0] == '.':
                id = id[1:]
            if id[-1] == '.':
                id = id[:-1]
        except IndexError:
            print(id)
            pass

    #5
    if not id:
        id = 'a'
        
        
    #6, 7
    if len(id) > 15:
        id = id[:15]
        if id[-1] == '.':
            id = id[:-1]
    elif len(id) < 3:
        id = id + id[-1] * (3-len(id))
        print(2)
    
    return id