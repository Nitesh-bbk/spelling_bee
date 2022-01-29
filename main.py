from pprint import pprint
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
