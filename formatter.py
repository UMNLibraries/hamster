import string
from string import digits

import pprint

class Formatter:

  def __init__(self, text, split_token):
    self.words = text.split(split_token)

  def strip_words(self, words):
    return map(str.strip, words)

  def lower_words(self, words):
    return map(str.lower, words)

  def remove_punctuation(self, words):
    f = lambda text : text.translate(string.maketrans("",""), string.punctuation)
    return map(f, words)

  def remove_digits(self, words):
    f = lambda text : text.translate(None, digits)
    return map(f, words)

  def remove_short_words(self, words):
    f = lambda text : ' '.join(word for word in text.split() if len(word) > 4)
    return map(f, words)

  def remove_empties(self, words):
    return filter(None, words)

  def remove_duplicates(self, words):
    return set(words)

  def run_all(self):
    words = self.words
    words = self.strip_words(words)
    words = self.lower_words(words)
    words = self.lower_words(words)
    words = self.remove_punctuation(words)
    words = self.remove_digits(words)
    words = self.remove_short_words(words)
    words = self.remove_empties(words)
    words = self.remove_duplicates(words)
    return words




