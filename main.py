from flask import Flask
from pkg.db import S3
from pkg.grep import grep


app = Flask(__name__)
s3 = S3()    

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/grep")
def grep():
    grep()
    return ""




app.run(host="0.0.0.0", port=8000, debug=True)
