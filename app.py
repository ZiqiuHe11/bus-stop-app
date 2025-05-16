from flask import Flask, render_template, request, abort
import sqlite3

app = Flask(__name__)

DATABASE = 'bus_stops.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stops')
def stops():
    conn = get_db_connection()
    query = "SELECT * FROM bus_stops LIMIT 100"
    stops = conn.execute(query).fetchall()
    conn.close()
    return render_template('stops.html', stops=stops)

@app.route('/search')
def search():
    term = request.args.get('q', '')
    conn = get_db_connection()
    query = """
        SELECT * FROM details
        WHERE CommonName LIKE ? OR Street LIKE ? OR LocalityName LIKE ?
        LIMIT 100
    """
    results = conn.execute(query, (f'%{term}%', f'%{term}%', f'%{term}%')).fetchall()
    conn.close()
    return render_template('search.html', results=results, term=term)

@app.route('/stop/<code>')
def stop_detail(code):
    conn = get_db_connection()
    query = "SELECT * FROM details WHERE NaptanCode = ?"
    stop = conn.execute(query, (code,)).fetchone()
    conn.close()
    if stop is None:
        abort(404)
    return render_template('stop_detail.html', stop=stop)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

