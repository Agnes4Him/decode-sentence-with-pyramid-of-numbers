def convert_list_to_string(list):
    str = " "
    return (str.join(list))

def decode(message_file):
    file_dict = {}
    numbers_list = []
    words_list = []
    pyramid_list = []
    with open(message_file) as f:
        line = f.readline()
        while line:
            #print(line, end='')
            line_list = line.split()
            file_dict[line_list[0]] = line_list[1]
            line = f.readline()
    #print(file_dict)
    for key, value in file_dict.items():
        #print(key)
        numbers_list.append(int(key))
        words_list.append(value)
        numbers_list.sort()
    #print(numbers_list)
    #print(words_list)
    n = 0
    start = 0
    end = 1
    while True:
        x = slice(start, end)
        pyramid_list.append(numbers_list[x])
        start = start + len(numbers_list[x])
        end = end + len(numbers_list[x]) + 1
        n += 1
        if pyramid_list[-1][-1] == 300:
            break
    #print(pyramid_list)
    decoded_nums = []
    for item in pyramid_list:
        #print(item[-1])
        decoded_nums.append(item[-1])
    decoded_msg = []
    for num in decoded_nums:
        for key, value in file_dict.items():
            if str(num) == key:
                decoded_msg.append(value)

    print(convert_list_to_string(decoded_msg))


# Call decode() function here
decode('coding_qual_input.txt')