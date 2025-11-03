from flask import Flask

app = Flask(__name__)

# Rota da Página inicial
@app.route('/')
def hello_world():
    return  render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
