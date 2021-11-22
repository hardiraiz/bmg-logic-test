def iterasi(n):
    result = str()
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            result += 'Frontend Backend'
        elif i % 3 == 0:
            result += 'Frontend'
        elif i % 5 == 0:
            result += 'Backend'
        else:
            result += f'{i}'

        if i < n:
            result += ','

        i += 1
    
    return result


print(iterasi(50))
