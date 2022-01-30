from fastapi import FastAPI
import os

app = FastAPI()
words_file_path = None


@app.get("/buzz/")
def generate_word_list(key_letter: str, supporting_letters: str):
    print(os.curdir)
    global words_file_path
    if words_file_path is None:
        words_file_path = r'./spelling_bee/data/words.txt'
    key_letter = key_letter.lower()
    supporting_letters = supporting_letters.lower()

    matches = []
    all_letters = list(supporting_letters) + [key_letter]
    with open(words_file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            word = line.strip().lower()
            if len(word) <= 3:
                continue
            if key_letter in word and set(word).issubset(all_letters):
                matches.append(word)
    matches.sort(key=lambda x: len(x), reverse=True)

    return matches
