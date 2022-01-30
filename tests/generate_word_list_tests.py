import spelling_bee.main
from spelling_bee.main import generate_word_list
import unittest


class GenerateWordListTests(unittest.TestCase):
    def test_should_generate_word_list(self):
        spelling_bee.main.words_file_path = r'../tests/data/test_words.txt'
        results = generate_word_list(key_letter='c', supporting_letters='oxtnei')
        self.assertEqual(17, len(results))

    def test_should_generate_word_list_case_insensitive(self):
        spelling_bee.main.words_file_path = r'../tests/data/test_words.txt'
        results = generate_word_list(key_letter='c', supporting_letters='oxtneI')
        self.assertEqual(17, len(results))


if __name__ == '__main__':
    unittest.main()
