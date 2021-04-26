# Importando Flask
from flask import Flask

# definindo objeto da classe
app = Flask(__name__)

@app.route('/') # caminho da rota
def index():
    return "Página Inicial" # Mostra o conteúdo na tela

# so roda o app se for o arquivo principal
if __name__ == "__main__":
    app.run()