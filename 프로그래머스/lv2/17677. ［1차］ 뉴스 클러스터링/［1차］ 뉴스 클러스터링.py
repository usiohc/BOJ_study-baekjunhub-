def solution(str1, str2):
    lst1 = []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            lst1.append(str1[i:i + 2].upper())

    lst2 = []
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            lst2.append(str2[i:i + 2].upper())
    
    lst1_source = lst1[:]
    lst1_result = lst1[:]
    for el in lst2:
        if el not in lst1_source:
            lst1_result.append(el)
        else:
            lst1_source.remove(el)
    
    lst2_result = []
    for el in lst2:
        if el in lst1:
            lst1.remove(el)
            lst2_result.append(el)
    
    if not lst1_result and not lst2_result:
        return 65536
    elif not lst2_result:
        return 0
    else:
        return int((len(lst2_result)/len(lst1_result)) * 65536)