import unittest, os, sys
sys.path.append(os.path.abspath('..'))
from formatter import Formatter
from sure import expect

class FormatterTest(unittest.TestCase):

  def test_format_all(self):
    text = '''
    I HATE JUSTIN BIEBER comedy 
    I LOVE JUSTIN BIEBER comedy 
    JUSTIN BIEBER WEDDING comedy 
    JUSTIN BIEBER HAIR SOS 83 actress albino squirrel bored brittani taylor comedy entertainment fun funky funny happy hollywood hot justin bieber love missal random series sexy shout out sunday show silly sketch vampire vampires weekly 
    IS JUSTIN BIEBER CREEPY OR ADORABLE What Really Happened To Tiger Woods Criminal Names comedy newsinformation 
    Lady Gaga Alejandro Video Eats Rosary Miley Cyrus NO HOMO Spellbound Wins BGT comedy newsinformation 
    Black Eyed Peas on winning their 2nd consecutive AMA 2010 abc aguilera american awards bieber black bon christina clark dick diddy diddydirty dirty divorce dream enrique eyed iglesias jovi justin katy milian money music peas perry pink productions rihanna talkinterview tay the usher 
    '''
    formatter = Formatter(text, "\n")
    words = formatter.run_all()
    expect(words).to.equal(set(['alejandro video rosary miley cyrus spellbound comedy newsinformation','black winning their consecutive aguilera american awards bieber black christina clark diddy diddydirty dirty divorce dream enrique iglesias justin milian money music perry productions rihanna talkinterview usher','justin bieber actress albino squirrel bored brittani taylor comedy entertainment funky funny happy hollywood justin bieber missal random series shout sunday silly sketch vampire vampires weekly', 'justin bieber comedy', 'justin bieber creepy adorable really happened tiger woods criminal names comedy newsinformation', 'justin bieber wedding comedy']))
if __name__ == '__main__':
    unittest.main()