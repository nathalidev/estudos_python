from flask import Flask
from flask import render_template #função do flask para renderização de pagina do front
from flask import jsonify # função para retorno de dados em json pro front usar
from flask import redirect, url_for #joga o usuário pra url em questão

app = Flask(__name__) 

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
