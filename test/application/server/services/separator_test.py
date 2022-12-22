import pytest

from application.server.constants import WORD_SEPARATORS, SENTENCE_SEPARATORS
from application.server.services.separator import Separator
from test.application import data_sets


@pytest.mark.parametrize(
    "text, expected_result, include_separators",
    [
        (data_sets.TEXT_1, ['HELO ', 'i ', 'Am.', 'Lets ', 'do ', 'it!', 'Ok,', 'it2 ', 'cool?'], True),
        (data_sets.TEXT_2, ['It ', 'is,', 'not ', 'Finished ', 'sentence'], True),
        (data_sets.TEXT_3, ['It ', 'is ', 'finished.', 'but\n', 'too ', 'line!'], True),
        (data_sets.TEXT_1, ['HELO', 'i', 'Am', 'Lets', 'do', 'it', 'Ok', 'it2', 'cool'], False),
        (data_sets.TEXT_2, ['It', 'is', 'not', 'Finished', 'sentence'], False),
        (data_sets.TEXT_3, ['It', 'is', 'finished', 'but', 'too', 'line'], False)
    ]
)
def test_separator_word_run(text, expected_result, include_separators):
    separator = Separator(text)

    result = separator.run(WORD_SEPARATORS, include_separators=include_separators)
    assert result == expected_result


@pytest.mark.parametrize(
    "text, expected_result, include_separators",
    [
        (data_sets.TEXT_1, [' HELO i Am.', ' Lets do it!', ' Ok, it2 cool?'], True),
        (data_sets.TEXT_2, [' It is, not Finished sentence'], True),
        (data_sets.TEXT_3, [' It is finished.', ' but\ntoo line!'], True),
        (data_sets.TEXT_1, [' HELO i Am', ' Lets do it', ' Ok, it2 cool'], False),
        (data_sets.TEXT_2, [' It is, not Finished sentence'], False),
        (data_sets.TEXT_3, [' It is finished', ' but\ntoo line'], False)
    ]
)
def test_separator_sentences_run(text, expected_result, include_separators):
    separator = Separator(text)

    result = separator.run(SENTENCE_SEPARATORS, include_separators=include_separators)

    assert result == expected_result
