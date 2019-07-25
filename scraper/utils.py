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
