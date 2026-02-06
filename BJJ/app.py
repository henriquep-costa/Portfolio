from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("jiujitsu.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# ---------------------------
# LISTAR
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
# CADASTRAR
# ---------------------------
@app.route('/api/techniques', methods=['POST'])
def add_technique():
    data = request.json

    conn = get_db_connection()
    conn.execute(
        '''
        INSERT INTO techniques (name, category, position, level)
        VALUES (?, ?, ?, ?)
        ''',
        (data['name'], data['category'], data['position'], data['level'])
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Technique added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
