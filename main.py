import timeit
from datetime import datetime

from statistic_containers import Statistic
from calculators import CharStatisticCalculator, WordStatisticCalculator, TextStatisticCalculator, SentenceStatisticCalculator
from constants import WORD_SEPARATORS, SENTENCE_SEPARATORS
from separator import Separator


class Main:
    def run(self):
        with open("some_text.txt", "r") as file:
            data = file.read()

        statistic = Statistic()
        now = datetime.now()
        statistic.datatime = now.strftime("%d/%m/%Y %H:%M:%S")
        tic = timeit.default_timer()

        statistic.character_statistic = CharStatisticCalculator(data).get_statistic()
        statistic.text_statistic = TextStatisticCalculator(data).get_statistic()
        separator = Separator(data)
        words = separator.run(WORD_SEPARATORS)
        sentences = separator.run(SENTENCE_SEPARATORS, include_separators=True)
        statistic.word_statistic = WordStatisticCalculator(words).get_statistic()
        statistic.sentence_statistic = SentenceStatisticCalculator(sentences).get_statistic()

        toc = timeit.default_timer()
        statistic.time_to_process = toc - tic

        # TODO add visualizer class
        print(statistic)


if __name__ == '__main__':
    m = Main()
    m.run()
