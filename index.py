from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    name = {'juan':'j'}
    return jsonify(name)
if __name__ == '__main__':
    app.run(debug=True)