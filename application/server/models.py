from application import db


class AnalysisReport(db.Document):
    name = db.StringField()
    text = db.StringField()
    time_to_process = db.FloatField()
    datatime = db.StringField()
    char_number = db.IntField()
    char_frequency = db.DictField()
    char_distribution = db.DictField()

    words_number = db.IntField()
    words_average_length = db.FloatField()
    most_used_words = db.ListField()
    longest_words = db.ListField()
    shortest_words = db.ListField()
    number_palindrome = db.IntField()
    longest_palindrome = db.ListField()

    sentences_number = db.IntField()
    sentences_average_words_number = db.FloatField()
    longest_sentences = db.ListField()
    shortest_sentences = db.ListField()

    is_palindrome = db.BooleanField()
    reversed = db.StringField()
    reversed_with_order = db.StringField()
