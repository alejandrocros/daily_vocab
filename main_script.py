import argparse

from src.utils import exam, exam_handler, read_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Supervised training')
    parser.add_argument('--data_path', '-d', type=str, default='./data/vocabulary.json', help='Path to vocabulary JSON')
    parser.add_argument('--source_lang', '-s', type=str, default='es', help='Source Language')
    parser.add_argument('--target_lang', '-t', type=str, default='fr', help='Target Language')
    parser.add_argument('--mode', '-m', type=int, default=1, help='Test Mode: 1->multilingual 2->ES to FR 3->FR to ES')
    params = parser.parse_args()
    data = read_data(params.data_path)
    exam_handler(data, params.source_lang, params.target_lang, params.mode)
