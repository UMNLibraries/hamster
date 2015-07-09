from flask import Flask, request
from formatter import Formatter
from bayeser import Bayeser
from werkzeug.wrappers import Request

app = Flask(__name__)
@app.route("/", methods=['POST'])
def run(environ, start_response):
  request = Request(environ)
  ham_phrases = Formatter(request.form['ham'], "\n").run_all()
  spam_phrases = Formatter(request.form['spam'], "\n").run_all()
  test_phrase = request.form['test']
  classifier = Bayeser(ham_phrases, spam_phrases, test_phrase)
  result = classifier.classify()
  start_response("200 OK", [
    ("Content-Type", "text/plain"),
    ("Content-Length", str(len(result)))
  ])
  return iter([result])

if __name__ == "__main__":
    app.run()