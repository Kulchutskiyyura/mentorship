import pytest

from application.server.constants import WORD_SEPARATORS, SENTENCE_SEPARATORS
from application.server.services.separator import Separator
from application.server.services.calculators import (
    CharStatisticCalculator,
    TextStatisticCalculator,
    WordStatisticCalculator
)

from test.application import data_sets


@pytest.mark.parametrize(
    "text, number, frequency, distribution",
    [
        (
                data_sets.TEXT_1,
                37,
                {'O': 2, 'o': 3, '2': 1, 'k': 1, 'l': 1, 'A': 1, ',': 1, 'i': 3, ' ': 9, 'c': 1, '?': 1, 'd': 1, 't': 3,
                 '.': 1, 'H': 1, 'e': 1, 's': 1, 'L': 2, '!': 1, 'E': 1, 'm': 1},
                {'O': 5.405405405405405, 'o': 8.108108108108109, '2': 2.7027027027027026, 'k': 2.7027027027027026,
                 'l': 2.7027027027027026, 'A': 2.7027027027027026, ',': 2.7027027027027026, 'i': 8.108108108108109,
                 ' ': 24.324324324324326, 'c': 2.7027027027027026, '?': 2.7027027027027026, 'd': 2.7027027027027026,
                 't': 8.108108108108109, '.': 2.7027027027027026, 'H': 2.7027027027027026, 'e': 2.7027027027027026,
                 's': 2.7027027027027026, 'L': 5.405405405405405, '!': 2.7027027027027026, 'E': 2.7027027027027026,
                 'm': 2.7027027027027026
                 }

        ),
        (
                data_sets.TEXT_2,
                29,
                {'I': 1, 'd': 1, 't': 3, 'o': 1, 'F': 1, 'n': 4, 's': 3, 'e': 4, ',': 1, 'i': 3, ' ': 5, 'c': 1,
                 'h': 1},
                {'I': 3.4482758620689653, 'd': 3.4482758620689653, 't': 10.344827586206897, 'o': 3.4482758620689653,
                 'F': 3.4482758620689653, 'n': 13.793103448275861, 's': 10.344827586206897, 'e': 13.793103448275861,
                 ',': 3.4482758620689653, 'i': 10.344827586206897, ' ': 17.24137931034483,
                 'c': 3.4482758620689653, 'h': 3.4482758620689653
                 }
        ),
        (
                data_sets.TEXT_3,
                30,
                {'I': 1, 'l': 1, 'f': 1, 'd': 1, '!': 1, 't': 3, 'b': 1, 'o': 2, '.': 1, 'u': 1, 'n': 2, 's': 2, 'e': 2,
                 'i': 4, ' ': 5, '\n': 1, 'h': 1
                 },
                {'I': 3.3333333333333335, 'l': 3.3333333333333335, 'f': 3.3333333333333335, 'd': 3.3333333333333335,
                 '!': 3.3333333333333335, 't': 10.0, 'b': 3.3333333333333335, 'o': 6.666666666666667,
                 '.': 3.3333333333333335, 'u': 3.3333333333333335, 'n': 6.666666666666667, 's': 6.666666666666667,
                 'e': 6.666666666666667, 'i': 13.333333333333334, ' ': 16.666666666666664, '\n': 3.3333333333333335,
                 'h': 3.3333333333333335
                 }
        ),
    ]
)
def test_char_statistic(text, number, frequency, distribution):
    calculator = CharStatisticCalculator(text)

    result = calculator.get_statistic()

    assert result.number == number
    assert result.frequency == frequency
    assert result.distribution == distribution


