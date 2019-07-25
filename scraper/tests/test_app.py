import os
import sys
import unittest
from unittest import mock
module_dir = os.path.dirname('..')
sys.path.append(os.path.join(module_dir, '../scraper/'))

from app import app
import utils
from fixtures import basic_es_2_en, basic_en_2_es, suggestion_en_to_es, suggestion_es_to_en, advanced_search

def mocked_request(query):
    class MockResponse():
        def __init__(self, **kwargs):
            self.text = kwargs['html']
    
    switcher = {
        utils.get_translation_url('Cars'): MockResponse(html=basic_es_2_en.html),
        utils.get_translation_url('Coches', sl='es', tl='en'): MockResponse(html=basic_en_2_es.html),
        utils.get_translation_url('Widt'): MockResponse(html=suggestion_en_to_es.html),
        utils.get_translation_url('Jugand', sl='es', tl='en'): MockResponse(html=suggestion_es_to_en.html),
        utils.get_translation_url('Yo quisiera comprarme la mascara pero no se si me alcance'): MockResponse(html=advanced_search.html),
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
        """ Should return the translated en to es word """

        response = self.client.get('/translate?text=Cars&sl=en&tl=es').get_json()
        self.assertEqual(response['code'], 200)
        self.assertEqual(response['data']['translation'], 'Coches')
    
    @mock.patch('app.requests.get', side_effect=mocked_request)
    def test_basic_search_es_to_en(self, mocked_req):
        """ Should return the translated es to en word """

        response = self.client.get('/translate?text=Coches&sl=es&tl=en').get_json()
        self.assertEqual(response['code'], 200)
        self.assertEqual(response['data']['translation'], 'Cars')
    
    @mock.patch('app.requests.get', side_effect=mocked_request)
    def test_basic_search_en_to_es_with_suggestion(self, mocked_req):
        """ Should return the translated en to es word with suggestions """

        response = self.client.get('/translate?text=Widt&sl=en&tl=es').get_json()
        self.assertEqual(response['code'], 200)
        self.assertEqual(response['data']['translation'], 'Ancho')
        self.assertEqual(response['data']['suggestion'], 'Width')
    
    @mock.patch('app.requests.get', side_effect=mocked_request)
    def test_basic_search_es_to_en_with_suggestion(self, mocked_req):
        """ Should return the translated en to es word with suggestions """

        response = self.client.get('/translate?text=Jugand&sl=es&tl=en').get_json()
        self.assertEqual(response['code'], 200)
        self.assertEqual(response['data']['translation'], 'Playing')
        self.assertEqual(response['data']['suggestion'], 'Jugando')
    
    @mock.patch('app.requests.get', side_effect=mocked_request)
    def test_advanced_search_en_to_es(self, mocked_req):
        """ Should return the translated en to es word with suggestions """
        text = "Yo quisiera comprarme la mascara pero no se si me alcance"
        expected_text = "I would like to buy the mask but I don't know if it reaches me"

        response = self.client.get('/translate?text={}&sl=en&tl=es'.format(text)).get_json()
        self.assertEqual(response['code'], 200)
        self.assertEqual(response['data']['translation'], expected_text)

if __name__ == "__main__":
    unittest.main()
    