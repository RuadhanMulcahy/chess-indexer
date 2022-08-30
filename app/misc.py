def extract_integer_from_file_name(filename):
    return int(filename.split('_')[1].split('.')[0])

def num_dif(num_1, num_2):
    if num_1 > num_2:
        return num_1 - num_2
    else:
        return num_2 - num_1