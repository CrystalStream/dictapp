from flask import Flask, request as req, jsonify
from bs4 import BeautifulSoup
import requests
import utils

app = Flask(__name__)

@app.route('/translate')
def translate_word():
    try:
        word, src_lang, tgt_lang = list(req.args.items())
        translation_html = requests.get(utils.get_translation_url(word[1], src_lang[1], tgt_lang[1]))
        bs_html = BeautifulSoup(translation_html.text, 'html.parser')
        translated_text, suggestion = utils.get_translate(bs_html)

        return jsonify({'code': 200, 'data': { 'translation': translated_text, 'suggestion': suggestion }})
    except:
        return jsonify({'code': 500, 'error': True})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"error": True, "code": 404})

