from flask import Flask, send_from_directory, render_template, jsonify

app = Flask(__name__, static_folder='dist/static', template_folder='dist')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    try:
        return send_from_directory('dist', path)
    except:
        return render_template('index.html')

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    # Sample data, replace with actual data retrieval logic
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
