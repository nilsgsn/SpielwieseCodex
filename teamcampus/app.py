from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
teams = {}

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to TeamCampus'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    if username in users:
        return jsonify({'error': 'User exists'}), 400
    users[username] = {'password': password, 'team': None}
    return jsonify({'message': 'User registered'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and user['password'] == password:
        return jsonify({'message': 'Login successful'})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/teams', methods=['GET'])
def list_teams():
    return jsonify({'teams': list(teams.keys())})

@app.route('/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Team name required'}), 400
    if name in teams:
        return jsonify({'error': 'Team exists'}), 400
    teams[name] = {'courses': []}
    return jsonify({'message': 'Team created'}), 201

@app.route('/team/<team_name>', methods=['GET'])
def get_team(team_name):
    team = teams.get(team_name)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    return jsonify({'team': team_name, 'courses': team['courses']})

@app.route('/team/<team_name>/courses', methods=['POST'])
def add_course(team_name):
    team = teams.get(team_name)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    data = request.get_json()
    course = data.get('course')
    if not course:
        return jsonify({'error': 'Course name required'}), 400
    team['courses'].append(course)
    return jsonify({'message': 'Course added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
