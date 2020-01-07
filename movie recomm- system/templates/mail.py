from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['DEBUG']=True
app.config['TESTING']=True
app.config['MAIL_SERVER']='smtp.hushmail.com'
app.config['MAIL_PORT'] = 578
app.config['MAIL_USERNAME'] = 'vewap@techgroup.top'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_DEFAULT_SENDER']='vewap@techgroup.top'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello',sender=['vewap@techgroup.top'],  recipients = ['vewap@techgroup.top'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent msg"

if __name__ == '__main__':
   app.run(debug = True)