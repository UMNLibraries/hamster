import unittest, os, sys
sys.path.append(os.path.abspath('..'))
from fetcher import Fetcher
import requests
from sure import expect
import httpretty

class FetcherTest(unittest.TestCase):

  @httpretty.activate
  def test_fetch(self):
    httpretty.register_uri(httpretty.GET, "http://example.com",
                       body='[{"title": "Yippee"}]',
                       content_type="application/json")
    fetcher = Fetcher()
    data = fetcher.fetch('http://example.com')
    expect(data).to.equal('[{"title": "Yippee"}]')


if __name__ == '__main__':
    unittest.main()