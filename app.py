from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
cipher = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('text', '')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    encrypted_text = cipher.encrypt(data.encode()).decode()
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json.get('text', '')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    try:
        decrypted_text = cipher.decrypt(data.encode()).decode()
        return jsonify({'decrypted_text': decrypted_text})
    except Exception:
        return jsonify({'error': 'Invalid encrypted text'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
