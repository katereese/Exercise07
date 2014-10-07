

def read_data_from_twain(twain_file):

    twain_words_dict = {}

    opened_file = open(twain_file)

    for line in opened_file:
        word_keys_list = line.strip().split()
        
        for each_word in word_keys_list:
        
            if each_word in twain_words_dict:
                twain_words_dict[each_word] += 1
            else:
                twain_words_dict[each_word] = 1

    return twain_words_dict


def main():
    twain_file = "twain_10.txt"
    print read_data_from_twain(twain_file)

if __name__ == '__main__':
    main()