from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    # Dung lenh request de ban POST len rasa
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Lấy từ form
        user_message = request.form['user_message']
        noidungchathientai = request.form['chat_content']


        # Bắn lên rasa
        r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": "value", "message": user_message})
        print(r.json())
        noidungchathientai += "\n[BẠN]: " + user_message
        noidungchathientai += "\n[BOT]: " + r.json()[0]["text"]

        return render_template('index.html', noidungchathientai=noidungchathientai)

# Thuc thi server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)




