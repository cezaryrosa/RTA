
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    name = request.args.get("name", "")
    return f"hello {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

app.run()
# default port is 5000
# default add
