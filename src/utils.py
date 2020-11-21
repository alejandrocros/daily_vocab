import os
import json
from random import random, shuffle
from typing import Dict, List, Tuple

from src.scorer import Scorer


def read_data(data_path:str) -> List[Dict[str, str]]:
    try:
        with open(data_path, 'r') as fp:
            data = json.load(fp)
    except:
        print("Data couldn't be loaded!")
        data = list()
    shuffle(data)
    return data

def exam(data:list, src_lang:str, dest_lang:str, random_test:bool=False) -> None:
    print(f"Let's start with a {src_lang.upper()} to {dest_lang.upper()} test!")
    scorer = Scorer()
    for elem in data:
        if random_test and random() >= 0.5:
                _lang = src_lang
                src_lang = dest_lang
                dest_lang = _lang
        try:
            ### put this into a function
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
            print('\n')
        except KeyError:
            print(f"{elem} doesn't have the appropriate keys!")
    scorer.print_final_score()

def exam_handler(data:list, src_lang:str, dest_lang:str, mode:int=1) -> None:
    if mode==1:#Bilingual
        exam(data, src_lang=src_lang, dest_lang=dest_lang, random_test=True)
    elif mode==2:#Src -> Dest
        exam(data, src_lang=src_lang, dest_lang=dest_lang)
    elif mode==3:#Dest -> Src
        exam(data, src_lang=dest_lang, dest_lang=src_lang)
    return
