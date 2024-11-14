from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="¡Hola Mundo!")

@app.route('/api/hello')
def api_hello():
    return {'message': '¡Hola Mundo!', 
            'timestamp': datetime.datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)