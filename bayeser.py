import random
import nltk

class Bayeser:

  def __init__(self, ham_phrases, spam_phrases, test_words):
    self.test_words  = test_words
    self.all_words   = self.__get_all_words(ham_phrases.union(spam_phrases))
    labeled_phrases  = self.__label_phrases(ham_phrases, spam_phrases)
    training_set     = self.__get_training_set(labeled_phrases)
    self.__train(training_set)

  def __get_all_words(self, phrases):
    words = []
    for phrase in phrases:
      for word in phrase.split():
        words.append(word)
    return words

  def show_most_informative_features(self):
    self.classifier.show_most_informative_features()

  def classify(self):
    return self.classifier.classify(self.__word_features(self.test_words.split()))

  def __label_phrases(self, ham_phrases, spam_phrases):
    phrases = ([(ham, 'ham') for ham in ham_phrases] + [(spam, 'spam') for spam in spam_phrases])
    random.shuffle(phrases)
    return phrases

  def __get_training_set(self, phrases):
    return [(self.__word_features(n.split()), phrase) for (n, phrase) in phrases]

  def __train(self, training_set):
    self.classifier = nltk.NaiveBayesClassifier.train(training_set)

  def __word_features(self, test_words):
    features = {}
    for word in self.all_words:
      if word in test_words:
        features['contains(%s)' % word] = True
      else:
        features['contains(%s)' % word] = False
    return features