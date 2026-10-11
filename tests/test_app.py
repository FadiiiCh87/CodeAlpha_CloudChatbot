import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import app
def test_chat():
 with app.test_client() as c:
  assert c.post('/api/chat',json={'message':'What is your pricing?'}).json['intent']=='pricing'
  assert c.post('/api/chat',json={'message':''}).status_code==400
  assert c.post('/api/chat',json={'message':'unknown topic'}).json['intent']=='fallback'
