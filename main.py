from flask import Flask, render_template
import wikipediaapi
import re

app = Flask(__name__)
wikipedia = wikipediaapi.Wikipedia("UMA-api-user", "es")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info/<comunity>', methods=['GET'], )
def info(comunity):
    # Recibe el nombre de la comunidad y devuelve información sobre ella y una imagen obtenida de la API de Wikipedia
    page = wikipedia.page(comunity)
    text = page.summary.replace('\n', '<br>')
    clean_text = re.sub(r'\[.*?\]', '', text)
    # clean_text = re.sub(r'\&\d+\&', '', clean_text)
    output = {
        "status": 200,
        "title": page.title,
        "summary": clean_text,
        "url": page.fullurl
    }
    return output

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
