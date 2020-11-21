import os


class Scorer:
    def __init__(self):
        self.correct_answers = 0
        self.wrong_answers = 0
        self._update()

    def failure(self) -> None:
        self.wrong_answers += 1
        self._update()

    def success(self) -> None:
        self.correct_answers += 1
        self._update()

    def _update(self) -> None:
        self.total_ans = self.correct_answers + self.wrong_answers
        self.ratio = self.correct_answers/self.total_ans if self.total_ans else 0.

    def _get_mark(self, ratio:float) -> str:
        if ratio < 0.7:
            return 'Désolé, tu as raté'
        elif ratio < 0.9:
            return 'Pas mal'
        return 'Tu dois mettre nouveaux mots'

    def print_stats(self) -> None:
        print(f"{self.correct_answers}/{self.total_ans} --> {100 * self.ratio:.2f} %")

    def print_final_score(self) -> None:
        os.system('clear')
        mark = self._get_mark(self.ratio)
        print(f"Final score: {self.correct_answers}/{self.total_ans} --> {100 * self.ratio:.2f} %\n\n{mark}\n")
