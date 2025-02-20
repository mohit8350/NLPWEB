from flask import Flask, render_template, request
from mydb_code import Users
from myapi import API

apio = API()
app = Flask(__name__)
uo = Users()

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_login",  methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = uo.check_user(email, password)
    if response:
        return render_template('home.html', message = "Login successful.")
    else:
        return render_template('login.html', message = "Email or Password incorrect")

@app.route("/perform_registration", methods = ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = uo.check_and_add_new_user(name, email, password)

    if response:
        return render_template('login.html', message = "Registration successful. Login to proceed.")
    else:
        return render_template('register.html', message = "Email already registered.")

@app.route("/home", methods = ['get'])
def home():
    return render_template("home.html")

@app.route("/ner")
def ner():
    return render_template("ner.html")

@app.route("/perform_ner", methods = ['post'])
def perform_ner():
    text = request.form.get("text")
    message_to_show = apio.perform_NER(text)
    print(message_to_show)
    return render_template('ner.html', result = str(message_to_show))

@app.route("/sentiment_analysis")
def sentiment_analysis():
    return render_template('/sentiment_analysis.html')

@app.route("/perform_sentiment_analysis", methods = ['post'])
def perform_sentiment_analysis():
    text = request.form.get("text")
    message_to_show = apio.analyze_sentiment(text)
    return render_template('sentiment_analysis.html', result = message_to_show)

@app.route("/emotion_analysis")
def emotion_analysis():
    return render_template('emotion_analysis.html')

@app.route("/perform_emotion_analysis", methods = ['post'])
def perform_emotion_analysis():
    text = request.form.get("text")
    print(text)
    message_to_show = apio.analyze_emotion(text)
    print(message_to_show)
    return render_template('emotion_analysis.html', result = message_to_show)

@app.route("/abuse_detection")
def abuse_detection():
    return render_template('abuse_detection.html')

@app.route("/perform_abuse_detection", methods = ['post'])
def perform_abuse_detection():
    text = request.form.get("text")
    message_to_show = apio.detect_abuse(text)
    return render_template('abuse_detection.html', result = message_to_show)

app.run(debug=True)