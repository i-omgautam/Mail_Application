from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    sender_email = request.form['sender_email']
    receiver_email = request.form['receiver_email']
    subject = request.form['subject']
    body = request.form['body']

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = sender_email
    password = request.form['password']

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

    return "Email sent successfully."

if __name__ == '__main__':
    app.run(debug=True)
