def my_min_function(b):
    min_value = None
    max_value = None
    min_max = []
    for value in b:
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    if max_value == min_value:
        min_max.append(len(b))
    else:
        min_max.append(min_value)
        min_max.append(max_value)
        return min_max
        