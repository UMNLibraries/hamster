from flask import Flask, request

from formatter import Formatter
from bayeser import Bayeser
from fetcher import Fetcher

import json

app = Flask(__name__)

import pprint

@app.route("/")
def hello():
    pp = pprint.PrettyPrinter(indent=4)
    fetcher = Fetcher()
    ham_phrases  = Formatter(fetcher.fetch(request.args.get('ham_url', '')), "\n").run_all()
    spam_phrases = Formatter(fetcher.fetch(request.args.get('spam_url', '')), "\n").run_all()
    test_phrase = request.args.get('test_phrase', '')
    classifier = Bayeser(ham_phrases, spam_phrases, test_phrase)
    return classifier.classify()

if __name__ == "__main__":
    app.debug = True
    app.run()