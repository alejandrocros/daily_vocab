[//]: # (Image References)

[image1]: ./.github/images/demo_screenshot.png "Demo"
# Daily Vocabulary Recap

### Usage

Clone repo and run `main_script.py`:
```bash
python main_script.py -d ./data/vocabulary.json -s es -t fr -m 2
```

where
- `-d` or `--data_path` is a path to a .JSON with vocabulary translations (fields are language shortnames and values are words in that language)-
- `-s` or `--source_lang` and `-t` or `--target_lang` are the languages for the vocabulary recap.
- `-m` or `--mode` is the type of recap you want to do (`1` for random _source-target_ or _target-source_ questions  `2` for only _source-target_ and `3` for only _target-source_ questions).

(Run `python main_script.py -h` for syntax help.)

Sample of the test output:
![Demo][image1]

## TO-DO
- [X] Re-factor code.
- [ ] Add multiple choice (a `synonymous` field in JSON's).
- [ ] Split tests by word category.
