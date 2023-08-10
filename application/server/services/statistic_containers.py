from dataclasses import dataclass


@dataclass
class CharacterStatistic:
    number: int = None
    frequency: dict = None
    distribution: dict = None


@dataclass
class WordStatistic:
    number: int = None
    average_length: float = None
    most_used: list = None
    longest: list = None
    shortest: list = None
    number_palindrome: int = None
    longest_palindrome: list = None


@dataclass
class SentenceStatistic:
    number: int = None
    average_words_number: float = None
    longest: list = None
    shortest: list = None


@dataclass
class TextStatistic:
    is_palindrome: bool = None
    reversed: str = None
    reversed_with_order: str = None


@dataclass
class Statistic:
    character_statistic: CharacterStatistic = None
    word_statistic: WordStatistic = None
    sentence_statistic: SentenceStatistic = None
    text_statistic: TextStatistic = None
    time_to_process: float = None
    datatime: str = None