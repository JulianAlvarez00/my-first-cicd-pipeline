from flask import Flask, render_template, request, jsonify
from supabase import create_client
import datetime
from config import SUPABASE_URL, SUPABASE_KEY

app = Flask(__name__)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def hello_world():
    return render_template('index.html', message="¡Hola Mundo!")

@app.route('/api/hello')
def api_hello():
    return {'message': '¡Hola Mundo!', 
            'timestamp': datetime.datetime.now().isoformat()}

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        
        # Validación básica
        required_fields = ['name', 'email', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Insertar en Supabase
        result = supabase.table('contact_messages').insert({
            'name': data['name'],
            'email': data['email'],
            'message': data['message']
        }).execute()

        return jsonify({'message': 'Message sent successfully'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)