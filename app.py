import os,re
from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
KNOWLEDGE={
 'greeting':(['hello','hi','hey','assalamualaikum'],'Hello! Ask me about pricing, hours, support or cloud hosting.'),
 'pricing':(['price','pricing','cost','plan'],'For pricing, please contact our sales team for a quote.'),
 'hours':(['hours','timing','open'],'Our support portal is available 24/7. Human agent hours depend on the team.'),
 'support':(['support','help','contact'],'Contact support@example.com (demo address; replace before production).'),
 'cloud':(['cloud','hosting','deploy'],'We can discuss scalable cloud deployment, monitoring and backups.'),
 'thanks':(['thank','shukriya'],'You are welcome!')}
def answer(message):
 words=set(re.findall(r'[a-z]+',message.lower()))
 for intent,(patterns,response) in KNOWLEDGE.items():
  if any(set(re.findall(r'[a-z]+',p)).issubset(words) for p in patterns):return intent,response
 return 'fallback','I do not have a verified answer for that. Please contact support.'
@app.get('/')
def home():return render_template('index.html')
@app.get('/health')
def health():return jsonify(status='ok')
@app.post('/api/chat')
def chat():
 data=request.get_json(silent=True) or {};message=data.get('message','')
 if not isinstance(message,str) or not message.strip() or len(message)>1000:return jsonify(error='Message must be 1-1000 characters'),400
 intent,response=answer(message)
 return jsonify(intent=intent,reply=response,model='retrieval-based')
if __name__=='__main__':app.run(debug=os.getenv('FLASK_DEBUG')=='1')