@pytest.mark.parametrize(
    "text, is_palindrome, reversed, reversed_with_order",
    [
        (
                data_sets.TEXT_1,
                False,
                '?looc 2ti ,kO !ti od steL .mA i OLEH ',
                '?cool it2,Ok!it do Lets.Am i HELO'
        ),
        (
                data_sets.TEXT_2,
                False,
                'ecnetnes dehsiniF ton ,si tI ',
                'sentence Finished not,is It'
        ),
        (
                data_sets.TEXT_3,
                False,
                '!enil oot\ntub .dehsinif si tI ',
                '!line too\nbut.finished is It'
        ),

    ]
)
def test_text_statistic(text, is_palindrome, reversed, reversed_with_order):
    calculator = TextStatisticCalculator(text)

    result = calculator.get_statistic()

    result.reversed = reversed
    result.is_palindrome = is_palindrome
    result.reversed_with_order = reversed_with_order


@pytest.mark.parametrize(
    "text, number,  average_length, most_used, longest, shortest, number_palindrome, longest_palindrome",
    [
        (
            data_sets.TEXT_1,
            9,
            2.6666666666666665,
            ['it2', 'do', 'i', 'HELO', 'Ok', 'cool', 'it', 'Am', 'Lets'],
            ['HELO', 'Lets', 'cool', 'it2', 'Am', 'do', 'it', 'Ok', 'i'],
            ['i', 'Am', 'do', 'it', 'Ok', 'it2', 'HELO', 'Lets', 'cool'],
            1,
            ['i']
        ),
        (
            data_sets.TEXT_2,
            5,
            4.6,
            ['sentence', 'not', 'is', 'Finished', 'It'],
            ['Finished', 'sentence', 'not', 'It', 'is'],
            ['It', 'is', 'not', 'Finished', 'sentence'],
            0,
            []
        ),
        (
            data_sets.TEXT_3,
            6,
            3.6666666666666665,
            ['finished', 'but', 'is', 'line', 'too', 'It'],
            ['finished', 'line', 'but', 'too', 'It', 'is'],
            ['It', 'is', 'but', 'too', 'line', 'finished'],
            0,
            []
        ),

    ]
)
def test_word_statistic(
        text,
        number,
        average_length,
        most_used,
        longest,
        shortest,
        number_palindrome,
        longest_palindrome
):
    words = Separator(text).run(WORD_SEPARATORS)
    calculator = WordStatisticCalculator(words)

    result = calculator.get_statistic()

    assert result.number == number
    assert result.average_length == average_length
    assert result.longest == longest
    assert result.shortest == shortest
    assert result.number_palindrome == number_palindrome
    assert result.longest_palindrome == longest_palindrome


@pytest.mark.parametrize(
    "text, number, average_length, most_used, longest, shortest, number_palindrome, longest_palindrome",
    [
        (
            data_sets.TEXT_1,
            3,
            12.333333333333334,
            [' Lets do it!', ' Ok, it2 cool?', ' HELO i Am.'],
            [' Ok, it2 cool?', ' Lets do it!', ' HELO i Am.'],
            [' HELO i Am.', ' Lets do it!', ' Ok, it2 cool?'],
            0,
            []
        ),
        (
            data_sets.TEXT_2,
            1,
            29.0,
            [' It is, not Finished sentence'],
            [' It is, not Finished sentence'],
            [' It is, not Finished sentence'],
            0,
            []
        ),
        (
            data_sets.TEXT_3,
            2,
            15.0,
            [' It is finished.', ' but\ntoo line!'],
            [' It is finished.', ' but\ntoo line!'],
            [' but\ntoo line!', ' It is finished.'],
            0,
            []
        ),

    ]
)
def test_sentence_statistic(
        text,
        number,
        average_length,
        most_used,
        longest,
        shortest,
        number_palindrome,
        longest_palindrome
):
    words = Separator(text).run(SENTENCE_SEPARATORS, include_separators=True)
    calculator = WordStatisticCalculator(words)

    result = calculator.get_statistic()

    assert result.number == number
    assert result.average_length == average_length
    assert result.longest == longest
    assert result.shortest == shortest
    assert result.number_palindrome == number_palindrome
    assert result.longest_palindrome == longest_palindrome
