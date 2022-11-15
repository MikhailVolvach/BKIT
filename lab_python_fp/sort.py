def sort(data, reverse=False):
    for i in range(len(data)):
        minimum = i

        for j in range(i + 1, len(data)):
            if data[j] < data[minimum]:
                minimum = j

        data[minimum], data[i] = data[i], data[minimum]
    return data[::-1] if reverse else data
