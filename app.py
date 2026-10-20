from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
import csv, io, os, random

app = Flask(__name__)
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
ATTENDANCE_FILE = os.path.join(DATA_DIR, "attendance.csv")

SAMPLE_STUDENTS = [
    {"id": "STU001", "name": "Aarav Sharma", "status": "Present", "presence": 94, "engagement": 82},
    {"id": "STU002", "name": "Diya Patel", "status": "Present", "presence": 88, "engagement": 91},
    {"id": "STU003", "name": "Kabir Verma", "status": "Late", "presence": 67, "engagement": 63},
    {"id": "STU004", "name": "Meera Joshi", "status": "Present", "presence": 96, "engagement": 78},
    {"id": "STU005", "name": "Ishaan Gupta", "status": "Absent", "presence": 0, "engagement": 0},
    {"id": "STU006", "name": "Ananya Rao", "status": "Present", "presence": 90, "engagement": 86},
]

def load_students():
    return [dict(s) for s in SAMPLE_STUDENTS]

@app.route("/")
def dashboard():
    return render_template("index.html", students=load_students())

@app.route("/api/attendance")
def attendance():
    return jsonify({"students": load_students(), "source": "DEMO DATA — not real biometric recognition",
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M")})

@app.route("/api/suggestions", methods=["POST"])
def suggestions():
    payload = request.get_json(silent=True) or {}
    avg = float(payload.get("avg_engagement", 75))
    attendance = float(payload.get("attendance_rate", 80))
    tips = []
    if avg < 60:
        tips.append("Pause for a short recap and ask a low-stakes question to re-engage the class.")
    elif avg < 80:
        tips.append("Add a brief pair discussion or a quick poll to check understanding.")
    else:
        tips.append("Engagement is strong; maintain the current pace and invite student questions.")
    if attendance < 70:
        tips.append("Review the session timing and share a concise catch-up resource with absent learners.")
    else:
        tips.append("Attendance is stable; continue using clear session goals and reminders.")
    tips.append("Treat behavioral signals as approximate group-level indicators, not proof of a student's attention or learning.")
    return jsonify({"suggestions": tips, "mode": "Local demo rules — no external AI service"})

@app.route("/api/export")
def export_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Student ID", "Name", "Status", "Presence %", "Engagement indicator %"])
    for s in load_students():
        writer.writerow([s["id"], s["name"], s["status"], s["presence"], s["engagement"]])
    mem = io.BytesIO(output.getvalue().encode("utf-8-sig"))
    mem.seek(0)
    return send_file(mem, mimetype="text/csv", as_attachment=True, download_name="demo_attendance.csv")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
