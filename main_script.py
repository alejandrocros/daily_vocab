import argparse
import json
import os

from random import random, shuffle
from typing import Dict, List, Tuple


class Scorer:
    def __init__(self):
        self.correct_answers = 0
        self.wrong_answers = 0
        self._update()

    def failure(self):
        self.wrong_answers += 1
        self._update()

    def success(self):
        self.correct_answers += 1
        self._update()

    def _update(self):
        self.total_ans = self.correct_answers + self.wrong_answers
        self.ratio = self.correct_answers/self.total_ans if self.total_ans else 0.

    def _get_mark(self, ratio:float) -> str:
        if ratio < 0.7:
            return 'Désolé, tu as raté'
        elif ratio < 0.9:
            return 'Pas mal'
        return 'Tu dois mettre nouveaux mots'

    def print_stats(self):
        print(f"{self.correct_answers}/{self.total_ans} --> {100 * self.ratio:.2f} %")

    def print_final_score(self):
        os.system('clear')
        mark = self._get_mark(self.ratio)
        print(f"Final score: {self.correct_answers}/{self.total_ans} --> {100 * self.ratio:.2f} %\n\n{mark}\n")


def read_data(data_path:str) -> List[Dict[str, str]]:
    try:
        with open(data_path, 'r') as fp:
            data = json.load(fp)
    except:
        print("Data couldn't be loaded!")
        data = list()
    shuffle(data)
    return data

def exam_handler(data:list, src_lang:str, dest_lang:str, mode:int=1):
    if mode==1:#Bilingual
        exam(data, src_lang=src_lang, dest_lang=dest_lang, random_test=True)
    elif mode==2:#Src -> Dest
        exam(data, src_lang=src_lang, dest_lang=dest_lang)
    elif mode==3:#Dest -> Src
        exam(data, src_lang=dest_lang, dest_lang=src_lang)
    return

def exam(data:list, src_lang:str, dest_lang:str, random_test:bool=False):
    print(f"Let's start with a {src_lang.upper()} to {dest_lang.upper()} test!")
    scorer = Scorer()
    for elem in data:
        if random_test and random() >= 0.5:
                _lang = src_lang
                src_lang = dest_lang
                dest_lang = _lang
        try:
            os.system('clear')
            src_word = elem[src_lang]
            dest_word = elem[dest_lang]
            comment = elem.get('comment', str())
            answer = str()
            scorer.print_stats()
            first_attempt = True
            while answer != dest_word:
                answer = input(
                    f"\n------\nTranslate {src_word if not comment else f'{src_word} ({comment})'} from {src_lang.upper()} to {dest_lang.upper()}:\n\n"
                    ).strip()
                if answer != dest_word:
                    print('\nBad guess, motherfucker')
                    if first_attempt:
                        scorer.failure()
                    first_attempt = False
            if first_attempt:
                scorer.success()
        except KeyError:
            print(f"{elem} doesn't have the appropriate keys!")
    scorer.print_final_score()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Supervised training')
    parser.add_argument('--data_path', '-d', type=str, default='./data/vocabulary.json', help='Path to vocabulary JSON')
    parser.add_argument('--source_lang', '-s', type=str, default='es', help='Source Language')
    parser.add_argument('--target_lang', '-t', type=str, default='fr', help='Target Language')
    parser.add_argument('--mode', '-m', type=int, default=1, help='Test Mode: 1->multilingual 2->ES to FR 3->FR to ES')
    params = parser.parse_args()
    data = read_data(params.data_path)
    exam_handler(data, params.source_lang, params.target_lang, params.mode)
