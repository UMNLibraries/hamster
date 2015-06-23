import urllib2

class Fetcher:

  def fetch(self, url):
    response = urllib2.urlopen(url)
    return response.read()