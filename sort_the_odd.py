def sort_array(source_array):
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            for i1 in range(len(source_array)):
                if source_array[i1] % 2 != 0 and source_array[i] < source_array[i1]:
                    buff = source_array[i1];
                    source_array[i1] = source_array[i];
                    source_array[i] = buff;
    return source_array;