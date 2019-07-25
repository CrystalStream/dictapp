from flask import Flask, request as req, jsonify
from bs4 import BeautifulSoup
import requests

def get_translation_url(text, sl='en', tl='es'):
    return 'https://translate.google.com/?text={}&sl={}&tl={}'.format(text, sl, tl)

def get_translate(html):
    main_container = html.find('div', class_='main-header')
    suggestion_container = main_container.find(id='spelling-correction', style='')
    results_container = main_container.find('div', class_='tlid-results-container')

    translated_text = results_container.find('span', class_='tlid-translation').span.text
    suggestion_text = ''
    if suggestion_container and suggestion_container.text:
        suggestion_text = suggestion_container.a.b.i.text

    return translated_text, suggestion_text
    

app = Flask(__name__)

@app.route('/translate')
def translate_word():
    try:
        word, src_lang, tgt_lang = list(req.args.items())
        translation_html = requests.get(get_translation_url(word[1], src_lang[1], tgt_lang[1]))
        bs_html = BeautifulSoup(translation_html.text, 'html.parser')
        translated_text, suggestion = get_translate(bs_html)

        return jsonify({'code': 200, 'data': { 'translation': translated_text, 'suggestion': suggestion }})
    except:
        return jsonify({'code': 500, 'error': True})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"error": True, "code": 404})

