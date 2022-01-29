from pprint import pprint


def main():
    words_file_path = r'/home/nitesh/PycharmProjects/spelling_bee/words.txt'
    words_list = []
    with open(words_file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            words_list.append(line.strip().lower())

    key_letter = 'h'
    supporting_letters = ['n', 'g', 'z', 'e', 'w', 'i'] + [key_letter]

    matches = []
    for word in words_list:
        if key_letter in word:
            matched = True
            for c in word:
                if c not in supporting_letters:
                    matched = False
                    break
            if matched:
                matches.append(word)
    matches.sort(key=lambda x: len(x), reverse=True)

    pprint(matches)


if __name__ == '__main__':
    main()
