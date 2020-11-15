import argparse
import json
#import pandas as pd

from typing import Dict, List, Tuple
from random import random, shuffle


def read_data(data_path:str) -> List[Dict[str, str]]:
    try:
        with open(data_path, 'r') as fp:
            data = json.load(fp)
    except:
        print("Data couldn't be loaded!")
        data = list()
    shuffle(data)
    return data

#def get_languages(data:dict)-> Tuple[str, str]:
#    langs = list(pd.DataFrame(data).columns)
#    if len(langs) > 2:
#        print('Too many languages in here!')
#    return langs[0], langs[1]

def exam_handler(data:list, src_lang:str, dest_lang:str, mode:int=1):
    if mode==1:#Bilingual
        exam(data, src_lang=src_lang, dest_lang=dest_lang, random_test=True)
    elif mode==2:#Src -> Dest
        exam(data, src_lang=src_lang, dest_lang=dest_lang)
    elif mode==3:#Dest -> Src
        exam(data, src_lang=src_lang, dest_lang=dest_lang)
    return

def exam(data:list, src_lang:str, dest_lang:str, random_test:bool=False):
    print(f"Let's start with a {src_lang.upper()} to {dest_lang.upper()} test!")
    for elem in data:
        if random_test and random() >= 0.5:
                _lang = src_lang
                src_lang = dest_lang
                dest_lang = _lang
        try:
            src_word = elem[src_lang]
            dest_word = elem[dest_lang]
            answer = str()
            while answer not in [dest_word, '.']:
                answer = input(
                    f"\n------\n Translate {src_word} from {src_lang.upper()} to {dest_lang.upper()}:\n"
                    )
                if answer!= dest_word:
                    print('\nBad guess, motherfucker')
        except KeyError:
            print(f"{elem} doesn't have the appropriate keys!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Supervised training')
    parser.add_argument('--data', '-d', type=str, default='./data/vocabulary.json', help='Path to vocabulary JSON')
    parser.add_argument('--source_lang', '-s', type=str, default='es', help='Source Language')
    parser.add_argument('--target_lang', '-t', type=str, default='fr', help='Target Language')
    parser.add_argument('--mode', '-m', type=int, default=1, help='Test Mode: 1->multilingual 2->ES to FR 3->FR to ES')
    params = parser.parse_args()
    data = read_data(params.data)
    exam_handler(data, params.source_lang, params.target_lang, params.mode)
