from flask import Flask, request
from formatter import Formatter
from bayeser import Bayeser

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    ham_phrases  = Formatter(request.form['ham'], "\n").run_all()
    spam_phrases = Formatter(request.form['spam'], "\n").run_all()
    test_phrase = request.form['test']
    classifier = Bayeser(ham_phrases, spam_phrases, test_phrase)
    return classifier.classify()

if __name__ == "__main__":
    app.debug = True
    app.run()