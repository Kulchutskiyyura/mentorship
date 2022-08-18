from abc import ABCMeta, abstractmethod
from constants import WORD_SEPARATORS, AMOUNT_OF_SHOWN
from separator import Separator
from statistic_containers import SentenceStatistic, WordStatistic, TextStatistic, CharacterStatistic


class StatisticCalculator(metaclass=ABCMeta):
    def __init__(self, data):
        self._data = data

    @abstractmethod
    def get_statistic(self):
        pass

    def _get_length(self):
        return len(self._data)

    def _get_frequency(self):
        frequency = {}
        unique_item = set(self._data)
        for item in unique_item:
            frequency.update({item: self._data.count(item)})

        return frequency

    def _get_shortest(self, amount):
        return list(sorted(self._data, key=lambda x: len(x)))[:amount]

    def _get_longest(self, amount):
        return list(sorted(self._data, key=lambda x: len(x), reverse=True))[:amount]

    def _is_palindrome(self, text):
        return text == text[::-1]


class CharStatisticCalculator(StatisticCalculator):
    def __init__(self, data):
        super().__init__(data)
        self._statistic = CharacterStatistic()

    def get_statistic(self):
        self._statistic.number = self._get_length()
        self._statistic.frequency = self._get_frequency()
        self._statistic.distribution = self._get_distribution()

        return self._statistic

    def _get_distribution(self):
        distribution = {}
        for char, frequency in self._statistic.frequency.items():
            distribution.update(
                {char: self._get_percentage(self._statistic.number, frequency)}
            )

        return distribution

    def _get_percentage(self, total, number):
        return number / total * 100


class WordStatisticCalculator(StatisticCalculator):
    def __init__(self, data):
        super().__init__(data)
        self._statistic = WordStatistic()
        self._palindrome_words = []

    def get_statistic(self):
        self._get_palindrome_words()
        self._statistic.number = self._get_length()
        self._statistic.average_length = self._get_average_length()
        self._statistic.longest = self._get_longest(AMOUNT_OF_SHOWN)
        self._statistic.shortest = self._get_shortest(AMOUNT_OF_SHOWN)
        self._statistic.most_used = self._get_most_used(AMOUNT_OF_SHOWN)

        palindrome_words = WordStatisticCalculator(self._palindrome_words)
        self._statistic.longest_palindrome = palindrome_words._get_longest(AMOUNT_OF_SHOWN)
        self._statistic.number_palindrome = palindrome_words._get_length()

        return self._statistic

    def _get_average_length(self):
        total_length = 0
        for word in self._data:
            total_length += len(word)

        return total_length / self._statistic.number

    def _get_most_used(self, amount):
        frequency = self._get_frequency()

        return list(sorted(frequency, key=frequency.get, reverse=True))[:amount]

    def _get_palindrome_words(self):
        for word in self._data:
            if self._is_palindrome(word):
                self._palindrome_words.append(word)


class SentenceStatisticCalculator(StatisticCalculator):
    def __init__(self, data):
        super().__init__(data)
        self._statistic = SentenceStatistic()

    def get_statistic(self):
        self._statistic.number = self._get_length()
        self._statistic.average_words_number = self._get_average_words_number()
        self._statistic.longest = self._get_longest(AMOUNT_OF_SHOWN)
        self._statistic.shortest = self._get_shortest(AMOUNT_OF_SHOWN)

        return self._statistic

    def _get_average_words_number(self):
        words_amount = 0
        for sentence in self._data:
            separator = Separator(sentence)
            words = separator.run(WORD_SEPARATORS)
            words_amount += len(words)

        return words_amount / self._statistic.number


class TextStatisticCalculator(StatisticCalculator):
    def __init__(self, data):
        super().__init__(data)
        self._statistic = TextStatistic()

    def get_statistic(self):

        self._statistic.is_palindrome = self._is_text_palindrome([*WORD_SEPARATORS])
        self._statistic.reversed = self._reverse()
        self._statistic.reversed_with_order = self._reverse_with_order()

        return self._statistic

    def _is_text_palindrome(self, punctuation_marks):
        text_without_marks: str = self._data
        for mark in punctuation_marks:
            text_without_marks.replace(mark, "")

        return self._is_palindrome(text_without_marks)

    def _reverse(self):
        return self._data[::-1]

    def _reverse_with_order(self):
        # need some fix
        separator = Separator(self._data)
        words = separator.run(WORD_SEPARATORS, include_separators=True)
        for index, word in enumerate(words):
            if any((char for char in word if char in WORD_SEPARATORS)):
                words[index] = word[len(word)-1] + word[:len(word)-1]

        return "".join(words[::-1])

