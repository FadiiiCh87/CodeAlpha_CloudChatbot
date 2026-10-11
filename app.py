import os, re
from difflib import SequenceMatcher
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024
FAQ = {
 "greeting": {"keywords": ["hello", "hi", "hey", "assalamualaikum", "salam", "مرحبا", "السلام عليكم"], "answer": "Hello! Ask about pricing, hours, support or cloud hosting."},
 "pricing": {"keywords": ["price", "pricing", "cost", "plan", "kitna", "qeemat", "سعر", "اسعار"], "answer": "Pricing depends on your requirements. Contact the service provider for an accurate quote."},
 "hours": {"keywords": ["hours", "timing", "open", "working hours", "waqt", "مواعيد", "ساعات"], "answer": "This demo portal is accessible 24/7; human support hours are not configured."},
 "support": {"keywords": ["support", "help", "contact", "madad", "مساعدة", "دعم"], "answer": "Please use the business's verified contact channel. No support address is configured in this demo."},
 "cloud": {"keywords": ["cloud", "hosting", "deploy", "server", "استضافة", "سحابة"], "answer": "Cloud deployment can include hosting, monitoring, backups and scaling."},
 "thanks": {"keywords": ["thank", "thanks", "shukriya", "شكرا"], "answer": "You're welcome!"}
}
def answer(message):
    q = " ".join(message.casefold().split())
    words = set(re.findall(r"\w+", q, re.UNICODE))
    ranked = []
    for intent, item in FAQ.items():
        scores = []
        for keyword in item["keywords"]:
            term = keyword.casefold()
            exact = term in q if " " in term else term in words
            scores.append(1.0 if exact else SequenceMatcher(None, q, term).ratio() * 0.68)
        ranked.append((max(scores), intent))
    score, intent = max(ranked)
    if score < 0.56:
        return "fallback", "I don't have a verified answer. Try pricing, hours, support or cloud hosting.", 0
    return intent, FAQ[intent]["answer"], round(score, 2)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/topics")
def topics():
    return jsonify(topics=[{"intent": key, "keywords": value["keywords"][:3]} for key, value in FAQ.items()])

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="A JSON object is required"), 400
    message = data.get("message", "")
    if not isinstance(message, str) or not message.strip() or len(message) > 1000:
        return jsonify(error="Message must be 1-1000 characters"), 400
    intent, reply, confidence = answer(message)
    return jsonify(intent=intent, reply=reply, confidence=confidence, model="FAQ retrieval (not generative AI)", source="curated FAQ" if intent != "fallback" else None)

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
