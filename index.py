from flask import Flask
from flask import jsonify

app = Flask(__name__)

if __name__ == '__main__':
    from routes import admin
    app.register_blueprint(admin)
    app.run(debug=True)