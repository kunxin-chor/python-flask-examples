from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    name = "Paul"
    return "<h1>Hello {}</h1>".format(name)
    
@app.route('/about-us')
def about_us():
    return "<h1>About Us</h1>"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)