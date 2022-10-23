def solution(cacheSize, cities):
    answer = 0
    cities = [city.upper() for city in cities]
    cache = []
    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.insert(len(cities)-1, city)
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
    
    return answer