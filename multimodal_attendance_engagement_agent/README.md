# Multimodal Attendance & Engagement Agent — Demo Prototype

A polished, local-first web dashboard demonstrating attendance overview, illustrative engagement trends, rule-based teaching suggestions, and CSV export.

## Important scope note
This is a **UI/API demo**, not a production multimodal recognition system. It uses fictional sample students and seeded indicators. It does not access a webcam or microphone, identify faces, or measure real attention. Do not use the sample results for real attendance, grading, or disciplinary decisions.

## Features
- Dashboard with attendance and illustrative engagement metrics
- Student roster with status and progress indicators
- Local rule-based teaching suggestions
- Downloadable CSV demo report
- Flask backend; no database or external AI API required
- Responsive interface

## Requirements
- Python 3.8+ (Python 3.10+ recommended)
- Windows, macOS, or Linux

## Run locally
1. Extract the ZIP.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment (optional but recommended).

   Windows:
   ```powershell
   py -m venv .venv
   .venv\\Scripts\\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

The app runs locally. The CSS references Google Fonts, so the font may fall back to system fonts without internet; app functionality remains local.

## API routes
- `GET /api/attendance` — sample roster and timestamp
- `POST /api/suggestions` — local rules-based suggestions; JSON body can include `avg_engagement` and `attendance_rate`
- `GET /api/export` — downloads a demo CSV

## Suggested demo flow
1. Open the dashboard and call out the demo/offline notice.
2. Show the attendance overview and fictional learner statuses.
3. Explain that the trend chart is illustrative.
4. Click **Generate suggestions**.
5. Click **Export CSV**.
6. Explain the privacy-first direction and the next step: replace seeded data with consent-based, validated, on-device sensing and human review.

## Future development roadmap
- Consent and notice workflow; retention controls
- Optional on-device video processing for sustained presence, subject to institutional policy
- Aggregate head-pose/movement signals with explicit limitations
- Optional audio activity features without storing raw audio
- Evaluation for bias, lighting, occlusion, accessibility, and false positives
- Explainable recommendations and instructor override
- Secure authentication, audit logs, and institutional data governance

## Disclaimer
Engagement signals are uncertain proxies and are not a direct measure of learning, emotion, or attention. Obtain informed consent and institutional approval before any real-world sensing.
