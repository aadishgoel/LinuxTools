from flask import *
from pkg.db import AWSFileStore
from pkg.grep import Grep, ExactMatchGrepStrategy


app = Flask(__name__)
fileStore = AWSFileStore()
grep = Grep(ExactMatchGrepStrategy)

@app.route("/")
def home():
    return "Hello, Welcome to Cloud Tools "


@app.route("/grep")
def _grep(methods=['GET']):
    inputParamValidaton = ["searchString", "from", "to"]
    reqData = json.loads(request.data)
    for inputParam in inputParamValidaton:
        if inputParam not in reqData:
            return "Missing Input Field: " + inputParam, 403

    return grep.search(fileStore, reqData["searchString"], reqData["from"], reqData["to"])


app.run(host="0.0.0.0", port=8000, debug=True)
