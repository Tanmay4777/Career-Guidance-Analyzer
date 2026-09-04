"""
AI Career Guidance Assistant - Backend API
Student: Tanmay Sah (DAS008051) | Data Alcott Systems
"""

from flask import Flask, jsonify, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html'))

@app.route('/index.html')
def index_html():
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html'))

CAREER_DATA = {
    "nlp": {
        "role": "AI & NLP Engineer",
        "skills": ["Python", "PyTorch", "Transformers", "BERT", "FastAPI", "Vector Databases"],
        "roadmap": "Core NLP -> Deep Learning -> Hugging Face & RAG -> Production Deployment",
        "salary_range": "₹12 - 28 LPA",
        "top_companies": ["Google", "Microsoft", "Data Alcott Systems", "OpenAI"]
    },
    "data_science": {
        "role": "Data Scientist",
        "skills": ["Python", "Pandas", "Scikit-learn", "SQL", "Statistics", "Tableau"],
        "roadmap": "Statistics & SQL -> EDA & Feature Engineering -> Classical ML -> Model Deployment",
        "salary_range": "₹10 - 24 LPA",
        "top_companies": ["Amazon", "Fractal", "Deloitte", "Adobe"]
    },
    "computer_vision": {
        "role": "Computer Vision Engineer",
        "skills": ["Python", "OpenCV", "PyTorch", "YOLOv8", "CNNs", "TorchVision"],
        "roadmap": "Image Fundamentals -> CNN Architectures -> Object Detection -> Edge AI",
        "salary_range": "₹11 - 26 LPA",
        "top_companies": ["Tesla", "Qualcomm", "Intel", "Samsung R&D"]
    }
}

@app.route("/api/career_guidance", methods=["POST"])
def career_guidance():
    payload = request.get_json() or {}
    query = payload.get("message", "").lower()

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Intent Classification
    if "salary" in query or "ctc" in query or "compensation" in query:
        return jsonify({
            "intent": "SALARY_INQUIRY",
            "data": {k: v["salary_range"] for k, v in CAREER_DATA.items()}
        })

    matched_role = None
    if "nlp" in query or "ai" in query or "language" in query:
        matched_role = CAREER_DATA["nlp"]
    elif "data" in query or "science" in query:
        matched_role = CAREER_DATA["data_science"]
    elif "vision" in query or "cv" in query or "image" in query:
        matched_role = CAREER_DATA["computer_vision"]

    if matched_role:
        return jsonify({
            "intent": "CAREER_PATH_DETAILS",
            "details": matched_role
        })

    return jsonify({
        "intent": "GENERAL_GUIDANCE",
        "message": "Explore roles in NLP, Data Science, or Computer Vision, or inquire about salary trends and interview prep."
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)