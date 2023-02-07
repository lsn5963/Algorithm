def solution(cacheSize, cities):
    data = []
    count = 0
    for city in cities:
        city = city.lower()
        if city not in data:
            if cacheSize == len(data):
                data.append(city)
                data.remove(data[0])
            else:
                data.append(city)
            count += 5
        else:
            data.append(city)
            data.remove(city)
            count += 1
    return count