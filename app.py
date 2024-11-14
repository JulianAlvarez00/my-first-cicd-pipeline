from flask import Flask, render_template, request, jsonify
from supabase import create_client, Client
import datetime
from config import SUPABASE_URL, SUPABASE_KEY
import re

app = Flask(__name__)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        
        # Validación detallada
        errors = {}
        
        # Validar nombre
        if not data.get('name'):
            errors['name'] = 'El nombre es requerido'
        elif len(data['name']) < 2:
            errors['name'] = 'El nombre debe tener al menos 2 caracteres'
            
        # Validar email
        if not data.get('email'):
            errors['email'] = 'El email es requerido'
        elif not validate_email(data['email']):
            errors['email'] = 'Email inválido'
            
        # Validar mensaje
        if not data.get('message'):
            errors['message'] = 'El mensaje es requerido'
        elif len(data['message']) < 10:
            errors['message'] = 'El mensaje debe tener al menos 10 caracteres'
            
        if errors:
            return jsonify({'errors': errors}), 400

        # Insertar en Supabase
        result = supabase.table('contact_messages').insert({
            'name': data['name'],
            'email': data['email'],
            'message': data['message']
        }).execute()

        return jsonify({'message': 'Mensaje enviado exitosamente'}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)