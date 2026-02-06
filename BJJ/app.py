from flask import Flask, jsonify, request, render_template
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "jiujitsu.db"

# ---------------------------
# FUNÇÃO PARA CONEXÃO E CRIAÇÃO DE TABELA
# ---------------------------
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_NAME):
        print("Banco não existe. Criando jiujitsu.db...")
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS techniques (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            position TEXT,
            level TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco inicializado e tabela pronta!")

# ---------------------------
# ROTA PRINCIPAL
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------------------
# LISTAR TÉCNICAS
# ---------------------------
@app.route('/api/techniques', methods=['GET'])
def get_techniques():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM techniques').fetchall()
    conn.close()

    techniques = []
    for row in rows:
        techniques.append({
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'position': row['position'],
            'level': row['level']
        })

    return jsonify(techniques)

# ---------------------------
# ADICIONAR TÉCNICA
# ---------------------------
@app.route('/api/techniques', methods=['POST'])
def add_technique():
    data = request.json

    if not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400

    conn = get_db_connection()
    conn.execute(
        '''
        INSERT INTO techniques (name, category, position, level)
        VALUES (?, ?, ?, ?)
        ''',
        (data['name'], data.get('category'),
         data.get('position'), data.get('level'))
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Technique added'}), 201

# ---------------------------
# INICIALIZA BANCO E RODA APP
# ---------------------------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
