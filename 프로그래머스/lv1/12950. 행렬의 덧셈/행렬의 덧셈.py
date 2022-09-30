def solution(arr1, arr2):
    answer = [[a+b for a,b in zip(arr1[i], arr2[i])] for i in range(len(arr1))]
    return answer