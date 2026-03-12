from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory list to store students
students = [
    {"name": "Your Name", "grade": 10, "section": "Zechariah"}
]

@app.route('/')
def home():
    return "Welcome to the Student API!"

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Search student by name (query parameter ?name=...)
@app.route('/student/search', methods=['GET'])
def search_student():
    name = request.args.get('name', '').lower()
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400
    
    results = [s for s in students if name in s['name'].lower()]
    if results:
        return jsonify(results)
    else:
        return jsonify({"message": "No student found with that name"}), 404

# Add a new student (POST JSON: {"name":"...", "grade":..., "section":"..."})
@app.route('/student/add', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or "name" not in data or "grade" not in data or "section" not in data:
        return jsonify({"error": "Missing required fields: name, grade, section"}), 400
    
    new_student = {
        "name": data["name"],
        "grade": data["grade"],
        "section": data["section"]
    }
    students.append(new_student)
    return jsonify({"message": "Student added successfully", "student": new_student}), 201

if __name__ == '__main__':
    app.run(debug=True)
