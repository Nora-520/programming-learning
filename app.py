from flask import Flask, request, jsonify, send_from_directory
import student_manager

app = Flask(__name__)

students = student_manager.load_students()

@app.route("/")
def home():
    return send_from_directory("frontend","index.html")

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data["name"]
    score = int(data["score"])

    students[name] = score
    student_manager.save_students(students)

    return jsonify({
        "message":"Student added successfully.",
        "name":name,
        "score":score
    })

if __name__ == "__main__":
    app.run(debug=True)