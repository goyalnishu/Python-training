def grouping_dictionary(l):
    result = {}
    for k, v in l:
        result.setdefault(k, []).append(v)
    return result


colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))
