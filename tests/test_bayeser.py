import unittest, os, sys
sys.path.append(os.path.abspath('..'))
from bayeser import Bayeser
from sure import expect

class BayeserTest(unittest.TestCase):
  spam_words = set(['justin bieber is so cool', 'russian hiphop is the best', 'viagra on sale now'])
  ham_words  = set(['african american performance artist', 'jazz age show revives interest in jazz', 'gallery opening portraying slavery'])

  def test_ham(self):
    test_words = 'african american bieber cool artist jazz'
    bayeser = Bayeser(self.ham_words, self.spam_words, test_words)
    expect(bayeser.classify()).to.equal('ham')

  def test_spam(self):
    test_words = 'african american bieber cool artist jazz viagra on sale'
    bayeser = Bayeser(self.ham_words, self.spam_words, test_words)
    expect(bayeser.classify()).to.equal('spam')

if __name__ == '__main__':
    unittest.main()