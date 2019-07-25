import os
import sys
import unittest
from unittest import mock
module_dir = os.path.dirname('..')
sys.path.append(os.path.join(module_dir, '../scraper/'))

from app import app
from fixtures import car_es_2_en

def get_translation_url(text, sl='en', tl='es'):
    return 'https://translate.google.com/?text={}&sl={}&tl={}'.format(text, sl, tl)

def mocked_request(query):
    class MockResponse():
        def __init__(self, **kwargs):
            self.text = kwargs['html']
    
    switcher = {
        get_translation_url('Cars'): MockResponse(html=car_es_2_en.html),
    }

    return switcher.get(query, MockResponse(html='<p class="not-found">Not found</p>'))

class ScraperTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_single_endpoint(self):
        """ Should return a 404 """
        endpoints = [
            '/',
            '/hello',
            '/testing'
        ]
        for endpoint in endpoints:
            response = self.client.get(endpoint).get_json()
            self.assertEqual(response['error'], True)
            self.assertEqual(response['code'], 404)

    @mock.patch('app.requests.get', side_effect=mocked_request)
    def test_basic_search_en_to_es(self, mocked_req):
        """ Should return the translated word """

        response = self.client.get('/translate?text=Cars&sl=en&tl=es').get_json()
        self.assertEqual(response['code'], 200)
        self.assertEqual(response['data']['translation'], 'Coches')

if __name__ == "__main__":
    unittest.main()
    