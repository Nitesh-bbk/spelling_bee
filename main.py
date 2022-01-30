from pprint import pprint
from fastapi import FastAPI

app = FastAPI()


@app.get("/buzz/")
def create_list_of_candidate_words(key_letter: str, supporting_letters: str):
    words_file_path = r'./words.txt'
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
