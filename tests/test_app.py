import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app

def test_faq_and_fallback():
    with app.test_client() as c:
        assert c.get("/health").json["status"] == "ok"
        assert c.post("/api/chat", json={"message": "What is your pricing?"}).json["intent"] == "pricing"
        assert c.post("/api/chat", json={"message": "مرحبا"}).json["intent"] == "greeting"
        assert c.post("/api/chat", json={"message": "shukriya"}).json["intent"] == "thanks"
        assert c.post("/api/chat", json={"message": "unknown topic xyz"}).json["intent"] == "fallback"
        assert c.post("/api/chat", json={"message": ""}).status_code == 400
        assert c.post("/api/chat", json={"message": "x" * 1001}).status_code == 400
        assert c.post("/api/chat", json=[]).status_code == 400
        assert len(c.get("/api/topics").json["topics"]) >= 5
