import timeit
from datetime import datetime

from application.server.services.statistic_containers import Statistic
from application.server.services.calculators import CharStatisticCalculator, WordStatisticCalculator, TextStatisticCalculator, \
    SentenceStatisticCalculator
from application.server.constants import WORD_SEPARATORS, SENTENCE_SEPARATORS
from application.server.services.separator import Separator
from application.server.models import AnalysisReport


class TextAnalyzer:
    @classmethod
    def get_report(cls, name, text):
        statistic = Statistic()
        now = datetime.now()
        statistic.datatime = now.strftime("%d/%m/%Y %H:%M:%S")
        tic = timeit.default_timer()

        statistic.character_statistic = CharStatisticCalculator(text).get_statistic()
        statistic.text_statistic = TextStatisticCalculator(text).get_statistic()
        separator = Separator(text)
        words = separator.run(WORD_SEPARATORS)
        sentences = separator.run(SENTENCE_SEPARATORS, include_separators=True)
        statistic.word_statistic = WordStatisticCalculator(words).get_statistic()
        statistic.sentence_statistic = SentenceStatisticCalculator(sentences).get_statistic()

        toc = timeit.default_timer()
        statistic.time_to_process = toc - tic

        return AnalysisReport(
            name=name,
            text=text,

            time_to_process=statistic.time_to_process,
            datatime=statistic.datatime,
            char_number=statistic.character_statistic.number,
            char_frequency=statistic.character_statistic.frequency,
            char_distribution=statistic.character_statistic.distribution,

            words_number=statistic.word_statistic.number,
            words_average_length=statistic.word_statistic.average_length,
            most_used_words=statistic.word_statistic.most_used,
            longest_words=statistic.word_statistic.longest,
            shortest_words=statistic.word_statistic.shortest,
            number_palindrome=statistic.word_statistic.number_palindrome,
            longest_palindrome=statistic.word_statistic.longest_palindrome,

            sentences_number=statistic.sentence_statistic.number,
            sentences_average_words_number=statistic.sentence_statistic.average_words_number,
            longest_sentences=statistic.sentence_statistic.longest,
            shortest_sentences=statistic.sentence_statistic.shortest,

            is_palindrome=statistic.text_statistic.is_palindrome,
            reversed=statistic.text_statistic.reversed,
            reversed_with_order=statistic.text_statistic.reversed_with_order
        )
