from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Default'

if __name__ == '__main__':
    app.run(debug=True)