from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='')
import requests
import csv
import secrets

app = Flask(__name__)

app.config['DEBUG'] = True

usuarios_autorizados = ["usuario1", "usuario2", "usuario3"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_instagram_data', methods=['POST'])
def get_instagram_data():
    try:
        username = request.form['username']
        access_token = '821962829724167' 

        url = f'https://api.instagram.com/v1/users/self/media/recent/?access_token={access_token}'
        response = requests.get(url)
        response.raise_for_status()  

        data = response.json()

        posts = []

        for post in data['data']:
            posts.append({
                'created_time': post['created_time'],
                'text': post.get('caption', {}).get('text', ''),
                'likes': post['likes']['count']
            })

        with open('instagram_data.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['created_time', 'text', 'likes'])
            writer.writeheader()
            writer.writerows(posts)

        return "Dados coletados e salvos em 'instagram_data.csv'."
    except requests.exceptions.HTTPError as err:
        return f"Erro ao acessar a API do Instagram: {err}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

@app.route('/desautorizar/<username>')
def desautorizar(username):
    if username in usuarios_autorizados:
        usuarios_autorizados.remove(username)
        return redirect(url_for('confirmacao'))
    else:
        return "Usuário não autorizado para desautorização."

@app.route('/confirmacao')
def confirmacao():
    return "Você foi desautorizado com sucesso."

if __name__ == '__main__':
    app.run(debug=True)
