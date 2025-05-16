from flask import Flask, render_template, request, abort
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'bus_stops.db')

def get_db_connection():
    print("📍 Connecting to database path:", DATABASE)
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stops')
def stops():
    page = request.args.get('page', 1, type=int)
    per_page = 20 

    offset = (page - 1) * per_page

    conn = get_db_connection()
    total_query = "SELECT COUNT(*) FROM bus_stops"
    total_count = conn.execute(total_query).fetchone()[0]

    query = "SELECT * FROM bus_stops LIMIT ? OFFSET ?"
    stops = conn.execute(query, (per_page, offset)).fetchall()
    conn.close()

    total_pages = (total_count + per_page - 1) // per_page

    return render_template('stops.html', stops=stops, page=page, total_pages=total_pages)

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
  app.run(host="0.0.0.0", port=3000, debug=True)
