# Hamster

A simple *Ham/Spam* web service.This is an experimental project to support ingest filtering for [umbrasearch.org](http://umbrasearch.org).

## Installation

### Requirements

* Python (e.g. via [pyenv](https://github.com/yyuu/pyenv))
* Natural Language Toolkit and Flask

```
$ pip install nltk
$ pip install gunicorn
```

## Usage

* Start the app: `gunicorn -w 4 -b localhost:5000 hamster:run`
* Submit ham, spam and words you want classified as ham or spam to the app:

```
curl --data "spam=
I HATE JUSTIN BIEBER comedy
JUSTIN BIEBER WEDDING comedy
&ham=
story about thew big bang
recently in science discovers were made
&test=justin beiber recently discovers invention with science" http://localhost:5000
> ham
```

```
curl --data "spam=
I HATE JUSTIN BIEBER comedy
JUSTIN BIEBER WEDDING comedy
&ham=
story about thew big bang
recently in science discovers were made
&test=justin beiber comedy recently discovers invention with science wedding" http://localhost:5000
> spam
```

## Testing

### Requirements

```
$ pip install sure
$ pip install httpretty
$ pip install requests
```
### Run Tests

`python -m unittest discover tests`